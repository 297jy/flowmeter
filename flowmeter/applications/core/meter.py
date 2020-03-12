# coding=utf-8

from django.db.models import Q, F
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.valve_table import Valve
from flowmeter.config.db.operator_table import Operator
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.exceptions import ValueValidException
from flowmeter.config.const import UNKNOWN_STATE, UNKNOWN_VALUE


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
            "last_update_time": meter.last_update_time,
            "remark": meter.remark,
            "state_id": meter.state.id,
        }
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
        "online_state": state.online_state,
        "sensor_state": state.sensor_state,
    }
    for key, val in state_dict.items():
        if val == UNKNOWN_VALUE or val == UNKNOWN_STATE:
            state_dict[key] = ''
    return state_dict


def find_can_use_dtu_no(region):
    """
    查找在该区间上的一个可用dtu_no
    :param region:
    :return:
    """
    if region.used_num == region.right - region.left + 1:
        raise ValueValidException('区间:[{}-{}]，没有可分配的DTU编号，请更换区间！'.format(region.left, region.right))

    dtus = conf_dtu_api.find_dtus(Q(region=region))
    dtu_no = region.left
    for dtu in dtus:
        if dtu_no != dtu.dtu_no:
            break
        dtu_no += 1

    return dtu_no


def update_region_used_num(region):

    region.used_num = conf_dtu_api.get_used_num(region.id)
    region.save()


def update_dtu(dtu, dtu_info):

    if 'remark' in dtu_info.keys():
        dtu.remark = dtu_info['remark']
    dtu.save()


def get_valve_info(dtu_info):

    valve_info = {
        "valve_type": dtu_info['valve_type'],
        "dtu_id": dtu_info['dtu_id'],
    }
    if 'valve_dtu' in dtu_info:
        valve_info['valve_dtu_id'] = dtu_info['valve_dtu']
    if 'address' in dtu_info:
        valve_info['address'] = dtu_info['address']

    return valve_info


def get_dtu_info(dtu_info):

    dtu_dict = {
        "region_id": dtu_info['region_id'],
        "user_id": dtu_info['user_id'],
        "dtu_no": dtu_info['dtu_no'],
    }
    if 'remark' in dtu_info:
        dtu_dict['remark'] = dtu_info['remark']

    return dtu_dict


def get_remote_execute_oprs(meter_info):
    """
    获取需要执行的操作
    :param meter_info:
    :return:
    """
    old_meter = conf_meter_api.find_meter_by_id(meter_info['meter_id'])

    opr_funs = []
    if old_meter.address != meter_info['address']:
        opr_funs.append(Operator.create_set_meter_address_opr)
    if old_meter.flow_ratio != meter_info['flow_ratio']:
        opr_funs.append(Operator.create_set_flow_ratio_opr)

    return opr_funs
