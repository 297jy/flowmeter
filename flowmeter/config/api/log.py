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
    return core.add_alarm_log(log)


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
    if len(log_ids) == 0:
        return
    OprLog.objects.filter(id__in=log_ids).update(state=state)


def update_alarm_log_state(log_id, state):

    log = AlarmLog.objects.get(id=log_id)
    log.state = state
    log.save()


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


def get_system_log_total_num():

    log_total_num = SystemLog.objects.all().count()
    return log_total_num


def get_alarm_log_total_num():
    log_total_num = AlarmLog.objects.all().count()
    return log_total_num


def get_operator_log_total_num():
    log_total_num = OprLog.objects.all().count()
    return log_total_num


def get_sub_valve_alarm_num_by_man_id(man_id):

    num = AlarmLog.objects.filter(alarm_type=AlarmLog.ALARM_SUB_VALVE, meter__dtu__region__manufacturer_id=man_id)\
        .count()
    return num


def get_sensor_alarm_num_by_man_id(man_id):
    num = AlarmLog.objects.filter(alarm_type=AlarmLog.ALARM_SENSOR_ERROR, meter__dtu__region__manufacturer_id=man_id) \
        .count()
    return num


def get_exceed_alarm_num_by_man_id(man_id):
    num = AlarmLog.objects.filter(alarm_type=AlarmLog.ALARM_EXCEED_LIMIT, meter__dtu__region__manufacturer_id=man_id) \
        .count()
    return num


def get_valve_alarm_num_by_man_id(man_id):
    num = AlarmLog.objects.filter(alarm_type=AlarmLog.ALARM_VALVE_ERROR, meter__dtu__region__manufacturer_id=man_id) \
        .count()
    return num


def get_sub_valve_alarm_num_by_dtu_user_id(dtu_user_id):

    num = AlarmLog.objects.filter(alarm_type=AlarmLog.ALARM_SUB_VALVE, meter__dtu__user__id=dtu_user_id)\
        .count()
    return num


def get_sensor_alarm_num_by_dtu_user_id(man_id):
    num = AlarmLog.objects.filter(alarm_type=AlarmLog.ALARM_SENSOR_ERROR, meter__dtu__user__id=man_id) \
        .count()
    return num


def get_exceed_alarm_num_by_dtu_user_id(man_id):
    num = AlarmLog.objects.filter(alarm_type=AlarmLog.ALARM_EXCEED_LIMIT, meter__dtu__user__id=man_id) \
        .count()
    return num


def get_valve_alarm_num_by_dtu_user_id(man_id):
    num = AlarmLog.objects.filter(alarm_type=AlarmLog.ALARM_VALVE_ERROR, meter__dtu__user__id=man_id) \
        .count()
    return num










