# coding=utf-8

from flowmeter.config.api import data_field
from flowmeter.config.api import control_register
from flowmeter.common.api import math

__QUERY_OPE_CODE = 3


def is_query_opr(frame):

    field = data_field.find_opr_code_field()
    opr_code = frame[field.begin_address]
    return opr_code == __QUERY_OPE_CODE


def get_address(frame):
    """
    获取地址
    :param frame:
    :return:
    """
    field = data_field.find_address_field()
    address = frame[field.begin_address]
    return address


def __cal_surplus_gas(frame):
    """
    获取剩余气量
    :param frame:
    :return:
    """
    field = data_field.find_surplus_gas_field()
    if len(frame) <= field.end_address:
        return None
    surplus_gas = math.byte_arr_convert_signed_int(frame[field.begin_address: field.end_address + 1])
    return surplus_gas


def __cal_flow_rate(frame):
    """
    获取瞬时流量
    :param frame:
    :return:
    """
    field = data_field.find_flow_rate_field()
    if len(frame) <= field.end_address:
        return None
    flow_rate = math.calculate_double(frame[field.begin_address: field.end_address + 1])
    return flow_rate


def __cal_total_flow(frame):
    int_field = data_field.find_total_flow_int_field()
    float_field = data_field.find_total_flow_float_field()
    res = None
    if len(frame) > int_field.end_address:
        res = math.byte_arr_convert_int(frame[int_field.begin_address: int_field.end_address + 1])
    if len(frame) > float_field.end_address:
        res += math.calculate_double(frame[float_field.begin_address: float_field.end_address + 1])
    return res


def __get_version(frame):
    field = data_field.find_version_field()
    if len(frame) <= field.end_address:
        return None
    byte = frame[field.begin_address]
    version = (byte / 16) + byte % 16 * 0.1
    return version


def __get_all_state(frame):
    field = data_field.find_meter_state_field()

    if len(frame) <= field.end_address:
        return {}

    sl = frame[field.end_address]
    sh = frame[field.begin_address]
    valve_state = sl & 1
    battery_pressure_state = (sl >> 2) & 1
    sensor_state = (sl >> 6) & 1
    owe_state = (sl >> 7) & 1
    valve_error_flag = (sh >> 1) & 1
    recharge_state = (sh >> 2) & 1

    return {
        "valve_state": valve_state,
        "battery_pressure_state": battery_pressure_state,
        "sensor_state": sensor_state,
        "owe_state": owe_state,
        "valve_error_flag": valve_error_flag,
        "recharge_state": recharge_state,
    }


def __cal_power(frame):
    field = data_field.find_power_field()
    if len(frame) <= field.end_address:
        return None
    power = math.byte_arr_convert_int(frame[field.begin_address: field.end_address + 1])
    return power


def __cal_temperature(frame):
    field = data_field.find_temperature_field()
    if len(frame) <= field.end_address:
        return None
    temperature = math.byte_arr_convert_int(frame[field.begin_address: field.end_address + 1])
    return temperature


def __cal_flow_ratio(frame):
    field = data_field.find_flow_ratio_field()
    if len(frame) <= field.end_address:
        return None
    flow_ratio = math.byte_arr_convert_int(frame[field.begin_address: field.end_address + 1])
    return flow_ratio


# 数据域与其对应的计算函数映射
__field_cal_fun_map = {
    'surplus_gas': __cal_surplus_gas,
    "flow_rate": __cal_flow_rate,
    "total_flow": __cal_total_flow,
    "status": __get_all_state,
    "power": __cal_power,
    "temperature": __cal_temperature,
    "flow_ratio": __cal_flow_ratio,
}


def get_frame_data(frame):
    """
    获得数据帧中的数据
    :param frame:
    :return:
    """
    res = {}
    for field, fun in __field_cal_fun_map:
        res[field] = fun(frame)
    return res


def get_opr_type(frame):
    """
    获取操作类型
    :param frame:
    :return:
    """
    field_val = frame[2] << 8 + frame[3]
    const_data = frame[4] << 8 + frame[5]
    # 先根据域值筛选
    registers = control_register.find_registers_by_field_val(field_val)
    # 如果只筛选到一个操作类型，就直接返回
    if len(registers) == 1:
        return registers[0].opr_type
    # 如果筛选到多个操作类型，就根据固定数据继续筛选
    elif len(registers) > 1:
        for register in registers:
            if register.const_data == const_data:
                return register.opr_type
