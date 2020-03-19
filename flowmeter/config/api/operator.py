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
    must_dict = {
        'dtu_no': int,
        'meter_address': int,
        'opr_type': WhiteListCheck.check_opr_type,
    }
    param_check(opr, must_dict, extra=True)

    key = 'opr_unexecuted_{}'.format(opr['dtu_no'])
    # 获取地址映射
    address_dict = cache.get_obj(key)
    if address_dict is None:
        address_dict = {}
    # 获取操作类型映射
    opr_type_dict = address_dict.get(opr['meter_address'], {})
    # 获取操作列表
    oprs = opr_type_dict.get(opr['opr_type'], [])
    # 添加新操作到最后末尾
    oprs.append(dict(opr))

    opr_type_dict[opr['opr_type']] = oprs
    address_dict[opr['meter_address']] = opr_type_dict

    cache.set_obj(key, address_dict)


def add_wait_operator(opr):
    """
    添加到等待执行结果的队列中
    :param opr:
    :return:
    """
    must_dict = {
        'dtu_no': int,
        'meter_address': int,
        'opr_type': WhiteListCheck.check_opr_type,
    }
    param_check(opr, must_dict, extra=True)

    key = 'opr_wait_{}'.format(opr['dtu_no'])
    # 获取地址映射
    address_dict = cache.get_obj(key)
    if address_dict is None:
        address_dict = {}

    # 获取操作类型映射
    opr_type_dict = address_dict.get(opr['meter_address'], {})
    # 获取操作列表
    oprs = opr_type_dict.get(opr['opr_type'], [])
    # 添加新操作到最后末尾
    oprs.append(opr)

    opr_type_dict[opr['opr_type']] = oprs
    address_dict[opr['meter_address']] = opr_type_dict

    cache.set_obj(key, address_dict)


def get_all_unexecuted_opr(dtu_no):

    key = 'opr_unexecuted_{}'.format(dtu_no)
    oprs_dict = cache.get_obj(key)
    return oprs_dict if oprs_dict is not None else {}


def get_all_wait_opr(dtu_no):

    key = 'opr_wait_{}'.format(dtu_no)
    oprs_dict = cache.get_obj(key)
    return oprs_dict


def clear_all_dtu_operator(dtu_no):
    """
    删除关于DTU的所有命令操作
    :param dtu_no:
    :return:
    """
    key = 'opr_unexecuted_{}'.format(dtu_no)
    cache.delete(key)
    key = 'opr_wait_{}'.format(dtu_no)
    cache.delete(key)


def remove_dtu_unexecuted_opr(dtu_no, address, opr_type):
    """
    移除关于DTU的未执行的命令操作
    :param address:
    :param opr_type:
    :param dtu_no:
    :return:
    """
    address = str(address)

    key = 'opr_unexecuted_{}'.format(dtu_no)
    # 获取地址映射
    address_dict = cache.get_obj(key)
    if address_dict is None:
        address_dict = {}

    # 获取操作类型映射
    opr_type_dict = address_dict.get(address, {})
    opr_type_dict[opr_type] = []
    address_dict[address] = opr_type_dict
    cache.set_obj(key, address_dict)


def remove_dtu_wait_opr(dtu_no, address, opr_type):
    """
    移除关于DTU的等待操作结果的命令操作
    :param address:
    :param opr_type:
    :param dtu_no:
    :return:
    """
    address = str(address)

    key = 'opr_wait_{}'.format(dtu_no)
    address_dict = cache.get_obj(key)
    # 获取操作类型映射
    opr_type_dict = address_dict.get(address, {})
    opr_type_dict[opr_type] = []
    address_dict[address] = opr_type_dict
    cache.set_obj(key, address_dict)


def get_and_del_earliest_unexecuted_opr(dtu_no, address, opr_type):

    address = str(address)

    key = 'opr_unexecuted_{}'.format(dtu_no)
    # 获取地址映射
    address_dict = cache.get_obj(key)
    if address_dict is None:
        address_dict = {}
    # 获取操作类型映射
    opr_type_dict = address_dict.get(address, {})
    # 获取操作列表
    oprs = opr_type_dict.get(opr_type, [])
    if len(oprs) == 0:
        return None

    opr = oprs[0]
    opr_type_dict[opr_type] = oprs[1: len(oprs)]

    address_dict[address] = opr_type_dict
    cache.set_obj(key, address_dict)
    return opr


def get_and_del_wait_opr(dtu_no, address, opr_type, val):

    key = 'opr_wait_{}'.format(dtu_no)

    address = str(address)
    # 获取地址映射
    address_dict = cache.get_obj(key)
    if address_dict is None:
        address_dict = {}
    # 获取操作类型映射
    opr_type_dict = address_dict.get(address, {})
    # 获取操作列表
    oprs = opr_type_dict.get(opr_type, [])

    opr = None
    if len(oprs) == 0:
        return None

    if opr_type == Operator.QUERY:
        opr = oprs[0]
        opr_type_dict[opr_type] = oprs[1: len(oprs)]
    else:
        for i in range(0, len(oprs)):
            if oprs[i]['val'] == val:
                opr = oprs[i]
                break
        if opr is not None:
            oprs.remove(opr)
        opr_type_dict[opr_type] = oprs

    address_dict[address] = opr_type_dict
    cache.set_obj(key, address_dict)
    return opr



