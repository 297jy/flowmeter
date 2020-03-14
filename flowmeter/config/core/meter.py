# coding=utf-8

from flowmeter.config.db.meter_table import Meter
from django.db.utils import IntegrityError
from flowmeter.exceptions import ValueDuplicateException


def find_meter_opr_logs(meter):

    logs = meter.alarmlog_set.all()

    return logs


def find_one_meter(meter_info):

    try:
        meter = Meter.objects.prefetch_related('dtu').get(**meter_info)
        return meter
    except Meter.DoesNotExist:
        return None


def find_meters(meter_info):

    meters = Meter.objects.filter(**meter_info)

    return meters


def add_meter(meter_info):

    try:
        Meter.objects.create(**meter_info)
    except IntegrityError:
        raise ValueDuplicateException("该仪表已存在！")


def update_meter(old_meter, new_meter):
    """
    跟新仪表数据
    :param old_meter:
    :param new_meter:
    :return:
    """
    update_flag = False

    # 遍历字典存在的属性
    for field, val in new_meter.items():

        if getattr(old_meter, field) != val:
            update_flag = True
            setattr(old_meter, field, val)

    if update_flag:
        old_meter.save()


def update_meter_state(old_state, new_state):

    for field, val in new_state:
        setattr(old_state, field, val)

    old_state.save()


def del_batch_meter(meter_ids):
    """
    批量删除仪表
    :return:
    """

    Meter.objects.filter(id__in=meter_ids).delete()


