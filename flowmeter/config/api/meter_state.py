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

