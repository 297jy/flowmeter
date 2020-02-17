# coding=utf-8

from flowmeter.config.db.meter_table import Meter
from flowmeter.config.core import meter as core


def find_opr_logs_by_meter(meter_obj):

    logs = core.find_meter_opr_logs(meter_obj)

    return logs

