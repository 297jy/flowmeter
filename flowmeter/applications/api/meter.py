# coding=utf-8

import datetime

from django.db.models import F

from flowmeter.applications.core import meter as core
from flowmeter.applications.api import operator as app_opr_api
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.api import meter_state as conf_state_api
from flowmeter.config.api import operator as conf_opr_api
from flowmeter.config.api import log as conf_log_api
from flowmeter.common.api.validators import param_check
from flowmeter.common.api.validators import StrCheck, WhiteListCheck
from flowmeter.config.db.operator_table import Operator
from flowmeter.config.const import VALVE_STATE_OPEN, VALVE_STATE_CLOSE, RECHARGE_STATE_OPEN, RECHARGE_STATE_CLOSE, \
    STATE_ONLINE
from django.db import transaction
from flowmeter.applications.api import log as app_log_api


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

    dtu_no = conf_state_api.get_dtu_no_by_state_id(state_id)
    state = conf_state_api.find_meter_state_by_id(state_id)
    state = core.get_meter_state_dict(state)
    state['online_state'] = "在线" if conf_dtu_api.get_dtu_online_state(dtu_no) == STATE_ONLINE else "离线"
    return state


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

    dtu_nos = conf_meter_api.find_dtu_nos_by_meter_ids(meter_ids)
    # 保证原子性
    with transaction.atomic():
        conf_meter_api.del_batch_meter(meter_ids)
        conf_state_api.del_batch_meter_state(state_ids)
        # 清空操作队列
        for dtu_no in dtu_nos:
            conf_opr_api.clear_all_dtu_operator(dtu_no)


def update_meter(meter_info):
    """
    更新仪表信息
    :param meter_info:
    :return:
    """
    must_dict = {
        "id": int,
        "address": int,
        "dtu_no": int,
        "surplus_gas_limits": float,
    }
    param_check(meter_info, must_dict)

    # 保证原子性
    with transaction.atomic():
        # 更新不需要远程操作的仪表信息
        conf_meter_api.update_meter_info({"id": meter_info['id'],
                                          "surplus_gas_limits": meter_info['surplus_gas_limits']})


def update_valve_state(meter_state_info, user):
    """
    更改阀门状态
    :param user: 当前登录的用户
    :param meter_state_info:
    :return:
    """
    must_dict = {
        "id": int,
        "meter_id": int,
        "address": int,
        "valve_state": int,
        "dtu_no": int,
    }
    param_check(meter_state_info, must_dict, )

    dtu_no = meter_state_info['dtu_no']

    # 保证原子性
    with transaction.atomic():
        log_dict = {
            "opr_user_id": user['id'],
            "meter_id": meter_state_info['meter_id'],
        }
        if meter_state_info['valve_state'] == VALVE_STATE_OPEN:
            log_dict['opr_type'] = Operator.OPEN_VALVE
            log = conf_log_api.add_opr_log(log_dict)
            opr = Operator.create_open_valve_opr(user['id'], dtu_no, meter_state_info['address'], log.id)
        else:
            log_dict['opr_type'] = Operator.CLOSE_VALVE
            log = conf_log_api.add_opr_log(log_dict)
            opr = Operator.create_close_valve_opr(user['id'], dtu_no, meter_state_info['address'], log.id)

        app_opr_api.execute_remote_op(opr)


def update_recharge_state(meter_state_info, user):
    """
    更新仪表充值状态
    :param user: 当前登录的用户
    :param meter_state_info:
    :return:
    """
    must_dict = {
        "id": int,
        "meter_id": int,
        "address": int,
        "recharge_state": int,
        "dtu_no": int,
    }
    param_check(meter_state_info, must_dict, )

    dtu_no = meter_state_info['dtu_no']

    # 保证原子性
    with transaction.atomic():
        log_dict = {
            "opr_user_id": user['id'],
            "meter_id": meter_state_info['meter_id'],
        }
        if meter_state_info['recharge_state'] == RECHARGE_STATE_OPEN:
            log_dict['opr_type'] = Operator.OPEN_RECHARGE
            log = conf_log_api.add_opr_log(log_dict)
            opr = Operator.create_open_recharge_opr(user['id'], dtu_no, meter_state_info['address'], log.id)
        else:
            log_dict['opr_type'] = Operator.CLOSE_RECHARGE
            log = conf_log_api.add_opr_log(log_dict)
            opr = Operator.create_close_recharge_opr(user['id'], dtu_no, meter_state_info['address'], log.id)

        app_opr_api.execute_remote_op(opr)


