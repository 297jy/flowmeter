# coding=utf-8

from flowmeter.config.api import cache
from flowmeter.config.db.operator_table import Operator
from flowmeter.common.api.validators import param_check, WhiteListCheck


def add_unexecuted_operator(opr):
    """
    添加新的操作到待执行的队列中
    :param opr:
    :return:
    """
    key = 'opr_unexecuted_{}'.format(opr.dtu_no)
    # 获取地址映射
    address_dict = cache.get_obj(key)
    # 获取操作类型映射
    opr_type_dict = address_dict.get(opr.meter_address, {})
    # 获取操作列表
    oprs = opr_type_dict.get(opr.opr_type, [])
    # 添加新操作到最后末尾
    oprs.append(opr)
    cache.set_obj(key, address_dict)


def add_wait_operator(opr):
    """
    添加到等待执行结果的队列中
    :param opr:
    :return:
    """
    key = 'opr_wait_{}'.format(opr.dtu_no)
    # 获取地址映射
    address_dict = cache.get_obj(key)
    # 获取操作类型映射
    opr_type_dict = address_dict.get(opr.meter_address, {})
    # 获取操作列表
    oprs = opr_type_dict.get(opr.opr_type, [])
    # 添加新操作到最后末尾
    oprs.append(opr)
    cache.set_obj(key, address_dict)


def get_all_unexecuted_opr(dtu_no):

    key = 'operator_unexecuted_{}'.format(dtu_no)
    oprs_dict = cache.get_obj(key)
    return oprs_dict


def get_all_wait_opr(dtu_no):

    key = 'operator_wait_{}'.format(dtu_no)
    oprs_dict = cache.get_obj(key)
    return oprs_dict


def clear_all_dtu_operator(dtu_no):
    """
    删除关于DTU的所有命令操作
    :param dtu_no:
    :return:
    """
    key = 'operator_unexecuted_{}'.format(dtu_no)
    cache.delete(key)
    key = 'operator_wait_{}'.format(dtu_no)
    cache.delete(key)


def remove_dtu_unexecuted_opr(dtu_no, address, opr_type):
    """
    移除关于DTU的未执行的命令操作
    :param address:
    :param opr_type:
    :param dtu_no:
    :return:
    """
    key = 'operator_unexecuted_{}'.format(dtu_no)
    # 获取地址映射
    address_dict = cache.get_obj(key)
    # 获取操作类型映射
    opr_type_dict = address_dict.get(address, {})
    opr_type_dict[opr_type] = []
    cache.set_obj(key, address_dict)


def remove_dtu_wait_opr(dtu_no, address, opr_type):
    """
    移除关于DTU的等待操作结果的命令操作
    :param address:
    :param opr_type:
    :param dtu_no:
    :return:
    """
    key = 'operator_wait_{}'.format(dtu_no)
    address_dict = cache.get_obj(key)
    # 获取操作类型映射
    opr_type_dict = address_dict.get(address, {})
    opr_type_dict[opr_type] = []
    cache.set_obj(key, address_dict)


def get_and_del_earliest_unexecuted_opr(dtu_no, address, opr_type):
    key = 'operator_unexecuted_{}'.format(dtu_no)
    # 获取地址映射
    address_dict = cache.get_obj(key)
    # 获取操作类型映射
    opr_type_dict = address_dict.get(address, {})
    # 获取操作列表
    oprs = opr_type_dict.get(opr_type, [])
    if len(oprs) == 0:
        return None
    opr = oprs[0]
    opr_type_dict[opr_type] = oprs[1: len(oprs)]
    cache.set_obj(key, address_dict)
    return opr


def get_and_del_earliest_wait_opr(dtu_no, address, opr_type):
    key = 'operator_wait_{}'.format(dtu_no)
    # 获取地址映射
    address_dict = cache.get_obj(key)
    # 获取操作类型映射
    opr_type_dict = address_dict.get(address, {})
    # 获取操作列表
    oprs = opr_type_dict.get(opr_type, [])
    if len(oprs) == 0:
        return None
    opr = oprs[0]
    opr_type_dict[opr_type] = oprs[1: len(oprs)]
    cache.set_obj(key, address_dict)
    return opr



