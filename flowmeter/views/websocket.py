# coding=utf-8

import json
import time
import gevent
from flowmeter.common.api import request as request_api
from flowmeter.config.api import alarm_log_reader as conf_reader_api
from flowmeter.config.api import cache as conf_cache_api
from flowmeter.common.const import RoleType
from flowmeter.applications.api import log as app_log_api
from flowmeter.exceptions import ConnectCloseException

import logging

logger = logging.getLogger('log')

try:
    import uwsgi
except ImportError as ex:
    logging.error(str(ex))
    pass


def __get_unread_alarm_dicts(user):
    alarms = conf_reader_api.get_user_unread_alarms(user['id'])
    alarm_dicts = []
    for alarm in alarms:
        alarm_log_dict = {'alarm_reader_id': alarm.id,
                          'msg': app_log_api.render_msg(alarm.alarm_log, RoleType.MANUFACTURER)}
        alarm_dicts.append(alarm_log_dict)
    return alarm_dicts


def __notice_user(redis_pubsub):
    """通知用户消息"""
    while True:
        messages = redis_pubsub.listen()
        for msg in messages:
            if msg and msg['type'] == 'message':
                uwsgi.websocket_send(msg['data'])


def __check_live():
    """检查该websocket是否还生存"""
    # 重试次数
    __try_num = 3
    failed_num = 0
    while True:
        # 心跳包间隔90秒
        time.sleep(90)
        msg = uwsgi.websocket_recv_nb()
        if msg is None:
            failed_num += 1
        else:
            failed_num = 0

        if failed_num > __try_num:
            logger.error("心跳包超过{}次无响应，断开websocket连接！")
            raise ConnectCloseException("连接断开！")


def link_view(request):
    if request_api.is_login(request):
        # 获取当前登录的用户

        user = request_api.get_user(request)
        pubsub = __register_connect(user['id'])
        try:
            uwsgi.websocket_handshake()
            # 发送所有用户未阅读的警报
            alarm_dicts = __get_unread_alarm_dicts(user)
            for alarm_dict in alarm_dicts:
                uwsgi.websocket_send(json.dumps(alarm_dict).encode('utf-8'))

            # 创建协程
            gevent.joinall([
                gevent.spawn(__check_live),
                gevent.spawn(__notice_user, redis_pubsub=pubsub),
            ])
        finally:
            __unregister_connect(user['id'], pubsub)


def __register_connect(user_id):
    """注册一个连接并返回一个redis连接"""
    redis_pubsub = conf_cache_api.pubsub()
    redis_pubsub.subscribe('alarm_user_id_{}'.format(user_id))
    return redis_pubsub


def __unregister_connect(user_id, redis_pubsub):
    """取消注册"""
    redis_pubsub.unsubscribe('alarm_user_id_{}'.format(user_id))