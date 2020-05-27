# coding=utf-8

from flowmeter.config.db.log_table import AlarmLog, OprLog, SystemLog


def add_alarm_log(log):

    return AlarmLog.objects.create(alarm_type=log['alarm_type'], meter_id=log['meter_id'], opr_time=log['opr_time'])


def add_opr_log(log):

    opr = OprLog.objects.create(**log)
    return opr


def add_system_log(log):

    log = SystemLog.objects.create(**log)
    return log


def find_one_opr_log(log_info):

    try:
        opr = OprLog.objects.get(**log_info)
        return opr
    except OprLog.DoesNotExist:
        return None


def find_one_system_log(log_info):

    try:
        log = SystemLog.objects.get(**log_info)
        return log
    except SystemLog.DoesNotExist:
        return None

