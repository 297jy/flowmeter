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
from flowmeter.exceptions import ValueValidException
from django.db import transaction

import logging

logger = logging.getLogger('log')


class FlowMeterClients:
    """
    流量计DTU客户端与服务器端的连接集合
    """
    def __init__(self):
        self.dtu_to_connect_map = {}
        self.ip_to_dtu_map = {}

    def add(self, dtu_no, ip, connect):
        """
        如果添加的dtu连接不存在，则返回True，否则返回False
        :param dtu_no:
        :param ip:
        :param connect:
        :return:
        """
        if dtu_no not in self.dtu_to_connect_map.keys():
            self.dtu_to_connect_map[dtu_no] = connect
            self.ip_to_dtu_map[ip] = dtu_no
            return True
        return False

    def get_connect(self, dtu_no):
        return self.dtu_to_connect_map[dtu_no]

    def get_dtu_no(self, ip):
        return self.ip_to_dtu_map[ip]

    def remove(self, ip):

        dtu_no = self.get_dtu_no(ip)
        if dtu_no is None:
            return
        del self.ip_to_dtu_map[ip]

        if dtu_no in self.dtu_to_connect_map.keys():
            del self.dtu_to_connect_map[dtu_no]


class FlowMeterServer(Protocol):
    """
    与流量计通信的服务器
    """

    # 心跳包数据帧字节数
    HEART_BEAT_BYTE_NUM = 2
    # 16进制的比特数
    HEX_NUM = 4
    # 正在与服务器端连接的客户端
    clients = FlowMeterClients()

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
            dtu_no = dtu_no + byte << FlowMeterServer.HEX_NUM

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
        FlowMeterServer.clients.remove(ip)

    def dataReceived(self, data_frame):
        """
        数据接收
        :param data_frame
        :return:
        """
        ip = self.transport.getPeer().host
        try:
            # 回应心跳包
            if FlowMeterServer.__is_heart_beat(data_frame):
                # 添加新的客户端连接
                dtu_no = FlowMeterServer.__heart_beat_transfer_dtu_no(data_frame)
                connect = self.transport
                FlowMeterServer.clients.add(dtu_no, ip, connect)

                # 回应心跳包
                self.transport.write(data_frame)
                app_opr_api.execute_unexecuted_remote_op(dtu_no)

            else:
                dtu_no = self.clients.get_dtu_no(ip)
                # 先解析数据帧
                data = frame.parse_data_frame(data_frame)
                with transaction.atomic():
                    # 先执行一条等待结果的操作
                    app_opr_api.execute_wait_remote_op(dtu_no, data['address'], data['opr_type'])
                    # 更新仪表数据
                    app_meter_api.update_meter_data(dtu_no, data)
        except:
            traceback.print_exc()


class ModBusFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return FlowMeterServer(self)


def run_server(port=8081):
    """
    开始服务器端的运行
    :param port: 服务器连接端口
    :return:
    """
    endpoint = TCP4ServerEndpoint(reactor, port)
    endpoint.listen(ModBusFactory())
    reactor.run()


def send_data_frame(dtu_no, data_frame):

    connect = FlowMeterServer.clients.get_connect(dtu_no)
    # 如果流量计客户端离线，就抛异常
    if connect is None:
        raise OfflineException()

    connect.write(data_frame)



