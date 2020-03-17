# coding=utf-8

from flowmeter.config.api import log as conf_log_api
from flowmeter.config.db.log_table import OprLog
from flowmeter.common.api.validators import param_check, WhiteListCheck
from flowmeter.applications.core import log as core


def find_logs_by_query_terms(query_terms, page=None):
    """
    根据查询条件来查询管理员
    查询条件包括：管理员创建的时间，邮箱，手机，备注
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


def update_logs_success_state(log_ids):

    conf_log_api.update_opr_logs_state(log_ids, OprLog.SUCCESS_STATE)