# coding=utf-8

from flowmeter.config.api import cache
from flowmeter.common.api.validators import param_check, WhiteListCheck


def add_operator(opr):
    """
    添加操作
    :param opr:
    :return:
    """

    must_dict = {
        'user_id': int,
        'opr_type': WhiteListCheck.check_opr_type,
        "opr_time": int,
        "dtu_no": int,
        "meter_address": int,
    }
    param_check(opr, must_dict=must_dict, extra=True)

    keyname = 'operator' + str(opr['dtu_no'])
    cache.add_sorted_set(keyname, opr, opr['opr_time'])


def get_earliest_operator(dtu_no):
    """
    获取日期最早的操作
    :param dtu_no:
    :return:
    """
    keyname = 'operator' + str(dtu_no)
    opr = cache.get_sorted_set_first(keyname)
    return opr


