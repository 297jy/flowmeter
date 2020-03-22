# coding=utf-8
import datetime

from flowmeter.common.api.validators import param_check
from flowmeter.config.db.alarm_log_reader import AlarmLogReader
from flowmeter.config.db.log_table import AlarmLog


def add_unread_alarm(unread_alarm_dict):
    must_dict = {
        "user_id": int,
        "alarm_log": AlarmLog,
    }
    param_check(unread_alarm_dict, must_dict)

    user_id = unread_alarm_dict['user_id']
    alarm = unread_alarm_dict['alarm_log']
    now = datetime.datetime.now()
    unread_alarm_dict['unique_flag'] = '{}_{}_{}_{}_{}_{}'.format(now.year, now.month, now.day, user_id, alarm.meter.id,
                                                                  alarm.alarm_type)
    log_read = AlarmLogReader.objects.create(**unread_alarm_dict)

    return log_read


def read_alarm(alarm_read_id):

    reader = AlarmLogReader.objects.get(id=alarm_read_id)
    reader.state = AlarmLogReader.STATE_READ
    reader.save()


def get_user_unread_alarms(user_id):

    readers = AlarmLogReader.objects.filter(user_id=user_id, state=AlarmLogReader.STATE_UNREAD)
    return readers
