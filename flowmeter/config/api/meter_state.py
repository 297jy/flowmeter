# coding=utf-8

import datetime

from flowmeter.celery_task.api import alarm_task
from flowmeter.common.api.validators import param_check, WhiteListCheck
from flowmeter.config.db.log_table import AlarmLog
from flowmeter.config.db.meter_state_table import MeterState
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.core import meter_state as core
from flowmeter.config.db.meter_table import Meter
from flowmeter.config.const import SENSOR_ERROR_FLAG_TRUE, VALVE_ERROR_FLAG_TRUE, OWE_STATE_TRUE, VALVE_STATE_OPEN


def add_meter_state(state_info):
    must_dict = {
        "meter_id": int,
    }
    param_check(state_info, must_dict)

    state = MeterState.objects.create(**state_info)

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


def update_meter_state(meter_id, state_info):
    optional_dict = {
        "valve_state": WhiteListCheck.check_valve_state,
        "battery_pressure_state": WhiteListCheck.check_battery_pressure_state,
        "sensor_state": WhiteListCheck.check_sensor_state,
        "owe_state": WhiteListCheck.check_owe_state,
        "valve_error_flag": WhiteListCheck.check_valve_error_flag,
        "recharge_state": WhiteListCheck.check_recharge_state,
    }
    param_check(state_info, optional_dict=optional_dict)

    # 检查是否有警报发生
    if state_info.get('sensor_state') == SENSOR_ERROR_FLAG_TRUE:
        log_dict = {'alarm_type': AlarmLog.ALARM_SENSOR_ERROR, 'meter_id': meter_id,
                    'opr_time': datetime.datetime.now()}
        # 异步执行
        alarm_task.send_alarm.delay(log_dict)
    if state_info.get('valve_error_flag') == VALVE_ERROR_FLAG_TRUE:
        log_dict = {'alarm_type': AlarmLog.ALARM_VALVE_ERROR, 'meter_id': meter_id,
                    'opr_time': datetime.datetime.now()}
        # 异步执行
        alarm_task.send_alarm.delay(log_dict)

    if state_info.get('owe_state') == OWE_STATE_TRUE and state_info.get('valve_state') == VALVE_STATE_OPEN:
        log_dict = {'alarm_type': AlarmLog.ALARM_SUB_VALVE, 'meter_id': meter_id,
                    'opr_time': datetime.datetime.now()}
        # 异步执行
        alarm_task.send_alarm.delay(log_dict)

    try:
        state = conf_meter_api.find_meter_state_by_meter_id(meter_id)
        core.update_meter_state(state, state_info)
    except Meter.DoesNotExist:
        pass
