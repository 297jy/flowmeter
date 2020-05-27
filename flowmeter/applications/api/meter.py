# coding=utf-8

import datetime
import os

from flowmeter.applications.core import meter as core
from flowmeter.applications.api import operator as app_opr_api
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.api import meter_state as conf_state_api
from flowmeter.config.api import operator as conf_opr_api
from flowmeter.config.api import log as conf_log_api
from flowmeter.config.api import valve as conf_valve_api
from flowmeter.common.api.validators import param_check
from flowmeter.common.api.validators import StrCheck, WhiteListCheck, ListCheck
from flowmeter.config.db.operator_table import Operator
from flowmeter.config.const import VALVE_STATE_OPEN, VALVE_STATE_CLOSE, RECHARGE_STATE_OPEN, RECHARGE_STATE_CLOSE, \
    UNKNOWN_VALUE, UNKNOWN_STATE
from django.db import transaction
from flowmeter.config.db.meter_table import Meter
from flowmeter.settings import TMP_FILE_DIRECTORY_PATH
from flowmeter.common.api import file as common_file_api


def find_meter_by_query_terms(query_terms, user, page=None):
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
                                     query_terms.get('dtu_id'), user)

    meters, num = conf_meter_api.find_meters(filters, page)

    meter_dicts = []
    for meter in meters:
        meter_dicts.append(core.get_meter_dict(meter))

    return meter_dicts, num


def find_meter_state_by_id(state_id, user):
    state = conf_state_api.find_meter_state_by_id(state_id)
    state = core.get_meter_state_dict(state)
    if 'valve_state' not in user['actions']:
        if state['valve_state'] == UNKNOWN_VALUE or state['valve_state'] == UNKNOWN_STATE:
            state['valve_state'] = '未知'
        elif state['valve_state'] == VALVE_STATE_OPEN:
            state['valve_state'] = '开启'
        else:
            state['valve_state'] = "关闭"
    if 'recharge_state' not in user['actions']:
        if state['recharge_state'] == UNKNOWN_VALUE or state['recharge_state'] == UNKNOWN_STATE:
            state['recharge_state'] = '未知'
        elif state['recharge_state'] == RECHARGE_STATE_OPEN:
            state['recharge_state'] = '开启'
        else:
            state['recharge_state'] = "关闭"
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
        "valve_dtu_id": int,
        "valve_address": int,
        "remark": StrCheck.check_remark,
    }
    param_check(meter_info, must_dict, optional_dict)

    # 保证原子性
    with transaction.atomic():
        valve = core.get_valve_info(meter_info)
        # 添加仪表
        meter = conf_meter_api.add_meter(meter_info)
        # 添加状态
        conf_state_api.add_meter_state({'meter_id': meter.id})
        # 添加阀门控制器
        valve['meter_id'] = meter.id
        conf_valve_api.add_valve(valve)


def del_batch_meter(meter_ids):
    """
    :return:
    """

    dtu_nos = conf_meter_api.find_dtu_nos_by_meter_ids(meter_ids)
    # 保证原子性
    with transaction.atomic():
        conf_meter_api.del_batch_meter(meter_ids)
        # 清空操作队列
        for dtu_no in dtu_nos:
            conf_opr_api.clear_all_dtu_operator(dtu_no)


def update_meter(meter_info, user):
    """
    更新仪表信息
    :param meter_info:
    :param user:
    :return:
    """
    must_dict = {
        "id": int,
        "address": int,
        "dtu_no": int,
        "surplus_gas_limits": float,
    }
    optional_dict = {
        'remark': StrCheck.check_remark,
    }
    param_check(meter_info, must_dict, optional_dict)

    old_meter = conf_meter_api.find_meter_by_id(meter_info['id'])
    conf_meter_api.update_meter_info({"id": meter_info['id'],
                                      "surplus_gas_limits": meter_info['surplus_gas_limits'],
                                      "remark": meter_info.get('remark', '')})

    # 更改物理地址
    if old_meter.address != meter_info['address']:
        log_dict = {
            "opr_user_id": user['id'],
            "meter_id": meter_info['id'],
            "opr_type": Operator.SET_METER_ADDRESS,
        }
        # 保证原子性
        with transaction.atomic():
            log = conf_log_api.add_opr_log(log_dict)
            opr = Operator.create_set_meter_address_opr(meter_info['dtu_no'], old_meter.address, log.id,
                                                        meter_info['id'], meter_info['address'])
            app_opr_api.execute_remote_op(opr)


