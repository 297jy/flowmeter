# coding=utf-8

from flowmeter.celery import app
from flowmeter.common.api.validators import param_check
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.operator_table import Operator
from flowmeter.config.api import operator as conf_opr_api
from flowmeter.celery_task.core import opr_task as core


@app.task
def update_opr_result(dtu_no, data):
    must_dict = {
        "opr_type": str,
        "address": int,
    }
    optional_dict = {
        "data": dict,
        "val": dict,
    }
    param_check(data, must_dict=must_dict, optional_dict=optional_dict)

    opr_log_id = conf_opr_api.get_earliest_operator(dtu_no, data['address'], data['opr_type'])
    # 没找到操作日志 直接返回
    if opr_log_id is None:
        return
    # 更新为成功状态
    core.update_log_success_state(opr_log_id)

    core.update_meter_data(dtu_no, data)






