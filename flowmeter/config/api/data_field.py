# coding=utf-8

from flowmeter.config.core import data_field as core
from flowmeter.common.api.validators import param_check, StrCheck
from flowmeter.config.api import cache
from flowmeter.config.db.data_field_table import DataField
from django.db import transaction


def find_data_fields():

    fields = core.find_data_fields({})

    return fields


def update_data_field(field_info):

    must_dict = {
        'id': int,
        'begin_address': int,
        'end_address': int,
    }
    param_check(field_info, must_dict, extra=True)

    # 保证原子性
    with transaction.atomic():
        core.update_data_field(field_info)
        # 直接删除所有关于数据域的缓存
        cache.delete('field_*')


def find_opr_code_field():
    """
    查找操作码数据域
    :return:
    """
    key_name = 'field_opr_code'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'opr_code'})
    cache.set_obj(key_name, field)

    return field


def find_address_field():
    """
    查找地址数据域
    :return:
    """
    key_name = 'field_address'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'address'})
    cache.set_obj(key_name, field)

    return field


def find_surplus_gas_field():

    key_name = 'field_surplus_gas'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'surplus_gas'})
    cache.set_obj(key_name, field)

    return field


def find_flow_rate_field():

    key_name = 'field_flow_rate'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'flow_rate'})
    cache.set_obj(key_name, field)

    return field


def find_total_flow_field():

    key_name = 'field_total_flow'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'total_flow'})
    cache.set_obj(key_name, field)

    return field


def find_total_flow_int_field():

    key_name = 'field_flow_total_int'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'flow_total_int'})
    cache.set_obj(key_name, field)

    return field


def find_total_flow_float_field():

    key_name = 'field_flow_total_float'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'flow_total_float'})
    cache.set_obj(key_name, field)

    return field


def find_version_field():

    key_name = 'field_version'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'version'})
    cache.set_obj(key_name, field)

    return field


def find_meter_state_field():

    key_name = 'field_meter_state'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'meter_state'})
    cache.set_obj(key_name, field)

    return field


def find_power_field():

    key_name = 'field_power'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'power'})
    cache.set_obj(key_name, field)

    return field


def find_temperature_field():

    key_name = 'field_temperature'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'temperature'})
    cache.set_obj(key_name, field)

    return field


def find_flow_ratio_field():

    key_name = 'field_flow_ratio'
    if cache.is_exists(key_name):
        return cache.get_obj(key_name, DataField)

    field = core.find_one_data_field({'field_name': 'flow_ratio'})
    cache.set_obj(key_name, field)

    return field
