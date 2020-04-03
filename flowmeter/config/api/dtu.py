# coding=utf-8

from flowmeter.config.core import dtu as core
from flowmeter.common.api.validators import param_check, StrCheck
from flowmeter.config.api import cache
from flowmeter.config.db.dtu_table import Dtu
from flowmeter.modbus.api import server
from flowmeter.config.api import cache as conf_cache_api
from flowmeter.config.const import STATE_ONLINE, STATE_OFFLINE


def find_dtu_by_no(dtu_no):
    """
    根据dtu编号来查询dtu
    :param dtu_no:
    :return:
    """
    dtu = core.find_one_dtu({'dtu_no': dtu_no})

    return dtu


def find_dtu_by_id(dtu_id):

    dtu = core.find_one_dtu({'id': dtu_id})

    return dtu


def add_dtu(dtu_info):
    """
    添加dtu
    :param dtu_info:
    :return:
    """
    must_dict = {
        'dtu_no': int,
        'region_id': int,
        'user_id': int,
    }
    optional_dict = {
        'remark': StrCheck.check_remark,
    }
    param_check(dtu_info, must_dict=must_dict, optional_dict=optional_dict)

    return core.add_dtu(dtu_info)


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

    keyname = 'dtu_no_' + str(dtu_no)
    if cache.is_exists(keyname):
        return cache.get_int(keyname)

    dtu = core.find_one_dtu({'dtu_no': dtu_no})
    cache.set_int(keyname, dtu.id)

    return dtu.id


def del_batch_dtu(dtu_ids):
    """
    :return:
    """

    core.del_batch_dtu(dtu_ids)


def find_dtus(filters=None, page=None):

    if page is None:
        if filters:
            dtus = Dtu.objects.select_related('user', 'region').filter(filters).order_by('dtu_no')
        else:
            dtus = Dtu.objects.select_related('user', 'region').all().order_by('dtu_no')
    else:
        start_index = page.limit * (page.index - 1)
        end_index = page.index * page.limit
        if filters:
            dtus = Dtu.objects.filter(filters)[start_index: end_index]
        else:
            dtus = Dtu.objects.all()[start_index: end_index]

    return dtus


def get_used_num(region_id):
    res = Dtu.objects.filter(region_id=region_id).count()

    return res


def get_dtu_online_state(dtu_no):
    """
    获取DTU的在线状态
    :param dtu_no:
    :return:
    """
    return STATE_ONLINE if server.is_dtu_online(dtu_no) else STATE_OFFLINE


def find_dtus_of_select_box_by_man_id(man_id):
    dtus = Dtu.objects.filter(region__manufacturer__id=man_id).values('id', 'dtu_no', 'remark')
    dtu_infos = [dict(dtu) for dtu in dtus]
    return dtu_infos


def find_dtus_of_select_box_by_user_id(user_id):
    dtus = Dtu.objects.filter(user__id=user_id).values('id', 'dtu_no', 'remark')
    dtu_infos = [dict(dtu) for dtu in dtus]
    return dtu_infos


def find_all_dtus_of_select():
    dtus = Dtu.objects.all().values('id', 'dtu_no', 'remark')
    dtu_infos = [dict(dtu) for dtu in dtus]
    return dtu_infos


