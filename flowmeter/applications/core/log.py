# coding=utf-8
import datetime

from django.db.models import Q

from flowmeter import settings
from flowmeter.common.api.excel import Excel, ExcelField
from flowmeter.common.api.query import QueryTerms
from flowmeter.common.const import RoleType
from flowmeter.config.db.log_table import OprLog, SystemLog, AlarmLog
from flowmeter.config.db.operator_table import Operator
from flowmeter.config.api import log as conf_log_api
from flowmeter.common.common import transfer_obj_to_dict


def transfer_opr_log_database_to_display(oprlog_info):
    """
    将数据库中的值，转为前端显示的值
    :return:
    """
    # 格式化日期
    opr_time = oprlog_info['opr_time']
    oprlog_info['opr_time'] = str(opr_time.strftime(settings.DATETIME_FORMAT_STR))

    if 'state' in oprlog_info.keys():
        # 将英文的状态值，转化为中文
        state = oprlog_info['state']
        if state == OprLog.WAITE_STATE:
            state = '等待'
        elif state == OprLog.SUCCESS_STATE:
            state = '成功'
        elif state == OprLog.ERROR_STATE:
            state = '失败'
        oprlog_info['state'] = state

    opr_type_map = {
        Operator.QUERY: "查询",
        Operator.RECHARGE: "充值",
        Operator.SET_FLOW_RATIO: "设置流量系数",
        Operator.CLOSE_RECHARGE: "关闭预充值功能",
        Operator.OPEN_RECHARGE: "打开预充值功能",
        Operator.CLOSE_VALVE: "关阀",
        Operator.OPEN_VALVE: "开阀",
        Operator.SET_METER_ADDRESS: "设置仪表物理地址",
        Operator.RESET: "重启仪表",
    }

    oprlog_info['opr_type'] = opr_type_map[oprlog_info['opr_type']]


def __transfer_system_log_database_to_display(systemlog_info):
    """
    将系统日志数据库中的值，转为前端显示的值
    :return:
    """
    # 格式化日期
    opr_time = systemlog_info['opr_time']
    systemlog_info['opr_time'] = str(opr_time.strftime(settings.DATETIME_FORMAT_STR))

    if 'state' in systemlog_info.keys():
        # 将英文的状态值，转化为中文
        state = systemlog_info['state']
        if state == SystemLog.SUCCESS_STATE:
            state = '成功'
        elif state == SystemLog.ERROR_STATE:
            state = '失败'
        systemlog_info['state'] = state


def __transfer_alarm_log_database_to_display(alarmlog_info):
    """
    将数据库中的值，转为前端显示的值
    :return:
    """
    # 格式化日期
    alarm_time = alarmlog_info['opr_time']
    alarmlog_info['opr_time'] = str(alarm_time.strftime(settings.DATETIME_FORMAT_STR))

    alarm_type_map = {
        AlarmLog.ALARM_VALVE_ERROR: "阀门异常警报",
        AlarmLog.ALARM_SENSOR_ERROR: "传感器异常警报",
        AlarmLog.ALARM_SUB_VALVE: "分阀警报",
        AlarmLog.ALARM_EXCEED_LIMIT: "越限警报",
    }

    alarmlog_info['alarm_type'] = alarm_type_map[alarmlog_info['alarm_type']]


def find_logs_by_query_terms(query_terms, user, page=None):
    name = query_terms.get('username')
    state = query_terms.get('state')
    opr_type = query_terms.get('opr_type')
    begin_time = query_terms.get('begin_time')
    if begin_time:
        begin_time = datetime.datetime.strptime(begin_time, '%Y-%m-%d')
    end_time = query_terms.get('end_time')
    if end_time:
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')

    # 构造创建时间的查询条件
    term_info = {
        'opr_user__name__icontains': name,
        'state': state,
        'opr_type': opr_type,
        'opr_time__gte': begin_time,
        'opr_time__lte': end_time,
    }
    if user['role'] == RoleType.MANUFACTURER:
        term_info['meter__dtu__region__manufacturer__id'] = user['id']
    elif user['role'] == RoleType.DTU_USER:
        term_info['opr_user__id'] = user['id']

    query_box = QueryTerms.make_and_query_terms(**term_info)

    logs = conf_log_api.find_opr_log(query_box.get_filters(), page)

    return transfer_obj_to_dict(logs, ['id', 'opr_user.name', 'opr_time', 'val', 'state', 'opr_type',
                                       'meter.dtu.dtu_no', 'meter.address'], transfer_opr_log_database_to_display)


def find_system_logs_by_query_terms(query_terms, user, page=None):
    query_box = query_terms.get('query_box')
    state = query_terms.get('state')
    begin_time = query_terms.get('begin_time')
    if begin_time:
        begin_time = datetime.datetime.strptime(begin_time, '%Y-%m-%d')
    end_time = query_terms.get('end_time')
    if end_time:
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')

    # 构造创建时间的查询条件
    term_info = {
        'state': state,
        'opr_time__gte': begin_time,
        'opr_time__lte': end_time,
    }
    if user['role'] != RoleType.ADMIN:
        term_info['opr_user__id'] = user['id']

    # 构造创建时间的查询条件
    query_and = QueryTerms.make_and_query_terms(**term_info)
    query_or = QueryTerms.make_or_query_terms(
        action_type__icontains=query_box,
        opr_user__name__icontains=query_box,
    )

    logs = conf_log_api.find_system_log(query_and.get_filters() & query_or.get_filters(), page)

    return transfer_obj_to_dict(logs, ['id', 'opr_user.name', 'opr_time', 'action_type', 'state'],
                                __transfer_system_log_database_to_display)


