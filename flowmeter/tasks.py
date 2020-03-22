# coding=utf-8
from celery import shared_task

from flowmeter.modbus.api import server as modbus_server_api
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.applications.api import meter as app_meter_api
from flowmeter.modbus.api.server import FlowMeterClients

import logging

logger = logging.getLogger('log')


@shared_task
def query_meter_data():
    """
    定时查询目前所有在线DTU的所有仪表数据
    :return:
    """
    meters = conf_meter_api.find_meters()
    for meter in meters:
        app_meter_api.query_meter_data({'id': meter.id, 'address': meter.address, 'dtu_no': meter.dtu.dtu_no}, None,
                                       record_log=False)