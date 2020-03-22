# coding=utf-8
import json
import uuid

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from flowmeter.common.api import request as request_api
from dwebsocket import accept_websocket
from django_redis import get_redis_connection
from flowmeter.config.api import alarm_log_reader as conf_reader_api

from flowmeter.common.const import RoleType
from flowmeter.applications.api import log as app_log_api

import logging

logger = logging.getLogger('log')


def __get_unread_alarm_dicts(user):
    alarms = conf_reader_api.get_user_unread_alarms(user['id'])
    alarm_dicts = []
    for alarm in alarms:
        alarm_log_dict = {'alarm_reader_id': alarm.id,
                          'msg': app_log_api.render_msg(alarm.alarm_log, RoleType.MANUFACTURER)}
        alarm_dicts.append(alarm_log_dict)
    return alarm_dicts


@accept_websocket
def link_view(request):
    # 判断是不是ws请求
    if request.is_websocket():

        if request_api.is_login(request):
            # 获取当前登录的用户
            user = request_api.get_user(request)
            # 与前端的连接
            connect = request.websocket
            # 发送所有用户未阅读的警报
            alarm_dicts = __get_unread_alarm_dicts(user)
            for alarm_dict in alarm_dicts:
                connect.send(json.dumps(alarm_dict).encode('utf-8'))

            # 订阅属于这个用户的通道
            redis_cli = get_redis_connection('default')
            redis_pubsub = redis_cli.pubsub()
            redis_pubsub.subscribe('alarm_user_id_{}'.format(user['id']))

            while True:
                messages = redis_pubsub.listen()
                for msg in messages:
                    if msg and msg['type'] == 'message':
                        connect.send(msg['data'])