# coding=utf-8

from flowmeter.config.api import operator as conf_operator_api
from flowmeter.modbus.api import server
from flowmeter.modbus.api import frame
from flowmeter.config.api import operator as conf_operator_api

import logging

logger = logging.getLogger('log')


def execute_remote_op(opr):
    """
    执行远程操作
    :return:
    """
    data_frame = frame.generate_data_frame(opr.address, opr.opr_type, opr.val)
    # 直接向流量计发送数据帧
    try:
        server.send_data_frame(opr.dtu_no, data_frame)
    except:
        # 发送失败就放进命令队列中
        conf_operator_api.add_operator(opr)
