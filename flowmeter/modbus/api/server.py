# coding=utf-8
import threading
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from flowmeter.exceptions import OfflineException
from flowmeter.modbus.api import frame
from flowmeter.applications.api import operator as app_opr_api
from flowmeter.applications.api import meter as app_meter_api
from flowmeter.applications.api import log as app_log_api
from twisted.internet import task
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.api import configure as conf_configure_api
from flowmeter.config.api import operator as conf_opr_api
from flowmeter.config.api import log as conf_log_api
from flowmeter.config.db.log_table import OprLog


import logging

logger = logging.getLogger('log')


class FlowMeterClients:
    """
    流量计DTU客户端与服务器端的连接集合
    """

    dtu_to_connect_map = {}
    ip_to_dtu_map = {}
    lock = threading.Lock()

    @staticmethod
    def add(dtu_no, ip, connect):
        """
        如果添加的dtu连接不存在，则返回True，否则返回False
        :param dtu_no:
        :param ip:
        :param connect:
        :return:
        """
        FlowMeterClients.lock.acquire()
        try:
            if ip not in FlowMeterClients.ip_to_dtu_map.keys():
                FlowMeterClients.dtu_to_connect_map[dtu_no] = connect
                FlowMeterClients.ip_to_dtu_map[ip] = dtu_no
                return True
        finally:
            FlowMeterClients.lock.release()
        return False

    @staticmethod
    def get_connect(dtu_no):
        FlowMeterClients.lock.acquire()
        try:
            connect = FlowMeterClients.dtu_to_connect_map.get(dtu_no)
        finally:
            FlowMeterClients.lock.release()

        return connect

    @staticmethod
    def get_dtu_no(ip):
        FlowMeterClients.lock.acquire()
        dtu_no = FlowMeterClients.ip_to_dtu_map[ip] if ip in FlowMeterClients.ip_to_dtu_map.keys() else None
        FlowMeterClients.lock.release()
        return dtu_no

    @staticmethod
    def remove(ip):

        FlowMeterClients.lock.acquire()
        try:
            dtu_no = FlowMeterClients.get_dtu_no(ip)
            if dtu_no is None:
                return
            del FlowMeterClients.ip_to_dtu_map[ip]

            if dtu_no in FlowMeterClients.dtu_to_connect_map.keys():
                del FlowMeterClients.dtu_to_connect_map[dtu_no]
        finally:
            FlowMeterClients.lock.release()


class FlowMeterServer(Protocol):
    """
    与流量计通信的服务器
    """

    # 心跳包数据帧字节数
    HEART_BEAT_BYTE_NUM = 2
    # 16进制的比特数
    HEX_NUM = 8

    def __init__(self, factory):
        self.factory = factory

    @staticmethod
    def __is_heart_beat(data_frame):

        if len(data_frame) <= FlowMeterServer.HEART_BEAT_BYTE_NUM:
            return True
        else:
            return False

    @staticmethod
    def __heart_beat_transfer_dtu_no(heart_beat):
        """
        心跳包数据帧转DTU编号
        :param heart_beat:
        :return:
        """
        dtu_no = 0
        for byte in heart_beat:
            dtu_no = (dtu_no << FlowMeterServer.HEX_NUM) + byte
        logger.info("dtu_no:{}".format(dtu_no))
        return dtu_no

    def connectionMade(self):
        """
        开始连接
        :return:
        """
        pass

    def connectionLost(self, reason):
        """
        断开连接
        :param reason:
        :return:
        """
        ip = self.transport.getPeer().host
        dtu_no = FlowMeterClients.get_dtu_no(ip)

        logger.info("ip：{}，dtu_no：{}断开连接".format(ip, dtu_no))

        # 更新DTU离线状态
        try:
            conf_dtu_api.update_dtu_offline_state(dtu_no)
        except Exception as ex:
            logger.error(str(ex))

        FlowMeterClients.remove(ip)

    def dataReceived(self, data_frame):
        """
        数据接收
        :param data_frame
        :return:
        """
        ip = self.transport.getPeer().host

        logger.info("ip: {}，发送了{}数据帧".format(ip, data_frame))

        # 回应心跳包
        if FlowMeterServer.__is_heart_beat(data_frame):
            # 添加新的客户端连接
            dtu_no = FlowMeterServer.__heart_beat_transfer_dtu_no(data_frame)
            connect = self.transport
            FlowMeterClients.add(dtu_no, ip, connect)
            # 回应心跳包
            self.transport.getHandle().sendall(data_frame)

            # 更新上线状态
            try:
                conf_dtu_api.update_dtu_online_state(dtu_no)
            except Exception as ex:
                logger.error(str(ex))

        else:
            # 先解析数据帧
            try:
                FlowMeterServer.__data_receiver_handler(ip, data_frame)
            except Exception as ex:
                logger.error(str(ex))

    @staticmethod
    def __data_receiver_handler(ip, data_frame):
        """收到数据帧的处理函数"""
        dtu_no = FlowMeterClients.get_dtu_no(ip)
        data = frame.parse_data_frame(data_frame)
        # 先执行一条等待结果的操作
        opr = app_opr_api.execute_wait_remote_op(dtu_no, data['address'], data['opr_type'])
        # 更新仪表数据
        if opr is not None:
            if 'data' in data.keys() and isinstance(data['data'], dict):
                app_log_api.check_and_send_alarm(opr['meter_id'], data['data'], data['data'].get('status'))
            app_meter_api.update_meter_data(opr['meter_id'], data)


class ModBusFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return FlowMeterServer(self)


def query_meter_data():
    """
    定时查询目前所有在线DTU的所有仪表数据
    :return:
    """
    logger.info("开始定时查询流量计数据")
    meters = conf_meter_api.find_meters()
    meter_ids = [meter.id for meter in meters]
    app_meter_api.query_meter_data({"meter_ids": meter_ids}, None, record_log=False)


def run_server(port=8003):
    """
    开始服务器端的运行
    :param port: 服务器连接端口
    :return:
    """

    # 创建5秒定时任务
    five_seconds_tasks = task.LoopingCall(five_seconds_beat_task)
    five_seconds_tasks.start(5)

    # 创建10秒定时任务
    ten_seconds_tasks = task.LoopingCall(ten_seconds_beat_task)
    ten_seconds_tasks.start(10)

    # 创建30分钟定时任务
    query_task = task.LoopingCall(thirty_minutes_beat_task)
    query_task.start(30 * 60)

    endpoint = TCP4ServerEndpoint(reactor, port)
    endpoint.listen(ModBusFactory())
    reactor.run(installSignalHandlers=0)


def clear_timeout_opr():
    # 清除在等待超时的数据帧
    logger.info("开始清除过期操作")
    timeout_time = int(conf_configure_api.get_configure_by_name(conf_configure_api.get_wait_timeout()))
    oprs = conf_opr_api.get_all_timeout_wait_oprs(timeout_time)

    opr_ids = []
    for opr in oprs:
        opr_ids.append(opr.id)
        app_log_api.send_opr_status(opr.id)

    # 更新日志状态为失败
    conf_log_api.update_opr_logs_state(opr_ids, OprLog.ERROR_STATE)
    oprs.delete()

    logger.info("将日志：{}状态设置为失败！".format(opr_ids))


def exec_remote_opr():
    dtu_nos = conf_dtu_api.get_online_dtu_nos()
    for dtu_no in dtu_nos:
        app_opr_api.execute_unexecuted_remote_op(dtu_no)


def send_data_frame(dtu_no, data_frame):
    connect = FlowMeterClients.get_connect(dtu_no)
    # 如果流量计客户端离线，就抛异常
    if connect is None:
        raise OfflineException()

    connect.getHandle().sendall(data_frame)
    logger.info("服务器发送了：{}".format(data_frame))


def five_seconds_beat_task():
    """
    5秒定时任务
    :return:
    """
    try:
        exec_remote_opr()
    except Exception as ex:
        logger.error(str(ex))


def ten_seconds_beat_task():
    """
    10秒定时任务
    :return:
    """
    try:
        clear_timeout_opr()
    except Exception as ex:
        logger.error(str(ex))


def thirty_minutes_beat_task():
    """
    30分钟定时任务
    :return:
    """
    try:
        query_meter_data()
    except Exception as ex:
        logger.error(str(ex))


if __name__ == "__main__":
    t = threading.Thread(target=run_server, args=())
    t.start()
