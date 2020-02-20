# coding=utf-8

from flowmeter.modbus.core import frame as core
from flowmeter.config.db.operator_table import Operator


def parse_data_frame(data_frame):
    """
    解析接收到的数据帧
    :param data_frame:
    :return:
    """
    frame = {'address': core.get_address(data_frame)}
    if core.is_query_opr(data_frame):
        frame['opr_type'] = Operator.QUERY
        frame['data'] = core.get_frame_data(data_frame)
    else:
        frame['opr_type'] = core.get_opr_type(data_frame)