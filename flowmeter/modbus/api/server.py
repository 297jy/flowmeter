# coding=utf-8

import traceback

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from flowmeter.exceptions import OfflineException
from flowmeter.modbus.api import frame
from flowmeter.applications.api import operator as app_opr_api
from flowmeter.applications.api import meter as app_meter_api
from flowmeter.config.api import cache as conf_cache_api
from twisted.internet import task
from flowmeter.config.api import configure as conf_configure_api
from flowmeter.exceptions import ValueValidException
from django.db import transaction
from flowmeter.config.api import meter as conf_meter_api

import logging

logger = logging.getLogger('log')


class FlowMeterClients:
    """
    流量计DTU客户端与服务器端的连接集合
    """

    dtu_to_connect_map = {}
    ip_to_dtu_map = {}

    @staticmethod
    def add(dtu_no, ip, connect):
        """
        如果添加的dtu连接不存在，则返回True，否则返回False
        :param dtu_no:
        :param ip:
        :param connect:
        :return:
        """
        if dtu_no not in FlowMeterClients.dtu_to_connect_map.keys():
            FlowMeterClients.dtu_to_connect_map[dtu_no] = connect
            FlowMeterClients.ip_to_dtu_map[ip] = dtu_no
            return True
        return False

    @staticmethod
    def get_connect(dtu_no):
        return FlowMeterClients.dtu_to_connect_map.get(dtu_no)

    @staticmethod
    def get_online_dtu_no_list():
        return FlowMeterClients.dtu_to_connect_map.keys()

    @staticmethod
    def get_dtu_no(ip):
        return FlowMeterClients.ip_to_dtu_map[ip] if ip in FlowMeterClients.ip_to_dtu_map.keys() else None

    @staticmethod
    def remove(ip):

        dtu_no = FlowMeterClients.get_dtu_no(ip)
        if dtu_no is None:
            return
        del FlowMeterClients.ip_to_dtu_map[ip]

        if dtu_no in FlowMeterClients.dtu_to_connect_map.keys():
            del FlowMeterClients.dtu_to_connect_map[dtu_no]


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

        try:
            # 回应心跳包
            if FlowMeterServer.__is_heart_beat(data_frame):
                # 添加新的客户端连接
                dtu_no = FlowMeterServer.__heart_beat_transfer_dtu_no(data_frame)
                connect = self.transport
                FlowMeterClients.add(dtu_no, ip, connect)
                # 回应心跳包
                self.transport.getHandle().sendall(data_frame)

            else:
                dtu_no = FlowMeterClients.get_dtu_no(ip)
                # 先解析数据帧
                data = frame.parse_data_frame(data_frame)

                with transaction.atomic():
                    # 先执行一条等待结果的操作
                    opr = app_opr_api.execute_wait_remote_op(dtu_no, data['address'], data['opr_type'], data['data'])

                    # 更新仪表数据
                    if opr is not None:
                        app_meter_api.update_meter_data(opr['meter_id'], data)
        except:
            traceback.print_exc()


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
    for meter in meters:
        app_meter_api.query_meter_data({'id': meter.id, 'address': meter.address, 'dtu_no': meter.dtu.dtu_no}, None,
                                       record_log=False)


def run_server(port=8081):
    """
    开始服务器端的运行
    :param port: 服务器连接端口
    :return:
    """

    # 创建定时任务，定时循环调用
    exec_remote_task = task.LoopingCall(exec_remote_opr)
    # 开启定时任务，并指定定时任务的时间间隔
    exec_remote_task.start(int(conf_configure_api.get_unexecuted_opr_check_time()))

    query_task = task.LoopingCall(query_meter_data)
    query_task.start(10)

    endpoint = TCP4ServerEndpoint(reactor, port)
    endpoint.listen(ModBusFactory())
    reactor.run(installSignalHandlers=0)


def exec_remote_opr():
    dtu_nos = FlowMeterClients.get_online_dtu_no_list()
    for dtu_no in dtu_nos:
        app_opr_api.execute_unexecuted_remote_op(dtu_no)


def send_data_frame(dtu_no, data_frame):
    connect = FlowMeterClients.get_connect(dtu_no)
    # 如果流量计客户端离线，就抛异常
    if connect is None:
        raise OfflineException()

    connect.getHandle().sendall(data_frame)


def is_dtu_online(dtu_no):
    """
    判断DTU是否在线
    :param dtu_no:
    :return:
    """
    return dtu_no in FlowMeterClients.get_online_dtu_no_list()


if __name__ == "__main__":
    run_server()
