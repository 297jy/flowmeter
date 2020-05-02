# coding=utf-8

import json
import time
import gevent
import redis
from flowmeter.common.api import request as request_api
from flowmeter.config.api import alarm_log_reader as conf_reader_api
from flowmeter.common.const import RoleType
from flowmeter.applications.api import log as app_log_api
from flowmeter.config.api import cache as conf_cache_api

import logging

logger = logging.getLogger('log')

try:
    import uwsgi
except ImportError as ex:
    logging.error(str(ex))
    pass


class ReturnFlag:
    def __init__(self):
        self.is_return = False


def __get_unread_alarm_dicts(user):
    alarms = conf_reader_api.get_user_unread_alarms(user['id'])
    alarm_dicts = []
    for alarm in alarms:
        alarm_log_dict = {'alarm_reader_id': alarm.id,
                          'msg': app_log_api.render_msg(alarm.alarm_log, RoleType.MANUFACTURER)}
        alarm_dicts.append(alarm_log_dict)
    return alarm_dicts


def __notice_user(redis_pubsub, flag):
    """通知用户消息"""
    while not flag.is_return:
        messages = redis_pubsub.listen()
        for msg in messages:
            if msg and msg['type'] == 'message':
                uwsgi.websocket_send(msg['data'])


def __check_live(conn, flag):
    """检查该websocket是否还生存"""

    # 重试次数
    __try_num = 3
    failed_num = 0
    while True:
        # 心跳包间隔90秒
        time.sleep(10)
        try:
            uwsgi.websocket_recv_nb()
            failed_num = 0
        except:
            failed_num += 1

        if failed_num > __try_num:
            logger.error("心跳包超过{}次无响应，断开websocket连接！".format(__try_num))
            flag.is_return = True
            __unregister_connect(conn)
            return


def link_view(request):
    if request_api.is_login(request):
        # 获取当前登录的用户

        user = request_api.get_user(request)
        conn = __register_connect(user['id'])

        uwsgi.websocket_handshake()
        # 发送所有用户未阅读的警报
        alarm_dicts = __get_unread_alarm_dicts(user)
        for alarm_dict in alarm_dicts:
            uwsgi.websocket_send(json.dumps(alarm_dict).encode('utf-8'))

        flag = ReturnFlag()
        # 创建协程
        gevent.joinall([
            gevent.spawn(__check_live, conn=conn, flag=flag),
            gevent.spawn(__notice_user, redis_pubsub=conn.pubsub(), flag=flag),
        ])


def __register_connect(user_id):
    """注册一个连接并返回一个redis连接"""
    conn = redis.Redis(connection_pool=conf_cache_api.pool)
    redis_pubsub = conn.pubsub()
    redis_pubsub.subscribe('alarm_user_id_{}'.format(user_id))
    return conn


def __unregister_connect(conn):
    """取消注册"""
    conn.close()
