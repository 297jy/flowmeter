# coding=utf-8

import datetime

from django.db.models import F

from flowmeter.config.core import meter as core
from flowmeter.common.api.validators import param_check, StrCheck, WhiteListCheck
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.meter_table import Meter
from flowmeter.config.db.meter_state_table import MeterState


def find_opr_logs_by_meter(meter_obj):
    logs = core.find_meter_opr_logs(meter_obj)

    return logs


def find_meter(dtu_no, address):
    dtu_id = conf_dtu_api.find_id_by_dtu_no(dtu_no)
    meter = core.find_one_meter({'dtu_id': dtu_id, 'address': address})

    return meter


def get_meter_surplus_gas_limits(meter_id):
    """
    获取仪表的剩余气量限值
    :param meter_id:
    :return:
    """
    meter = Meter.objects.values('surplus_gas_limits').get(id=meter_id)
    return meter['surplus_gas_limits']


def find_meter_state(dtu_no, address):

    meter = Meter.objects.get(dtu__dtu_no=dtu_no, address=address)
    return meter.meterstate


def find_meter_state_by_meter_id(meter_id):

    state = MeterState.objects.get(meter__id=meter_id)
    return state


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


def find_infos_by_meter_ids(meter_ids):
    """
    获得仪表对应的dtu和物理地址
    :param meter_ids:
    :return:
    """
    meters = Meter.objects.select_related('dtu__dtu_no').values('id', 'dtu__dtu_no', 'address').filter(id__in=meter_ids)
    info_dicts = []
    for meter in meters:
        info_dicts.append({'dtu_no': meter['dtu__dtu_no'], 'address': meter['address'], 'meter_id': meter['id']})
    return info_dicts


def find_meters(filters=None, page=None):
    if page is None:
        if filters:
            meters = Meter.objects.filter(filters).order_by('dtu__dtu_no', 'address')
        else:
            meters = Meter.objects.all().order_by('dtu__dtu_no', 'address')
        num = len(meters)
    else:
        start_index = page.limit * (page.index - 1)
        end_index = page.index * page.limit
        if filters:
            num = Meter.objects.filter(filters).count()
            meters = Meter.objects.filter(filters).order_by('dtu__dtu_no', 'address')[start_index: end_index]
        else:
            num = Meter.objects.all().count()
            meters = Meter.objects.all().order_by('dtu__dtu_no', 'address')[start_index: end_index]

    return meters, num


def add_meter(meter_info):
    must_dict = {
        "dtu_id": int,
        "address": int,
        "surplus_gas_limits": float,
    }
    optional_dict = {
        "remark": StrCheck.check_remark,
    }
    param_check(meter_info, must_dict, optional_dict)

    return core.add_meter(meter_info)


def update_meter_data(meter_id, meter_data):
    optional_dict = {
        "address": int,
        "last_update_time": datetime.datetime,
        "surplus_gas": int,
        "flow_ratio": float,
        "flow_rate": float,
        "total_flow": float,
        "temperature": float,
        "power": int,
        "version": float,
    }
    param_check(meter_data, optional_dict=optional_dict)

    old_meter = find_meter_by_id(meter_id)

    core.update_meter(old_meter, meter_data)


def add_meter_surplus_gas(dtu_no, address, num):
    """
    给仪表充值
    :param dtu_no:
    :param address:
    :param num:
    :return:
    """
    old_meter = find_meter(dtu_no, address)
    old_meter.surplus_gas = F(old_meter.surplus_gas) + num
    old_meter.last_update_time = datetime.datetime.now()
    old_meter.save()


def update_meter_info(meter_info):
    must_dict = {
        "id": int,
    }
    optional_dict = {
        "surplus_gas_limits": float,
        "remark": StrCheck.check_remark,
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


def get_valve_dtu_and_address(meter_id):

    meter = Meter.objects.values('valve__dtu__dtu_no', 'valve__address').get(id=meter_id)
    return meter['valve__dtu__dtu_no'], meter['valve__address']


def get_total_meter_num_by_man_id(man_id):
    num = Meter.objects.filter(dtu__region__manufacturer__id=man_id).count()
    return num


def get_total_meter_num_by_dtu_user_id(dtu_user_id):
    num = Meter.objects.filter(dtu__user__id=dtu_user_id).count()
    return num


def get_all_meters():
    return Meter.objects.all()
