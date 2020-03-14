# coding=utf-8

from flowmeter.applications.core import meter as core
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.api import meter_state as conf_state_api
from flowmeter.config.api import operator as conf_opr_api
from flowmeter.common.api.validators import param_check
from flowmeter.common.api.validators import StrCheck, WhiteListCheck
from django.db import transaction
from flowmeter.common.api import request as request_api


def find_meter_by_query_terms(query_terms, page=None):
    """
    查找仪表
    """

    optional_dict = {
        "manufacturer_id": int,
        "dtu_id": int,
        "dtu_user_id": int,
    }

    param_check(query_terms, optional_dict=optional_dict)

    filters = core.get_meter_filters(query_terms.get('manufacturer_id'), query_terms.get('dtu_user_id'),
                                     query_terms.get('dtu_id'))

    meters = conf_meter_api.find_meters(filters, page)

    meter_dicts = []
    for meter in meters:
        meter_dicts.append(core.get_meter_dict(meter))

    return meter_dicts


def find_meter_state_by_id(state_id):

    state = conf_state_api.find_meter_state_by_id(state_id)
    return core.get_meter_state_dict(state)


def add_meter(meter_info):
    """
    添加一个meter
    :return:
    """
    must_dict = {
        "dtu_id": int,
        "address": int,
        "surplus_gas_limits": float,
    }
    optional_dict = {
        "remark": StrCheck.check_remark,
    }
    param_check(meter_info, must_dict, optional_dict)

    # 保证原子性
    with transaction.atomic():
        state = conf_state_api.add_meter_state()
        meter_info['state_id'] = state.id
        conf_meter_api.add_meter(meter_info)


def del_batch_meter(meter_ids, state_ids):
    """
    :return:
    """

    # 保证原子性
    with transaction.atomic():

        conf_meter_api.del_batch_meter(meter_ids)
        conf_state_api.del_batch_meter_state(state_ids)


def update_meter(meter_info, user):
    """
    更新仪表信息
    :param user: 当前登录的用户
    :param meter_info:
    :return:
    """
    must_dict = {
        "id": int,
        "address": int,
        "surplus_gas_limits": float,
        "flow_ratio": float,
    }
    param_check(meter_info, must_dict)

    dtu_no = conf_meter_api.find_dtu_no_by_meter_id(meter_info['id'])

    # 保证原子性
    with transaction.atomic():
        # 获取需要远程执行的命令
        oprs = core.get_remote_execute_oprs(user['id'], dtu_no, meter_info)

        # 将操作添加到缓存中
        for opr in oprs:
            conf_opr_api.add_operator(opr)

        # 更新不需要远程操作的仪表信息
        conf_meter_api.update_meter_info({"id": meter_info['id'],
                                          "surplus_gas_limits": meter_info['surplus_gas_limits']})


def update_meter_state(meter_state_info, user):
    """
    更新仪表信息
    :param user: 当前登录的用户
    :param meter_state_info:
    :return:
    """
    must_dict = {
        "id": int,
        "meter_id": int,
    }
    optional_dict = {
        "valve_state": int,
        "recharge_state": int,
    }
    param_check(meter_state_info, must_dict, optional_dict)

    dtu_no = conf_meter_api.find_dtu_no_by_meter_id(meter_state_info['meter_id'])

    # 保证原子性
    with transaction.atomic():
        # 获取需要远程执行的命令
        oprs = core.get_remote_execute_oprs(user['id'], dtu_no, meter_state_info=meter_state_info)

        # 将操作添加到缓存中
        for opr in oprs:
            conf_opr_api.add_operator(opr)





