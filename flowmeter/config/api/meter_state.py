# coding=utf-8

import datetime
from flowmeter.config.core import meter as core
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