def update_valve_state(meter_state_info, user):
    """
    更改阀门状态
    :param user: 当前登录的用户
    :param meter_state_info:
    :return:
    """
    must_dict = {
        "meter_ids": ListCheck.check_is_int_list,
        "valve_state": int,
    }
    param_check(meter_state_info, must_dict, )

    # 查找该流量计对应的阀门DTU
    meter_infos = conf_meter_api.find_infos_by_meter_ids(meter_state_info['meter_ids'])

    for meter_info in meter_infos:
        # 保证原子性
        with transaction.atomic():
            log_dict = {
                "opr_user_id": user['id'],
                "meter_id": meter_info['meter_id'],
            }
            if meter_state_info['valve_state'] == VALVE_STATE_OPEN:
                log_dict['opr_type'] = Operator.OPEN_VALVE
                log = conf_log_api.add_opr_log(log_dict)
                opr = Operator.create_open_valve_opr(meter_info['dtu_no'], meter_info['address'], log.id,
                                                     meter_info['meter_id'])
            else:
                log_dict['opr_type'] = Operator.CLOSE_VALVE
                log = conf_log_api.add_opr_log(log_dict)
                opr = Operator.create_close_valve_opr(meter_info['dtu_no'], meter_info['address'], log.id,
                                                      meter_info['meter_id'])

            app_opr_api.execute_remote_op(opr)


def update_recharge_state(meter_state_info, user):
    """
    更新仪表充值状态
    :param user: 当前登录的用户
    :param meter_state_info:
    :return:
    """
    must_dict = {
        "meter_ids": ListCheck.check_is_int_list,
        "recharge_state": WhiteListCheck.check_recharge_state,
    }
    param_check(meter_state_info, must_dict, )

    meter_infos = conf_meter_api.find_infos_by_meter_ids(meter_state_info['meter_ids'])
    for meter_info in meter_infos:
        # 保证原子性
        with transaction.atomic():
            log_dict = {
                "opr_user_id": user['id'],
                "meter_id": meter_info['meter_id'],
            }
            if meter_state_info['recharge_state'] == RECHARGE_STATE_OPEN:
                log_dict['opr_type'] = Operator.OPEN_RECHARGE
                log = conf_log_api.add_opr_log(log_dict)
                opr = Operator.create_open_recharge_opr(meter_info['dtu_no'], meter_info['address'], log.id,
                                                        meter_info['meter_id'])
            else:
                log_dict['opr_type'] = Operator.CLOSE_RECHARGE
                log = conf_log_api.add_opr_log(log_dict)
                opr = Operator.create_close_recharge_opr(meter_info['dtu_no'], meter_info['address'], log.id,
                                                         meter_info['meter_id'])
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
    log_dict = {"opr_user_id": user['id'], "meter_id": meter_info['id'], 'opr_type': Operator.SET_FLOW_RATIO}
    # 保证原子性
    with transaction.atomic():
        log = conf_log_api.add_opr_log(log_dict)
        opr = Operator.create_set_flow_ratio_opr(dtu_no, meter_info['address'],
                                                 log.id, meter_info['id'], meter_info['flow_ratio'])
        app_opr_api.execute_remote_op(opr)


def query_meter_data(meter_info, user, record_log=True):
    must_dict = {
        "meter_ids": ListCheck.check_is_int_list,
    }
    param_check(meter_info, must_dict)
    meter_infos = conf_meter_api.find_infos_by_meter_ids(meter_info['meter_ids'])

    for meter_info in meter_infos:
        dtu_no = meter_info['dtu_no']

        log_dict = {}
        if record_log:
            log_dict = {"opr_user_id": user['id'], "meter_id": meter_info['meter_id'], 'opr_type': Operator.QUERY,
                        'val': ""}
        # 保证原子性
        with transaction.atomic():

            log_id = None
            if record_log:
                log = conf_log_api.add_opr_log(log_dict)
                log_id = log.id

            opr = Operator.create_query_opr(dtu_no, meter_info['address'], log_id, meter_info['meter_id'])
            app_opr_api.execute_remote_op(opr)


def reset_meter(meter_info, user):
    """
    重启仪表
    :param meter_info:
    :param user: 当前登录的用户
    :return:
    """
    must_dict = {
        "meter_ids": ListCheck.check_is_int_list,
    }
    param_check(meter_info, must_dict, )

    meter_infos = conf_meter_api.find_infos_by_meter_ids(meter_info['meter_ids'])
    for meter_info in meter_infos:
        log_dict = {"opr_user_id": user['id'], "meter_id": meter_info['meter_id'], 'opr_type': Operator.RESET,
                    'val': ""}
        # 保证原子性
        with transaction.atomic():
            log = conf_log_api.add_opr_log(log_dict)
            opr = Operator.create_reset_opr(meter_info['dtu_no'], meter_info['address'], log.id, meter_info['meter_id'])
            app_opr_api.execute_remote_op(opr)


