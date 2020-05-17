# coding=utf-8

import time

from flowmeter.config.db.operator_table import Operator, UnExecutedOpr, WaitOpr
from flowmeter.common.api.validators import param_check, WhiteListCheck

import logging
logger = logging.getLogger('log')


def add_unexecuted_operator(opr):
    """
    添加新的操作到待执行的队列中
    :param opr:
    :return:
    """
    must_dict = {
        'dtu_no': int,
        'address': int,
        'opr_type': WhiteListCheck.check_opr_type,
    }
    param_check(opr, must_dict, extra=True)
    opr['opr_time'] = time.time()

    UnExecutedOpr.objects.create(**opr)


def get_all_unexecuted_opr(dtu_no):

    oprs = UnExecutedOpr.objects.filter(dtu_no=dtu_no)
    return oprs


def add_wait_operator(opr):
    """
    添加到等待执行结果的队列中
    :param opr:
    :return:
    """
    must_dict = {
        'dtu_no': int,
        'address': int,
        'opr_type': WhiteListCheck.check_opr_type,
    }
    param_check(opr, must_dict, extra=True)

    opr['opr_time'] = time.time()

    WaitOpr.objects.create(**opr)


def get_one_wait_opr(dtu_no, address, opr_type):
    """获取并删除一个等待操作"""
    try:
        opr = WaitOpr.objects.get(dtu_no=dtu_no, address=address, opr_type=opr_type)
        return opr
    except WaitOpr.DoesNotExist:
        return None


def get_and_del_earliest_unexecuted_opr(dtu_no, address, opr_type):
    try:
        opr = UnExecutedOpr.objects.get(dtu_no=dtu_no, address=address, opr_type=opr_type)
        opr.delete()
        return opr
    except WaitOpr.DoesNotExist:
        return None


def get_all_wait_opr_by_dtu_no(dtu_no):
    oprs = WaitOpr.objects.filter(dtu_no=dtu_no)
    return oprs


def clear_all_timeout_wait_oprs(time_out):
    """
    清除所有已经超时的等待操作
    :param time_out:
    :return: 已经清除的等待操作
    """
    now_time = time.time()
    oprs = WaitOpr.objects.filter(opr_time__lt=now_time-time_out)
    oprs.delete()
    return oprs


def clear_all_dtu_operator(dtu_no):
    """
    删除关于DTU的所有命令操作
    :param dtu_no:
    :return:
    """
    UnExecutedOpr.objects.filter(dtu_no=dtu_no).delete()
    WaitOpr.objects.filter(dtu_no=dtu_no).delete()


def remove_dtu_unexecuted_opr(dtu_no, address, opr_type):
    """
    移除关于DTU的未执行的命令操作
    :param address:
    :param opr_type:
    :param dtu_no:
    :return:
    """
    UnExecutedOpr.objects.filter(dtu_no=dtu_no, address=address, opr_type=opr_type).delete()


def remove_dtu_wait_opr(dtu_no, address, opr_type):
    """
    移除关于DTU的等待操作结果的命令操作
    :param address:
    :param opr_type:
    :param dtu_no:
    :return:
    """
    WaitOpr.objects.filter(dtu_no=dtu_no, address=address, opr_type=opr_type).delete()


def get_log_ids_and_del_unexecuted_opr(dtu_no, address, opr_type):

    oprs = UnExecutedOpr.objects.filter(dtu_no=dtu_no, address=address, opr_type=opr_type)
    log_ids = [opr.log_id for opr in oprs]
    oprs.delete()
    return log_ids


def del_unexecuted_opr_by_ids(opr_ids):

    UnExecutedOpr.objects.filter(id__in=opr_ids).delete()


def del_unexecuted_opr_by_id(opr_id):
    UnExecutedOpr.objects.filter(id=opr_id).delete()




