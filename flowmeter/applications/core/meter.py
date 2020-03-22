# coding=utf-8
import datetime

from django.db.models import Q, F

from flowmeter import settings
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
        "remark": meter.remark,
        "state_id": meter.meterstate.id,
    }

    if meter.last_update_time is not None:
        meter_dict['last_update_time'] = meter.last_update_time.strftime(settings.DATETIME_FORMAT_STR)

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
        "valve_address": state.meter.valve.address,
        "valve_dtu": state.meter.valve.dtu.id,
        "version": state.meter.version,
        "temperature": state.meter.temperature
    }
    for key, val in state_dict.items():
        if val == UNKNOWN_VALUE or val == UNKNOWN_STATE:
            state_dict[key] = '未知'

    if state_dict['battery_pressure_state'] == BATTERY_PRESSURE_STATE_NORMAL:
        state_dict['battery_pressure_state'] = '正常'
    else:
        state_dict['battery_pressure_state'] = '异常'

    if state_dict['valve_error_flag'] == VALVE_ERROR_FLAG_FALSE:
        state_dict['valve_error_flag'] = '正常'
    else:
        state_dict['valve_error_flag'] = '异常'

    if state_dict['owe_state'] == OWE_STATE_FALSE:
        state_dict['owe_state'] = '正常'
    else:
        state_dict['owe_state'] = '欠费'

    if state_dict['sensor_state'] == OWE_STATE_FALSE:
        state_dict['sensor_state'] = '正常'
    else:
        state_dict['sensor_state'] = '异常'

    return state_dict


def update_dtu(dtu, dtu_info):
    if 'remark' in dtu_info.keys():
        dtu.remark = dtu_info['remark']
    dtu.save()


def get_valve_info(meter_info):
    """
    提取出阀门信息
    :param meter_info:
    :return:
    """
    valve = {
        'dtu_id': meter_info.pop('valve_dtu_id', None),
        'address': meter_info.pop('valve_address', None),
    }
    if valve['dtu_id'] is None:
        valve['dtu_id'] = meter_info['dtu_id']

    if valve['address'] is None:
        valve['address'] = meter_info['address']

    return valve


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
