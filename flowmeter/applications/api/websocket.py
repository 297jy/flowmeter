# coding=utf-8

import json

from flowmeter.celery import app
from flowmeter.views.websocket import clients


@app.task
def send_data(user_ids, data):
    """
    向客户端发送数据
    :param user_ids:
    :param data:
    :return:
    """
    # 遍历需要推送消息的用户
    for user_id in user_ids:
        # 表明当前的用户在线，直接发送
        if user_id in clients.keys():
            clients[user_id].send(json.dumps(data).encode('utf-8'))