def find_alarm_logs_by_query_terms(query_terms, user, page=None):
    query_box = query_terms.get('query_box')
    state = query_terms.get('state')
    alarm_type = query_terms.get('alarm_type')
    begin_time = query_terms.get('begin_time')
    if begin_time:
        begin_time = datetime.datetime.strptime(begin_time, '%Y-%m-%d')
    end_time = query_terms.get('end_time')
    if end_time:
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')

    term_info = {
        'state': state,
        'opr_time__gte': begin_time,
        'opr_time__lte': end_time,
        'alarm_type': alarm_type,
    }
    if user['role'] == RoleType.MANUFACTURER:
        term_info['meter__dtu__region__manufacturer__id'] = user['id']
    elif user['role'] == RoleType.DTU_USER:
        term_info['meter__dtu__user__id'] = user['id']

    # 构造创建时间的查询条件
    query_or = QueryTerms.make_or_query_terms(
        meter__dtu__user__name__icontains=query_box,
        meter__dtu__region__manufacturer__name__icontains=query_box,
        meter__dtu__dtu_no__icontains=query_box,
        meter__address__icontains=query_box,
    )
    query_and = QueryTerms.make_and_query_terms(**term_info)

    logs = conf_log_api.find_alarm_log(query_or.get_filters() & query_and.get_filters(), page)

    return transfer_obj_to_dict(logs, ['id', 'meter.dtu.user.name', 'meter.dtu.region.manufacturer.name',
                                       'alarm_type', 'meter.address', 'meter.dtu.dtu_no', 'opr_time'],
                                __transfer_alarm_log_database_to_display)


def __log_export(log_dict_list, sheet_name, filename, excel_fields):
    """
    将日志导出到EXCEL文件中
    """

    excel = Excel(excel_fields)
    excel.obj_dict_list = log_dict_list
    excel.write(filename, sheet_name)


def systemlog_export(systemlog_ids, filename):
    """
    将系统日志导出到文件中
    :param systemlog_ids:
    :param filename:
    :return:
    """
    prop_list = ['opr_user_name', 'action_type', 'state', 'opr_time']
    name_list = ['操作人员名称', '行为', '状态', '操作日期']
    excel_fields = []
    for index in range(0, len(prop_list)):
        excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))

    logs = conf_log_api.find_system_log(Q(id__in=systemlog_ids))
    log_dicts = transfer_obj_to_dict(logs, ['id', 'opr_user.name', 'opr_time', 'action_type', 'state'],
                                     __transfer_system_log_database_to_display)

    __log_export(log_dicts, '系统日志列表', filename, excel_fields)


def alarmlog_export(alarmlog_ids, filename):
    """
    将警报日志导出到文件中
    :param alarmlog_ids:
    :param filename:
    :return:
    """
    prop_list = ['meter_dtu_user_name', 'meter_dtu_region_manufacturer_name', 'meter_dtu_dtu_no', 'meter_address',
                 'alarm_type', 'opr_time']
    name_list = ['仪表厂商名称', '仪表用户名称', '仪表DTU编号', '仪表物理地址', '警报类型', '警报时间']
    excel_fields = []
    for index in range(0, len(prop_list)):
        excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))

    logs = conf_log_api.find_alarm_log(Q(id__in=alarmlog_ids))
    log_dicts = transfer_obj_to_dict(logs, ['id', 'meter.dtu.user.name', 'meter.dtu.region.manufacturer.name',
                                            'alarm_type', 'meter.address', 'meter.dtu.dtu_no', 'opr_time'],
                                     __transfer_alarm_log_database_to_display)

    __log_export(log_dicts, '警报日志列表', filename, excel_fields)


def oprlog_export(oprlog_ids, filename):
    """
    将系统日志导出到文件中
    :param oprlog_ids:
    :param filename:
    :return:
    """
    prop_list = ['opr_user_name', 'meter_dtu_dtu_no', 'meter_address', 'opr_type', 'val', 'state', 'opr_time']
    name_list = ['操作人员名称', 'DTU编号', '仪表物理地址', '操作类型', '值', '状态', '操作日期']
    excel_fields = []
    for index in range(0, len(prop_list)):
        excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))

    logs = conf_log_api.find_opr_log(Q(id__in=oprlog_ids))
    log_dicts = transfer_obj_to_dict(logs, ['id', 'opr_user.name', 'opr_time', 'val', 'state', 'opr_type',
                                            'meter.dtu.dtu_no', 'meter.address'],
                                     transfer_opr_log_database_to_display)

    __log_export(log_dicts, '操作日志列表', filename, excel_fields)
