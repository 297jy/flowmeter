# coding=utf-8

import json

from flowmeter.views.websocket import clients
from flowmeter.config.api import cache as conf_cache_api


def add_unread_alarm_queue(user_id, data):
    """
    添加到缓存未阅读警报队列中
    :param user_id:
    :param data:
    :return:
    """
    unread_queue = conf_cache_api.get_hash('unread', user_id)
    if unread_queue is None:
        unread_queue = []
    unread_queue.append(data)
    conf_cache_api.set_hash('unread', user_id, unread_queue)

