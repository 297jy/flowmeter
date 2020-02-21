# coding=utf-8

from flowmeter.config.db.log_table import AlarmLog, OprLog, LoginLog


def add_alarm_log(log):

    AlarmLog.objects.create(**log)


def add_opr_log(log):

    OprLog.objects.create(**log)


def find_one_opr_log(log_info):

    try:
        opr = OprLog.objects.get(**log_info)
        return opr
    except OprLog.DoesNotExist:
        return None


def find_earliest_opr_log(log_info):

    log = OprLog.objects.filter(**log_info).order_by('opr_time')[0: 1]

    return log


def update_opr_log_state(log, state):

    log.state = state
    log.save()

