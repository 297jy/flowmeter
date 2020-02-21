# coding=utf-8

from flowmeter.celery import app
from flowmeter.common.api.validators import param_check
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.operator_table import Operator
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


