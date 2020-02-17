# coding=utf-8

from flowmeter.config.db.meter_table import Meter


def find_meter_opr_logs(meter):

    logs = meter.alarmlog_set.all()

    return logs


def find_one_meter(meter_info):

    try:
        meter = Meter.objects.get(**meter_info)
        return meter
    except Meter.DoesNotExist:
        return None

