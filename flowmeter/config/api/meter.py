# coding=utf-8

import datetime
from flowmeter.config.core import meter as core
from flowmeter.common.api.validators import param_check, StrCheck, WhiteListCheck
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.meter_table import Meter


def find_opr_logs_by_meter(meter_obj):
    logs = core.find_meter_opr_logs(meter_obj)

    return logs


def find_meter(dtu_no, address):
    dtu_id = conf_dtu_api.find_id_by_dtu_no(dtu_no)
    meter = core.find_one_meter({'dtu_id': dtu_id, 'address': address})

    return meter


def find_meter_by_id(meter_id):

    meter = core.find_one_meter({'id': meter_id})

    return meter


def find_dtu_no_by_meter_id(meter_id):

    meter = Meter.objects.select_related('dtu__dtu_no').values('dtu__dtu_no').get(id=meter_id)
    dtu_no = meter['dtu__dtu_no']
    return dtu_no


def find_dtu_nos_by_meter_ids(meter_ids):
    meters = Meter.objects.select_related('dtu__dtu_no').values('dtu__dtu_no').filter(id__in=meter_ids)
    dtu_nos = []
    for meter in meters:
        dtu_nos.append(meter['dtu__dtu_no'])
    return dtu_nos


def find_meters(filters=None, page=None):
    if page is None:
        if filters:
            meters = Meter.objects.filter(filters).order_by('dtu__dtu_no')
        else:
            meters = Meter.objects.all().order_by('dtu__dtu_no')
    else:
        start_index = page.limit * (page.index - 1)
        end_index = page.index * page.limit
        if filters:
            meters = Meter.objects.filter(filters).order_by('dtu__dtu_no')[start_index: end_index]
        else:
            meters = Meter.objects.all().order_by('dtu__dtu_no')[start_index: end_index]

    return meters


def add_meter(meter_info):
    must_dict = {
        "dtu_id": int,
        "address": int,
        "surplus_gas_limits": float,
        "state_id": int,
    }
    optional_dict = {
        "remark": StrCheck.check_remark,
    }
    param_check(meter_info, must_dict, optional_dict)

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


def update_meter_info(meter_info):
    must_dict = {
        "id": int,
    }
    optional_dict = {
        "surplus_gas_limits": float,
    }
    param_check(meter_info, must_dict, optional_dict)

    old_meter = find_meter_by_id(meter_info['id'])
    core.update_meter(old_meter, meter_info)


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


def del_batch_meter(meter_ids):
    """
    :return:
    """

    core.del_batch_meter(meter_ids)


def get_meter_flow_ratio(meter_id):

    Meter.objects.values('flow_ratio').get(id=meter_id)
