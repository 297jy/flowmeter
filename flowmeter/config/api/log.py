# coding=utf-8

import datetime
from flowmeter.config.core import log as core
from flowmeter.config.db.log_table import OprLog, SystemLog, AlarmLog
from flowmeter.common.api.validators import param_check, WhiteListCheck, StrCheck


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
        "opr_user_id": int,
        "meter_id": int,
    }
    if log.get('val') is not None:
        log['val'] = str(log['val'])
    param_check(log, must_dict=must_dict, extra=True)

    log['state'] = OprLog.WAITE_STATE
    log['opr_time'] = datetime.datetime.now()
    return core.add_opr_log(log)


def add_system_log(log):

    must_dict = {
        "action_type": StrCheck.check_action_type,
        "opr_user_id": int,
        "opr_time": datetime.datetime,
        "state": WhiteListCheck.check_opr_state,
    }
    optional_dict = {
        "msg": StrCheck.check_msg,
    }

    param_check(log, must_dict=must_dict, optional_dict=optional_dict)

    return core.add_system_log(log)


def find_opr_log_by_id(log_id):

    log = core.find_one_opr_log({"id": log_id})

    return log


def update_opr_logs_state(log_ids, state):

    OprLog.objects.filter(id__in=log_ids).update(state=state)


def find_opr_log(filters=None, page=None):
    """
    查询操作日志，按操作日期降序
    :param filters:
    :param page:
    :return:
    """
    if page is None:
        if filters:
            logs = OprLog.objects.filter(filters).order_by('-opr_time')
        else:
            logs = OprLog.objects.filter(filters).order_by('-opr_time')
    else:
        start_index = page.limit * (page.index - 1)
        end_index = page.index * page.limit
        if filters:
            logs = OprLog.objects.filter(filters).order_by('-opr_time')[start_index: end_index]
        else:
            logs = OprLog.objects.all().order_by('-opr_time')[start_index: end_index]

    return logs


def find_system_log(filters=None, page=None):
    """
    查询系统日志，按操作日期降序
    :param filters:
    :param page:
    :return:
    """
    if page is None:
        if filters:
            logs = SystemLog.objects.filter(filters).order_by('-opr_time')
        else:
            logs = SystemLog.objects.filter(filters).order_by('-opr_time')
    else:
        start_index = page.limit * (page.index - 1)
        end_index = page.index * page.limit
        if filters:
            logs = SystemLog.objects.filter(filters).order_by('-opr_time')[start_index: end_index]
        else:
            logs = SystemLog.objects.all().order_by('-opr_time')[start_index: end_index]

    return logs


def find_alarm_log(filters=None, page=None):
    """
    查询警报日志，按操作日期降序
    :param filters:
    :param page:
    :return:
    """
    if page is None:
        if filters:
            logs = AlarmLog.objects.filter(filters).order_by('-opr_time')
        else:
            logs = AlarmLog.objects.filter(filters).order_by('-opr_time')
    else:
        start_index = page.limit * (page.index - 1)
        end_index = page.index * page.limit
        if filters:
            logs = AlarmLog.objects.filter(filters).order_by('-opr_time')[start_index: end_index]
        else:
            logs = AlarmLog.objects.all().order_by('-opr_time')[start_index: end_index]

    return logs


def del_opr_logs(opr_log_ids):

    OprLog.objects.filter(id__in=opr_log_ids).delete()


def del_system_logs(opr_log_ids):

    SystemLog.objects.filter(id__in=opr_log_ids).delete()


def del_alarm_logs(opr_log_ids):

    AlarmLog.objects.filter(id__in=opr_log_ids).delete()





