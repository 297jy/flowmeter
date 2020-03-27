# coding=utf-8

from flowmeter.config.api import user as conf_user_api
from flowmeter.config.api import log as conf_log_api
from flowmeter.config.api import meter as conf_meter_api


def get_total_admin_num():
    """
    获得管理员总数
    :return:
    """
    admin_num = conf_user_api.get_admin_num()
    return admin_num


def get_total_manufacturer_num():
    """
    获得供气商总数
    :return:
    """
    manufacturer_num = conf_user_api.get_manufacturer_num()
    return manufacturer_num


def get_total_dtu_user_num():
    """
    获得DTU用户总数
    :return:
    """
    dtu_user_num = conf_user_api.get_dtu_user_num()
    return dtu_user_num


def get_total_opr_log_num():
    """
    获得操作日志总数
    :return:
    """
    log_num = conf_log_api.get_operator_log_total_num()
    return log_num


def get_total_alarm_log_num():
    """
    获得警报日志总数
    :return:
    """
    log_num = conf_log_api.get_alarm_log_total_num()
    return log_num


def get_total_system_log_num():
    """
    获得系统日志总数
    :return:
    """
    log_num = conf_log_api.get_system_log_total_num()
    return log_num


def get_dtu_user_num_by_man_id(man_id):

    num = conf_user_api.get_dtu_user_num_by_man_id(man_id)
    return num


def get_meter_num_by_man_id(man_id):
    num = conf_meter_api.get_total_meter_num_by_man_id(man_id)
    return num


def get_meter_num_by_dtu_user_id(dtu_user_id):
    num = conf_meter_api.get_total_meter_num_by_dtu_user_id(dtu_user_id)
    return num


def get_sub_valve_alarm_num_by_dtu_user_id(dtu_user_id):
    num = conf_log_api.get_sub_valve_alarm_num_by_dtu_user_id(dtu_user_id)
    return num


def get_sub_valve_alarm_num_by_man_id(man_id):
    num = conf_log_api.get_sub_valve_alarm_num_by_man_id(man_id)
    return num


def get_sensor_alarm_num_by_man_id(man_id):
    num = conf_log_api.get_sensor_alarm_num_by_man_id(man_id)
    return num


def get_sensor_alarm_num_by_dtu_user_id(dtu_user_id):
    num = conf_log_api.get_sensor_alarm_num_by_dtu_user_id(dtu_user_id)
    return num


def get_valve_alarm_num_by_man_id(man_id):
    num = conf_log_api.get_valve_alarm_num_by_man_id(man_id)
    return num


def get_valve_alarm_num_by_dtu_user_id(dtu_user_id):
    num = conf_log_api.get_valve_alarm_num_by_dtu_user_id(dtu_user_id)
    return num


def get_exceed_alarm_num_by_dtu_user_id(dtu_user_id):
    num = conf_log_api.get_exceed_alarm_num_by_dtu_user_id(dtu_user_id)
    return num


def get_exceed_alarm_num_by_man_id(man_id):
    num = conf_log_api.get_exceed_alarm_num_by_man_id(man_id)
    return num


