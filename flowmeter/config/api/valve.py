# coding=utf-8
from django.db import IntegrityError

from flowmeter.common.api.validators import param_check
from flowmeter.config.db.valve_table import Valve
from flowmeter.exceptions import ValueDuplicateException


def add_valve(valve_info):

    must_dict = {
        'meter_id': int,
        'dtu_id': int,
    }
    optional_dict = {
        'address': int,
        'valve_dtu_id': int,
    }
    param_check(valve_info, must_dict, optional_dict)
    try:
        valve = Valve.objects.create(**valve_info)
        return valve
    except IntegrityError:
        raise ValueDuplicateException("该仪表已存在！")


def del_batch_valve(valve_ids):
    """
    :return:
    """

    Valve.objects.filter(id__in=valve_ids).delete()


def update_valve(valve_info):
    """
    更新阀门控制器
    :return:
    """
    must_dict = {
        'id': int,
    }
    optional_dict = {
        'dtu_id': int,
        'address': int,
    }
    param_check(valve_info, must_dict, optional_dict)

    valve = Valve.objects.get(id=valve_info['id'])
    # 更新阀门
    for att, val in valve_info.items():
        if getattr(valve, att) != val:
            setattr(valve, att, val)
    valve.save()
