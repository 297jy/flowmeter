# coding=utf-8

from flowmeter.config.core import dtu as core
from flowmeter.common.api.validators import param_check, StrCheck
from flowmeter.config.api import cache


def find_dtu_by_no(dtu_no):
    """
    根据dtu编号来查询dtu
    :param dtu_no:
    :return:
    """
    dtu = core.find_one_dtu({'dtu_no': dtu_no})

    return dtu


def add_dtu(dtu_info):
    """
    添加dtu
    :param dtu_info:
    :return:
    """
    must_dict = {
        'protocol_id': int,
        'dtu_no': int,
        'region_id': int,
    }
    optional_dict = {
        'remark': StrCheck.check_remark,
    }
    param_check(dtu_info, must_dict=must_dict, optional_dict=optional_dict)

    core.add_dtu(dtu_info)


def find_meters_by_dtu_no(dtu_no):
    """
    查询dtu_no所有的仪表
    :param dtu_no:
    :return:
    """
    dtu = find_dtu_by_no(dtu_no)
    meters = core.find_dtu_meters(dtu)

    return meters


def find_id_by_dtu_no(dtu_no):

    keyname = 'dtu_no_' + dtu_no
    if cache.is_exists(keyname):
        return cache.get_int(keyname)

    dtu = core.find_one_dtu({'dtu_no': dtu_no})
    cache.set_int(keyname, dtu.id)

    return dtu.id

