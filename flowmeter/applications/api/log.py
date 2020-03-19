# coding=utf-8

from flowmeter.config.api import log as conf_log_api
from flowmeter.config.db.log_table import OprLog
from flowmeter.common.api.validators import param_check, WhiteListCheck, StrCheck
from flowmeter.applications.core import log as core


def find_logs_by_query_terms(query_terms, page=None):
    """
    :param page: 分页对象
    :param query_terms:
    :return: 查询到的操作日志列表
    """

    optional_dict = {
        "begin_time": str,
        "end_time": str,
        "username": str,
        "state": WhiteListCheck.check_opr_state,
        "opr_type": WhiteListCheck.check_opr_type,
    }
    param_check(query_terms, must_dict={}, optional_dict=optional_dict)

    logs = core.find_logs_by_query_terms(query_terms, page)

    return logs


def find_system_logs_by_query_terms(query_terms, page=None):
    """
    :param page: 分页对象
    :param query_terms:
    :return: 查询到的系统日志列表
    """

    optional_dict = {
        "begin_time": str,
        "end_time": str,
        "username": str,
        "state": WhiteListCheck.check_opr_state,
        "action_type": StrCheck.check_action_type,
    }
    param_check(query_terms, must_dict={}, optional_dict=optional_dict)

    logs = core.find_system_logs_by_query_terms(query_terms, page)

    return logs


def find_alarm_logs_by_query_terms(query_terms, page=None):
    """
    :param page: 分页对象
    :param query_terms:
    :return: 查询到的警报日志列表
    """

    optional_dict = {
        "begin_time": str,
        "end_time": str,
        "query_box": str,
        "alarm_type": WhiteListCheck.check_alarm_type,
        "state": WhiteListCheck.check_opr_state,
    }
    param_check(query_terms, optional_dict=optional_dict)

    logs = core.find_alarm_logs_by_query_terms(query_terms, page)

    return logs


def update_logs_success_state(log_ids):

    conf_log_api.update_opr_logs_state(log_ids, OprLog.SUCCESS_STATE)


def del_opr_logs(opr_log_ids):
    """
    删除操作日志
    :param opr_log_ids:
    :return:
    """
    conf_log_api.del_opr_logs(opr_log_ids)


def del_system_logs(opr_log_ids):
    """
    删除系统日志
    :param opr_log_ids:
    :return:
    """
    conf_log_api.del_system_logs(opr_log_ids)


def del_alarm_logs(opr_log_ids):
    """
    删除警报日志
    :param opr_log_ids:
    :return:
    """
    conf_log_api.del_alarm_logs(opr_log_ids)