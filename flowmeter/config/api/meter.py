# coding=utf-8

import datetime
from flowmeter.config.core import meter as core
from flowmeter.common.api.validators import param_check, StrCheck, WhiteListCheck
from flowmeter.config.api import dtu as conf_dtu_api


def find_opr_logs_by_meter(meter_obj):

    logs = core.find_meter_opr_logs(meter_obj)

    return logs


def find_meter(dtu_no, address):

    dtu_id = conf_dtu_api.find_id_by_dtu_no(dtu_no)
    meter = core.find_one_meter({'dtu_id': dtu_id, 'address': address})

    return meter


def add_meter(meter_info):

    must_dict = {
        "dtu_id": int,
        "address": int,
        "valve_id": int,
    }
    param_check(meter_info, must_dict)

    core.add_meter(meter_info)


def update_meter_data(dtu_no, address, meter_data):

    optional_dict = {
        "dtu_no": int,
        "address": int,
        "last_update_time": datetime.datetime,
        "surplus_gas": float,
        "surplus_gas_limits": float,
        "flow_ratio": float,
        "flow_rate": float,
        "total_flow": float,
        "temperature": float,
        "power": float,
        "version": float,
    }
    param_check(meter_data, optional_dict=optional_dict)

    old_meter = find_meter(dtu_no, address)

    core.update_meter(old_meter, meter_data)


def update_meter_state(dtu_no, address, meter_state):
    """
    更新仪表状态
    :param dtu_no:
    :param address:
    :param meter_state:
    :return:
    """
    must_dict = {
        'valve_state': WhiteListCheck.check_valve_state,
        'recharge_state': WhiteListCheck.check_recharge_state,
        'battery_pressure_state': WhiteListCheck.check_battery_pressure_state,
        'valve_error_flag': WhiteListCheck.check_valve_error_flag,
        'owe_state': WhiteListCheck.check_owe_state,
        'sensor_state': WhiteListCheck.check_sensor_state,
    }
    optional_dict = {
        'online_state': WhiteListCheck.check_online_state,
    }
    param_check(meter_state, must_dict, optional_dict)

    old_meter = find_meter(dtu_no, address)

    core.update_meter_state(old_meter.state, meter_state)