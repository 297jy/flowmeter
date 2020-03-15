# coding=utf-8

import datetime
from flowmeter.common.api.validators import param_check, StrCheck, WhiteListCheck
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.meter_state_table import MeterState


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

