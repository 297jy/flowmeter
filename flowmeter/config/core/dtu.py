# coding=utf-8

from flowmeter.config.db.dtu_table import Dtu


def find_one_dtu(dtu_info):
    """
    :param dtu_info:
    :return:
    """
    try:
        dtu = Dtu.objects.get(**dtu_info)
        return dtu
    except Dtu.DoesNotExist:
        return None


def add_dtu(dtu_info):

    Dtu.objects.create(**dtu_info)


def find_dtu_meters(dtu):

    meters = dtu.meter_set.all()

    return meters
