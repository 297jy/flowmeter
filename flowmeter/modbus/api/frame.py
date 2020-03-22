# coding=utf-8

from flowmeter.modbus.core import frame as core
from flowmeter.config.db.operator_table import Operator


def parse_data_frame(data_frame):
    """
    解析接收到的数据帧
    :param data_frame:
    :return:
    """
    core.check_crc(data_frame)
    data = {'address': core.get_address(data_frame)}
    if core.is_query_opr(data_frame):
        data['opr_type'] = Operator.QUERY
        data['data'] = core.get_frame_data(data_frame)
    else:
        data['opr_type'] = core.get_opr_type(data_frame)
        data['data'] = core.get_field_val(data_frame, data['opr_type'])

    return data


def generate_data_frame(address, opr_type, val=None):
    """
    根据操作类型，生成数据帧
    :param address:
    :param opr_type:
    :param val:
    :return:
    """
    __SET_REGISTER_OPR_CODE = 6
    __QUERY_OPR_CODE = 3
    frame = [int(address)]
    if opr_type == Operator.QUERY:
        frame.append(__QUERY_OPR_CODE)
    else:
        frame.append(__SET_REGISTER_OPR_CODE)
    register = core.get_register_by_opr_type(opr_type)
    field_val_h = register.field_val >> 8
    field_val_l = register.field_val - (field_val_h << 8)
    frame.append(field_val_h)
    frame.append(field_val_l)

    # 如果有值就使用用户提供的值
    if val is not None:
        data_h = val >> 8
        data_l = val - (data_h << 8)
    else:
        data_h = register.const_data >> 8
        data_l = register.const_data - (data_h << 8)
    frame.append(data_h)
    frame.append(data_l)

    # 计算校验码
    crc_h, crc_l = core.cal_crc(frame)
    frame.append(crc_l)
    frame.append(crc_h)

    return bytes(frame)
