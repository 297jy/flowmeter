# coding=utf-8

import json

from flowmeter.celery import app
from flowmeter.common.const import RoleType
from flowmeter.views.websocket import clients
from flowmeter.config.api import user as conf_user_api
from flowmeter.celery_task.core import alarm_task as core


@app.task
def send_alarm(alarm_log):
    """
    向用户发送警报
    :return:
    """
    # 所有管理员都要推送警报
    admin_ids = conf_user_api.get_all_admin_ids()
    # 还需要向流量计的厂商推送警报
    man_id = alarm_log.meter.dtu.region.manufacturer.id
    # 还需要向DTU用户推送警报
    user_id = alarm_log.meter.dtu.user.id

    for admin_id in admin_ids:
        # 表明当前的用户在线，直接发送
        if admin_id in clients.keys():
            clients[admin_id].send(json.dumps({'alarm_id': alarm_log.id,
                                              'msg': core.render_msg(alarm_log, RoleType.ADMIN)}).encode('utf-8'))

    if man_id in clients.keys():
        clients[man_id].send(json.dumps({'alarm_id': alarm_log.id,
                                         'msg': core.render_msg(alarm_log, RoleType.MANUFACTURER)}).encode('utf-8'))

    if user_id in clients.keys():
        clients[user_id].send(json.dumps({'alarm_id': alarm_log.id,
                                         'msg': core.render_msg(alarm_log, RoleType.DTU_USER)}).encode('utf-8'))
