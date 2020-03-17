# coding=utf-8

import datetime
from flowmeter.common.api.validators import param_check, StrCheck, WhiteListCheck
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.meter_state_table import MeterState
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.core import meter_state as core


def add_meter_state():

    state = MeterState()
    state.save()

    return state


def find_meter_state_by_id(state_id):

    state = MeterState.objects.get(id=state_id)

    return state


def del_batch_meter_state(state_ids):
    """
    :return:
    """

    MeterState.objects.filter(id__in=state_ids).delete()


def get_valve_state(meter_state_id):
    """
    获取阀门状态
    :param meter_state_id:
    :return:
    """
    state = MeterState.objects.values('valve_state').get(id=meter_state_id)
    valve_state = state['valve_state']
    return valve_state


def get_recharge_state(meter_state_id):
    """
    获取充值状态
    :param meter_state_id:
    :return:
    """
    state = MeterState.objects.values('recharge_state').get(id=meter_state_id)
    recharge_state = state['recharge_state']
    return recharge_state


def get_dtu_no_by_state_id(state_id):
    """
    获取仪表状态对应的DTU
    :param state_id:
    :return:
    """
    state = MeterState.objects.values('meter__dtu__dtu_no').get(id=state_id)
    return state['meter__dtu__dtu_no']


def update_meter_state(dtu_no, address, state_info):
    optional_dict = {
        "valve_state": WhiteListCheck.check_valve_state,
        "battery_pressure_state": WhiteListCheck.check_battery_pressure_state,
        "sensor_state": WhiteListCheck.check_sensor_state,
        "owe_state": WhiteListCheck.check_owe_state,
        "valve_error_flag": WhiteListCheck.check_valve_error_flag,
        "recharge_state": WhiteListCheck.check_recharge_state,
    }
    param_check(state_info, optional_dict=optional_dict)

    state = conf_meter_api.find_meter_state(dtu_no, address)
    core.update_meter_state(state, state_info)
