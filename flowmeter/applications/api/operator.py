# coding=utf-8


from flowmeter.modbus.api import server
from flowmeter.modbus.api import frame
from flowmeter.config.api import operator as conf_operator_api
from flowmeter.applications.api import log as app_log_api
from flowmeter.config.db.operator_table import Operator
from django.db import transaction

import logging

logger = logging.getLogger('log')


def execute_remote_op(opr):
    """
    执行远程操作
    :return:
    """
    opr = dict(opr)
    logger.info('添加了未执行操作：{}'.format(opr))
    with transaction.atomic():
        if opr['opr_type'] != Operator.RECHARGE:

            log_ids = conf_operator_api.get_log_ids_and_del_unexecuted_opr(opr['dtu_no'], opr['address'], opr['opr_type'])
            app_log_api.update_logs_success_state(log_ids)
            # 之前还未执行的关阀操作可以删除
            if opr['opr_type'] == Operator.OPEN_VALVE:
                log_ids = conf_operator_api.get_log_ids_and_del_unexecuted_opr(opr['dtu_no'], opr['address'],
                                                                               Operator.CLOSE_VALVE)
            if opr['opr_type'] == Operator.CLOSE_VALVE:
                log_ids = conf_operator_api.get_log_ids_and_del_unexecuted_opr(opr['dtu_no'], opr['address'],
                                                                               Operator.OPEN_VALVE)

            if opr['opr_type'] == Operator.OPEN_RECHARGE:
                log_ids = conf_operator_api.get_log_ids_and_del_unexecuted_opr(opr['dtu_no'], opr['address'],
                                                                               Operator.CLOSE_RECHARGE)
            if opr['opr_type'] == Operator.CLOSE_RECHARGE:
                log_ids = conf_operator_api.get_log_ids_and_del_unexecuted_opr(opr['dtu_no'], opr['address'],
                                                                               Operator.OPEN_RECHARGE)
            app_log_api.update_logs_success_state(log_ids)

        conf_operator_api.add_unexecuted_operator(opr)


def execute_unexecuted_remote_op(dtu_no):
    """
    执行一条还未执行的远程操作
    :return:
    """
    # 先获取缓存中存在的带执行的操作命令
    oprs = conf_operator_api.get_all_unexecuted_opr(dtu_no)

    # 正在等待的操作不重复执行
    wait_oprs = conf_operator_api.get_all_wait_opr(dtu_no)
    wait_opr_set = set()
    for opr in wait_oprs:
        key_name = "_".join([str(opr.dtu_no), str(opr.address), opr.opr_type])
        wait_opr_set.add(key_name)

    opr_map = {}
    for opr in oprs:
        key_name = "_".join([str(opr.dtu_no), str(opr.address), opr.opr_type])
        if key_name not in wait_opr_set:
            opr_map[key_name] = opr

    for opr in opr_map.values():
        try:
            with transaction.atomic():
                conf_operator_api.del_unexecuted_opr_by_id(opr.id)
                conf_operator_api.add_wait_operator(dict(opr))
                data_frame = frame.generate_data_frame(opr.address, opr.opr_type, opr.val)
                server.send_data_frame(dtu_no, data_frame)
        except Exception as ex:
            logger.error(str(ex))


def execute_wait_remote_op(dtu_no, address, opr_type):
    """
    执行一条等待执行结果的远程操作
    :return:返回正在等待结果的操作
    """
    # 先获取缓存中存在的带执行的操作命令
    opr = conf_operator_api.get_one_wait_opr(dtu_no, address, opr_type)
    if opr is not None:
        if opr.log_id:
            with transaction.atomic():
                app_log_api.update_logs_success_state([opr.log_id])
                opr.delete()
    return opr
