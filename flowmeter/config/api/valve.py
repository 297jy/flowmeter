# coding=utf-8

from flowmeter.common.api.validators import param_check
from flowmeter.config.db.valve_table import Valve


def add_valve(valve_info):

    must_dict = {
        'valve_type': str,
        'dtu_id': int,
    }
    optional_dict = {
        'address': int,
        'valve_dtu_id': int,
    }
    param_check(valve_info, must_dict, optional_dict)

    valve = Valve.objects.create(**valve_info)

    return valve
