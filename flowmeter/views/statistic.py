# coding=utf-8
import datetime

from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.common.api import request as request_api
from flowmeter.common.const import RoleType
from flowmeter.settings import DATETIME_FORMAT_STR
from flowmeter.applications.api import statistic as app_statistic_api


@xframe_options_sameorigin
def admin_statistic_view(request):
    """
    管理员统计数据
    :param request:
    :return:
    """
    now_time = datetime.datetime.now()

    user = request_api.get_user(request)
    if user['role'] == RoleType.ADMIN:
        user['role_label'] = '管理员'
    elif user['role'] == RoleType.DTU_USER:
        user['role_label'] = 'DTU用户'
    else:
        user['role_label'] = '供气商'

    context = {
        'user': request_api.get_user(request),
        'now_time': now_time.strftime(DATETIME_FORMAT_STR),
        'admin_total_num': app_statistic_api.get_total_admin_num(),
        'man_total_num': app_statistic_api.get_total_manufacturer_num(),
        'dtu_user_num': app_statistic_api.get_total_dtu_user_num(),
        'system_log_num': app_statistic_api.get_total_system_log_num(),
        'alarm_log_num': app_statistic_api.get_total_alarm_log_num(),
        'opr_log_num': app_statistic_api.get_total_opr_log_num(),
    }
    return render(request, 'statistic/admin_statistic.html', context)


@xframe_options_sameorigin
def manufacturer_statistic_view(request):
    """
    供气商统计数据
    :param request:
    :return:
    """
    now_time = datetime.datetime.now()

    user = request_api.get_user(request)
    if user['role'] == RoleType.ADMIN:
        user['role_label'] = '管理员'
    elif user['role'] == RoleType.DTU_USER:
        user['role_label'] = 'DTU用户'
    else:
        user['role_label'] = '供气商'

    context = {
        'user': request_api.get_user(request),
        'now_time': now_time.strftime(DATETIME_FORMAT_STR),
        'valve_alarm_num': app_statistic_api.get_valve_alarm_num_by_man_id(user['id']),
        'exceed_alarm_num': app_statistic_api.get_exceed_alarm_num_by_man_id(user['id']),
        'dtu_user_num': app_statistic_api.get_dtu_user_num_by_man_id(user['id']),
        'sub_valve_alarm_num': app_statistic_api.get_sub_valve_alarm_num_by_man_id(user['id']),
        'meter_num': app_statistic_api.get_meter_num_by_man_id(user['id']),
        'sensor_alarm_num': app_statistic_api.get_sensor_alarm_num_by_man_id(user['id']),
    }
    return render(request, 'statistic/manufacturer_statistic.html', context)


@xframe_options_sameorigin
def dtu_user_statistic_view(request):
    """
    DTU用户统计数据
    :param request:
    :return:
    """
    now_time = datetime.datetime.now()

    user = request_api.get_user(request)
    if user['role'] == RoleType.ADMIN:
        user['role_label'] = '管理员'
    elif user['role'] == RoleType.DTU_USER:
        user['role_label'] = 'DTU用户'
    else:
        user['role_label'] = '供气商'

    context = {
        'user': request_api.get_user(request),
        'now_time': now_time.strftime(DATETIME_FORMAT_STR),
        'valve_alarm_num': app_statistic_api.get_valve_alarm_num_by_dtu_user_id(user['id']),
        'exceed_alarm_num': app_statistic_api.get_exceed_alarm_num_by_dtu_user_id(user['id']),
        'sub_valve_alarm_num': app_statistic_api.get_sub_valve_alarm_num_by_man_id(user['id']),
        'meter_num': app_statistic_api.get_meter_num_by_dtu_user_id(user['id']),
        'sensor_alarm_num': app_statistic_api.get_sensor_alarm_num_by_dtu_user_id(user['id']),
    }
    return render(request, 'statistic/dtu_user_statistic.html', context)