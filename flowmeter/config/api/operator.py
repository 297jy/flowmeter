# coding=utf-8

from flowmeter.config.api import cache
from flowmeter.common.api.validators import param_check, WhiteListCheck


def add_operator(opr):
    """
    添加操作
    :param opr:
    :return:
    """
    key = 'operator_{}_{}_{}'.format(opr.dtu_no, opr.opr_type, opr.address)
    cache.add_sorted_set(key, opr.log_id, opr.opr_time)


def get_earliest_operator(dtu_no, address, opr_type):
    """
    获取日期最早的操作
    :param opr_type:
    :param address:
    :param dtu_no:
    :return:
    """
    key = 'operator_{}_{}_{}'.format(dtu_no, opr_type, address)
    opr = cache.get_sorted_set_first(key)
    return opr


def clear_dtu_operator(dtu_no):
    """
    删除关于DTU的所有命令操作
    :param dtu_no:
    :return:
    """
    key = 'operator_{}*'.format(dtu_no)
    cache.delete(key)


