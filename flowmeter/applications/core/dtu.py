# coding=utf-8

from django.db.models import Q

from flowmeter.common.const import RoleType
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.api import user as conf_user_api
from flowmeter.exceptions import ValueValidException, DoesNotExistException, ParameterErrorException


def get_dtu_filter(manufacturer_id, dtu_user_id):

    filters = Q()
    if manufacturer_id is not None:
        filters &= Q(region__manufacturer__id=manufacturer_id)

    if dtu_user_id is not None:
        filters &= Q(user__id=dtu_user_id)

    return filters


def get_dtu_dict(dtu):

    return {
            "id": dtu.id,
            "user_id": dtu.user.id,
            "user_name": dtu.user.name,
            "user_phone": dtu.user.phone,
            "manufacturer_id": dtu.region.manufacturer.id,
            "manufacturer_name": dtu.region.manufacturer.name,
            "manufacturer_phone": dtu.region.manufacturer.phone,
            "remark": dtu.remark,
            "dtu_no": dtu.dtu_no,
        }


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


def get_dtu_user_by_phone(phone):
    try:
        user = conf_user_api.get_user_by_phone(phone)
        if user.role != RoleType.DTU_USER:
            raise ParameterErrorException("该用户不是DTU用户！")
        return user
    except DoesNotExistException:
        raise DoesNotExistException("该DTU用户不存在！")
