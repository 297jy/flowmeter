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


def generate_data_frame(address, opr_type, val=None):
    """
    根据操作类型，生成数据帧
    :param opr_type:
    :param val:
    :return:
    """
    __SET_REGISTER_OPR_CODE = 6
    frame = [address, __SET_REGISTER_OPR_CODE, ]
    register = core.get_register_by_opr_type(opr_type)
    field_val_h = register.field_val >> 8
    field_val_l = register.field_val - (field_val_h << 8)
    frame.append(field_val_h)
    frame.append(field_val_l)
    const_data_h = register.const_data >> 8
    const_data_l = register.const_data - const_data_h << 8
    frame.append(const_data_h)
    frame.append(const_data_l)
    # 计算校验码
    crc_h, crc_l = core.cal_crc(frame)
    frame.append(crc_h)
    frame.append(crc_l)
    return frame
