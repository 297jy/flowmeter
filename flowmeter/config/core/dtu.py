# coding=utf-8
from flowmeter.common.api import query
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

    return Dtu.objects.create(**dtu_info)


def find_dtu_meters(dtu):

    meters = dtu.meter_set.all()

    return meters


def del_batch_dtu(dtu_ids):
    """
    批量删除DTU
    :return:
    """
    query_terms = query.QueryTerms.make_or_query_terms(**{'id': dtu_ids})

    Dtu.objects.filter(query_terms.get_filters()).delete()