def recharge_meter(meter_ids, money, user):
    """
    给仪表充值
    :param money: 充值的数量
    :param meter_ids: 充值的仪表id
    :param user: 当前登录的用户
    :return:
    """

    meter_infos = conf_meter_api.find_infos_by_meter_ids(meter_ids)

    for meter_info in meter_infos:
        log_dict = {"opr_user_id": user['id'], "meter_id": meter_info['meter_id'], 'opr_type': Operator.RECHARGE,
                    'val': money}
        # 保证原子性
        with transaction.atomic():
            log = conf_log_api.add_opr_log(log_dict)
            opr = Operator.create_recharge_opr(meter_info['dtu_no'], meter_info['address'], log.id,
                                               meter_info['meter_id'], money)
            app_opr_api.execute_remote_op(opr)


def update_meter_data(meter_id, data):
    """
    更新仪表实时信息
    :param meter_id:
    :param data:
    :return:
    """
    must_dict = {
        "address": int,
        "opr_type": WhiteListCheck.check_opr_type,
    }

    param_check(data, must_dict, extra=True)
    meter_data = {'last_update_time': datetime.datetime.now()}

    if data['opr_type'] == Operator.QUERY:
        status = data['data'].pop('status')
        meter_data.update(data['data'])
        conf_state_api.update_meter_state(meter_id, status)

    # 更新仪表物理地址
    elif data['opr_type'] == Operator.SET_METER_ADDRESS:
        meter_data.update({'address': data['data']})

    # 更新仪表流量系数
    elif data['opr_type'] == Operator.SET_FLOW_RATIO:
        meter_data.update({'flow_ratio': data['data']})

    # 更新剩余气量
    elif data['opr_type'] == Operator.RECHARGE:
        surplus_gas = conf_meter_api.get_meter_surplus_gas(meter_id)
        meter_data.update({'surplus_gas': int(surplus_gas + data['data'])})

    # 更新阀门状态
    elif data['opr_type'] == Operator.OPEN_VALVE:
        conf_state_api.update_meter_state(meter_id, {'valve_state': VALVE_STATE_OPEN})

    # 更新阀门状态
    elif data['opr_type'] == Operator.CLOSE_VALVE:
        conf_state_api.update_meter_state(meter_id, {'valve_state': VALVE_STATE_CLOSE})

    # 更新预充值状态
    elif data['opr_type'] == Operator.OPEN_RECHARGE:
        conf_state_api.update_meter_state(meter_id, {'recharge_state': RECHARGE_STATE_OPEN})

    # 更新预充值状态
    elif data['opr_type'] == Operator.CLOSE_RECHARGE:
        conf_state_api.update_meter_state(meter_id, {'recharge_state': RECHARGE_STATE_CLOSE})

    conf_meter_api.update_meter_data(meter_id, meter_data)


def get_meter_state_view_info(meter_id):
    """
    获取仪表状态视图需要的消息
    :param meter_id: 仪表id
    :return:
    """
    meter = Meter.objects.values("meterstate__id", "dtu__dtu_no", "valve__id", "address").get(id=meter_id)
    return {
        "meter_id": meter_id,
        "dtu_no": meter.get('dtu__dtu_no'),
        "id": meter.get('meterstate__id'),
        "valve_id": meter.get('valve__id'),
        "address": meter.get('address'),
    }


def update_valve_address(valve_info):
    must_dict = {
        "id": int,
        "address": int,
    }
    param_check(valve_info, must_dict)

    conf_valve_api.update_valve(valve_info)


def update_valve_dtu(valve_info):
    must_dict = {
        "id": int,
        "dtu_id": int,
    }
    param_check(valve_info, must_dict)

    conf_valve_api.update_valve(valve_info)


def generate_report_table(meter_ids):
    """
    生成报表
    :return:
    """
    meter_infos = conf_meter_api.find_infos_by_meter_ids(meter_ids)

    file_list = []
    for meter_info in meter_infos:
        filename = 'DTU编号：{}-物理地址：{}-报表.html'.format(meter_info['dtu_no'], meter_info['address'])
        path = os.path.join(TMP_FILE_DIRECTORY_PATH, filename)
        file_list.append(path)
        core.draw_report(path, meter_info['meter_id'])

    zipfile = common_file_api.compress_file(file_list)
    return zipfile
