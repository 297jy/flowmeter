# coding=utf-8

import datetime
from flowmeter.config.core import log as core
from flowmeter.common.api.validators import param_check, WhiteListCheck


def add_alarm_log(log):

    must_dict = {
        "alarm_type": WhiteListCheck.check_alarm_type
    }
    param_check(log, must_dict=must_dict, extra=True)

    log['opr_time'] = datetime.datetime.now()
    core.add_alarm_log(log)


def add_opr_log(log):

    must_dict = {
        "opr_type": WhiteListCheck.check_opr_type,
        "state": WhiteListCheck.check_opr_state,
    }
    param_check(log, must_dict=must_dict, extra=True)

    log['opr_time'] = datetime.datetime.now()
    core.add_opr_log(log)


def find_earliest_opr_log(log_info):

    log = core.find_earliest_opr_log(log_info)

    return log


def find_opr_log_by_id(log_id):

    log = core.find_one_opr_log({"id": log_id})

    return log


def update_opr_log_state(log_id, state):

    log = find_opr_log_by_id(log_id)
    core.update_opr_log_state(log, state)





