# coding=utf-8
import traceback

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
    data_frame = frame.generate_data_frame(opr.meter_address, opr.opr_type, opr.val)
    # 直接向流量计发送数据帧
    try:
        server.send_data_frame(opr.dtu_no, data_frame)
        # 发送成功就把操作放进等待执行结果的队列中
        conf_operator_api.add_wait_operator(opr)
    except:
        traceback.print_exc()
        # 发送失败就放进未执行命令队列中
        conf_operator_api.add_unexecuted_operator(dict(opr))


def execute_unexecuted_remote_op(dtu_no):
    """
    执行一条还未执行的远程操作
    :return:
    """
    # 先获取缓存中存在的带执行的操作命令
    oprs_dict = conf_operator_api.get_all_unexecuted_opr(dtu_no)
    # 遍历所有待执行命令的仪表物理地址
    for address, opr_type_dict in oprs_dict.items():
        # 遍历所有命令类型
        for opr_type, oprs in opr_type_dict.items():

            # 如果是充值操作，则每条等待命令都需要发送
            if opr_type == Operator.RECHARGE:
                for opr in oprs:
                    with transaction.atomic():
                        conf_operator_api.get_and_del_earliest_unexecuted_opr(opr['meter_address'],
                                                                              opr['opr_type'], opr['val'])
                        conf_operator_api.add_wait_operator(opr)
                        data_frame = frame.generate_data_frame(opr['meter_address'], opr['opr_type'], opr['val'])
                        server.send_data_frame(dtu_no, data_frame)

            else:
                if len(oprs) > 0:
                    # 只需要执行最后一条命令，其他命令不用发送，状态直接设为成功
                    execute_opr = oprs[len(oprs) - 1]
                    log_ids = [opr['log_id'] for opr in oprs[0: -1]]
                    with transaction.atomic():
                        app_log_api.update_logs_success_state(log_ids)
                        # 把要执行的命令，放进等待队列中
                        conf_operator_api.add_wait_operator(execute_opr)
                        # 从待执行的命令队列中移除
                        conf_operator_api.remove_dtu_unexecuted_opr(dtu_no, address, opr_type)
                        data_frame = frame.generate_data_frame(address, opr_type, execute_opr['val'])
                        server.send_data_frame(dtu_no, data_frame)


def execute_wait_remote_op(dtu_no, address, opr_type, val):
    """
    执行一条等待执行结果的远程操作
    :return:
    """
    # 先获取缓存中存在的带执行的操作命令
    opr = conf_operator_api.get_and_del_wait_opr(dtu_no, address, opr_type, val)
    if opr is not None:
        app_log_api.update_logs_success_state([opr['log_id']])
