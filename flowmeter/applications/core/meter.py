# coding=utf-8

from django.db.models import Q, F
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.valve_table import Valve
from flowmeter.config.db.operator_table import Operator
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.api import log as conf_log_api
from flowmeter.config.api import meter_state as conf_state_api
from flowmeter.exceptions import ValueValidException
from flowmeter.config.const import UNKNOWN_STATE, UNKNOWN_VALUE, VALVE_STATE_OPEN, VALVE_STATE_CLOSE, \
    RECHARGE_STATE_OPEN, RECHARGE_STATE_CLOSE, BATTERY_PRESSURE_STATE_NORMAL, VALVE_ERROR_FLAG_FALSE, OWE_STATE_FALSE, \
    SENSOR_ERROR_FLAG_FALSE


def get_meter_filters(manufacturer_id, dtu_user_id, dtu_id):
    filters = Q()
    if manufacturer_id is not None:
        filters &= Q(dtu__region__manufacturer__id=manufacturer_id)
    if dtu_id is not None:
        filters &= Q(dtu__id=dtu_id)
    if dtu_user_id is not None:
        filters &= Q(dtu__user__id=dtu_user_id)

    return filters


def get_meter_dict(meter):
    meter_dict = {
        "id": meter.id,
        "user_id": meter.dtu.user.id,
        "user_name": meter.dtu.user.name,
        "manufacturer_name": meter.dtu.region.manufacturer.name,
        "dtu_no": meter.dtu.dtu_no,
        "address": meter.address,
        "surplus_gas": meter.surplus_gas,
        "total_flow": meter.total_flow,
        "surplus_gas_limits": meter.surplus_gas_limits,
        "flow_rate": meter.flow_rate,
        "flow_ratio": meter.flow_ratio,
        "power": meter.power,
        "temperature": meter.temperature,
        "version": meter.version,
        "last_update_time": meter.last_update_time,
        "remark": meter.remark,
        "state_id": meter.state.id,
    }
    for key, val in meter_dict.items():
        if val == UNKNOWN_VALUE or val == UNKNOWN_STATE:
            meter_dict[key] = '未知'

    return meter_dict


def get_meter_state_dict(state):

    state_dict = {
        "valve_state": state.valve_state,
        "recharge_state": state.recharge_state,
        "battery_pressure_state": state.battery_pressure_state,
        "valve_error_flag": state.valve_error_flag,
        "owe_state": state.owe_state,
        "sensor_state": state.sensor_state,
    }
    for key, val in state_dict.items():
        if val == UNKNOWN_VALUE or val == UNKNOWN_STATE:
            state_dict[key] = '未知'
        elif key == "valve_state":
            if val == VALVE_STATE_OPEN:
                state_dict[key] = '开启'
            else:
                state_dict[key] = '关闭'
        elif key == "recharge_state":
            if val == RECHARGE_STATE_OPEN:
                state_dict[key] = '开启'
            else:
                state_dict[key] = '关闭'
        elif key == "battery_pressure_state":
            if val == BATTERY_PRESSURE_STATE_NORMAL:
                state_dict[key] = '正常'
            else:
                state_dict[key] = '欠压'
        elif key == "valve_error_flag":
            if val == VALVE_ERROR_FLAG_FALSE:
                state_dict[key] = '正常'
            else:
                state_dict[key] = '异常'
        elif key == "owe_state":
            if val == OWE_STATE_FALSE:
                state_dict[key] = '正常'
            else:
                state_dict[key] = '欠费'

        elif key == "sensor_state":
            if val == SENSOR_ERROR_FLAG_FALSE:
                state_dict[key] = '正常'
            else:
                state_dict[key] = '异常'

    return state_dict


def update_dtu(dtu, dtu_info):
    if 'remark' in dtu_info.keys():
        dtu.remark = dtu_info['remark']
    dtu.save()


def get_valve_info(dtu_info):
    valve_info = {
        "valve_type": dtu_info['valve_type'],
        "dtu_id": dtu_info['dtu_id'],
    }
    if 'valve_dtu' in dtu_info:
        valve_info['valve_dtu_id'] = dtu_info['valve_dtu']
    if 'address' in dtu_info:
        valve_info['address'] = dtu_info['address']

    return valve_info


def get_dtu_info(dtu_info):
    dtu_dict = {
        "region_id": dtu_info['region_id'],
        "user_id": dtu_info['user_id'],
        "dtu_no": dtu_info['dtu_no'],
    }
    if 'remark' in dtu_info:
        dtu_dict['remark'] = dtu_info['remark']

    return dtu_dict


def create_opr_log(opr_info):
    """
    根据操作，创建对应的操作日志
    :return:
    """
    log = conf_log_api.add_opr_log(opr_info)

    return log