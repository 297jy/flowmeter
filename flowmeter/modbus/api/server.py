# coding=utf-8
import threading
import time
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
            if dtu_no not in FlowMeterClients.dtu_to_connect_map.keys():
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
            dtu_no = dtu_no + (byte << FlowMeterServer.HEX_NUM)

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
        # 更新DTU离线状态
        conf_dtu_api.update_dtu_offline_state(dtu_no)
        FlowMeterClients.remove(ip)
        logger.info("断开连接！")

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
            conf_dtu_api.update_dtu_online_state(dtu_no)

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

    meters = conf_meter_api.find_meters()
    meter_ids = [meter.id for meter in meters]
    app_meter_api.query_meter_data({"meter_ids": meter_ids}, None, record_log=False)


def run_server(port=8003):
    """
    开始服务器端的运行
    :param port: 服务器连接端口
    :return:
    """

    # 创建定时任务，定时循环调用
    exec_remote_task = task.LoopingCall(exec_remote_opr)
    # 开启定时任务，并指定定时任务的时间间隔
    exec_remote_task.start(conf_configure_api.get_unexecuted_opr_check_time())

    """
    query_task = task.LoopingCall(query_meter_data)
    query_task.start(conf_configure_api.get_query_meter_time() * 60)

    clear_task = task.LoopingCall(clear_failed_opr)
    clear_time = int(conf_configure_api.get_configure_by_name(conf_configure_api.get_clear_failed_opr_time_name()))
    clear_task.start(clear_time * 60)
    """
    endpoint = TCP4ServerEndpoint(reactor, port)
    endpoint.listen(ModBusFactory())
    reactor.run(installSignalHandlers=0)

"""
def clear_failed_opr():
    # 清除失败的远程操作
    dtu_nos = conf_dtu_api.get_all_dtu_no()
    now_time = time.time()
    for dtu_no in dtu_nos:
        oprs_dict = conf_opr_api.get_all_unexecuted_opr(dtu_no)
        for meter_address, opr_type_dict in oprs_dict.items():
            for opr_type, oprs in opr_type_dict.items():
                new_oprs = []
                failed_log_ids = []
                for opr in oprs:
                    # 删除掉已经超过两小时但是未执行成功的操作
                    if (now_time - opr['opr_time']) <= 7200:
                        new_oprs.append(opr)
                    else:
                        failed_log_ids.append(opr['log_id'])
                conf_opr_api.set_unexecuted_operator(dtu_no, meter_address, opr_type, new_oprs)
                conf_log_api.update_opr_logs_state(failed_log_ids, OprLog.ERROR_STATE)

        oprs_dict = conf_opr_api.get_all_wait_opr(dtu_no)
        for meter_address, opr_type_dict in oprs_dict.items():
            for opr_type, oprs in opr_type_dict.items():
                new_oprs = []
                failed_log_ids = []
                for opr in oprs:
                    # 删除掉已经超过两小时但是未执行成功的操作
                    if (now_time - opr['opr_time']) <= 7200:
                        new_oprs.append(opr)
                    else:
                        failed_log_ids.append(opr['log_id'])
                conf_opr_api.set_wait_operator(dtu_no, meter_address, opr_type, new_oprs)
                conf_log_api.update_opr_logs_state(failed_log_ids, OprLog.ERROR_STATE)
"""


def exec_remote_opr():
    dtu_nos = conf_dtu_api.get_online_dtu_nos()
    for dtu_no in dtu_nos:
        try:
            app_opr_api.execute_unexecuted_remote_op(dtu_no)
        except Exception as ex:
            logger.error(str(ex))


def send_data_frame(dtu_no, data_frame):
    connect = FlowMeterClients.get_connect(dtu_no)
    # 如果流量计客户端离线，就抛异常
    if connect is None:
        raise OfflineException()

    connect.getHandle().sendall(data_frame)


if __name__ == "__main__":
    t = threading.Thread(target=run_server, args=())
    t.start()
