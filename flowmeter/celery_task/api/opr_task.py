# coding=utf-8
from celery import shared_task

from flowmeter.modbus.api import server as modbus_server_api
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.applications.api import meter as app_meter_api


# @shared_task
def query_meter_data():
    """
    定时查询目前所有在线DTU的所有仪表数据
    :return:
    """
    dtu_nos = modbus_server_api.get_all_online_dtu_no()
    for dtu_no in dtu_nos:
        meters = conf_dtu_api.find_meters_by_dtu_no(dtu_no)
        for meter in meters:
            app_meter_api.query_meter_data({'id': meter.id, 'address': meter.address, 'dtu_no': meter.dtu.dtu_no}, None,
                                           record_log=False)