def update_flow_ratio(meter_info, user):
    """
    更新仪表流量系数
    :param meter_info:
    :param user: 当前登录的用户
    :return:
    """
    must_dict = {
        "id": int,
        "address": int,
        "dtu_no": int,
        "flow_ratio": float,
    }
    param_check(meter_info, must_dict, )

    dtu_no = meter_info['dtu_no']
    log_dict = {"opr_user_id": user['id'], "meter_id": meter_info['meter_id'], 'opr_type': Operator.SET_FLOW_RATIO}
    # 保证原子性
    with transaction.atomic():
        log = conf_log_api.add_opr_log(log_dict)
        opr = Operator.create_set_flow_ratio_opr(user['id'], dtu_no, meter_info['address'],
                                                 log.id, meter_info['flow_ratio'])
        app_opr_api.execute_remote_op(opr)


def query_meter_data(meter_info, user):
    must_dict = {
        "id": int,
        "address": int,
        "dtu_no": int,
    }
    param_check(meter_info, must_dict)

    dtu_no = meter_info['dtu_no']
    log_dict = {"opr_user_id": user['id'], "meter_id": meter_info['meter_id'], 'opr_type': Operator.QUERY, 'val': None}
    # 保证原子性
    with transaction.atomic():
        log = conf_log_api.add_opr_log(log_dict)
        opr = Operator.create_query_opr(user['id'], dtu_no, meter_info['address'], log.id)
        app_opr_api.execute_remote_op(opr)


def reset_meter(meter_info, user):
    """
    重启仪表
    :param meter_info:
    :param user: 当前登录的用户
    :return:
    """
    must_dict = {
        "id": int,
        "address": int,
        "dtu_no": int,
    }
    param_check(meter_info, must_dict, )

    dtu_no = meter_info['dtu_no']

    log_dict = {"opr_user_id": user['id'], "meter_id": meter_info['meter_id'], 'opr_type': Operator.RESET, 'val': None}

    # 保证原子性
    with transaction.atomic():
        log = conf_log_api.add_opr_log(log_dict)
        opr = Operator.create_reset_opr(user['id'], dtu_no, meter_info['address'], log.id)
        app_opr_api.execute_remote_op(opr)


def recharge_meter(meter_info, user):
    """
    给仪表充值
    :param meter_info:
    :param user: 当前登录的用户
    :return:
    """
    must_dict = {
        "id": int,
        "address": int,
        "dtu_no": int,
        "money": int,
    }
    param_check(meter_info, must_dict, )

    dtu_no = meter_info['dtu_no']
    # 充值金额
    money = meter_info['money']

    log_dict = {"opr_user_id": user['id'], "meter_id": meter_info['meter_id'], 'opr_type': Operator.RECHARGE,
                'val': money}

    # 保证原子性
    with transaction.atomic():
        log = conf_log_api.add_opr_log(log_dict)
        opr = Operator.create_recharge_opr(user['id'], dtu_no, meter_info['address'], log.id, money)
        app_opr_api.execute_remote_op(opr)


def update_meter_data(dtu_no, data):
    """
    更新仪表实时信息
    :param dtu_no:
    :param data:
    :return:
    """
    must_dict = {
        "address": int,
        "opr_type": WhiteListCheck.check_opr_type,
        "data": None
    }
    param_check(data, must_dict)
    meter_data = {'last_update_time': datetime.datetime.now()}
    if data['opr_type'] == Operator.QUERY:
        status = data['data'].pop('status')
        meter_data.update(data['data'])
        conf_state_api.update_meter_state(dtu_no, data['address'], status)
    # 更新仪表物理地址
    elif data['opr_type'] == Operator.SET_METER_ADDRESS:
        meter_data.update({'address': data['data']})

    # 更新仪表流量系数
    elif data['opr_type'] == Operator.SET_FLOW_RATIO:
        meter_data.update({'flow_ratio': data['data']})

    # 增加剩余气量
    elif data['opr_type'] == Operator.RECHARGE:
        meter_data.update({'surplus_gas': F('surplus_gas') + data['data']})

    # 更新阀门状态
    elif data['opr_type'] == Operator.OPEN_VALVE:
        meter_data.update({'valve_state': VALVE_STATE_OPEN})

    # 更新阀门状态
    elif data['opr_type'] == Operator.CLOSE_VALVE:
        meter_data.update({'valve_state': VALVE_STATE_CLOSE})

    # 更新预充值状态
    elif data['opr_type'] == Operator.OPEN_RECHARGE:
        meter_data.update({'recharge_state': RECHARGE_STATE_OPEN})
    # 更新预充值状态
    elif data['opr_type'] == Operator.CLOSE_RECHARGE:
        meter_data.update({'recharge_state': RECHARGE_STATE_CLOSE})

    conf_state_api.update_meter_state(dtu_no, data['address'], meter_data)
