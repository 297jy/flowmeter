# coding=utf-8

from flowmeter.config.api import cache
from flowmeter.common.api.validators import param_check, WhiteListCheck


def add_operator(opr):
    """
    添加操作
    :param opr:
    :return:
    """

    keyname = 'operator_' + opr.opr_type + '_' + str(opr.dtu_no) + '_' + str(opr.address)
    cache.add_sorted_set(keyname, opr.log_id, opr.opr_time)


def get_earliest_operator(dtu_no, address, opr_type):
    """
    获取日期最早的操作
    :param opr_type:
    :param address:
    :param dtu_no:
    :return:
    """
    keyname = 'operator_' + opr_type + '_' + str(dtu_no) + '_' + str(address)
    opr = cache.get_sorted_set_first(keyname)
    return opr


