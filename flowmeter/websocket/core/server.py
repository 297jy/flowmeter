# encoding=utf-8


import redis
import json
import tornado.ioloop
import tornado.web
import tornado.websocket

import logging

from flowmeter.config.api import alarm_log_reader as conf_reader_api
from flowmeter.applications.api import log as app_log_api
from flowmeter.config.api import user as conf_user_api

logger = logging.getLogger('log')


def run():

    application = tornado.web.Application([
        (r"/websocket/", AlarmNoticeHandler),
    ],)
    application.listen(port=8004, address="0.0.0.0")
    tornado.ioloop.IOLoop.instance().start()


class AlarmNoticeHandler(tornado.websocket.WebSocketHandler):
    # 每个用户对应的连接
    user_id_connect_map = {}

    def check_origin(self, origin: str):
        return True

    def open(self):
        """
        客户端连接成功时，自动执行
        :return:
        """
        pass

    def on_message(self, message):
        """
        客户端连发送消息时，自动执行
        :param message:
        :return:
        """

        user_info = json.loads(message)
        user_id = user_info['user_id']
        opr_msg = user_info['opr_msg']
        AlarmNoticeHandler.user_id_connect_map[user_id] = self

        if opr_msg is False:
            alarm_dicts = AlarmNoticeHandler.__get_unread_alarm_dicts(user_id)
            for alarm_dict in alarm_dicts:
                self.write_message(json.dumps(alarm_dict))

    @staticmethod
    def __get_unread_alarm_dicts(user_id):

        alarms = conf_reader_api.get_user_unread_alarms(user_id)

        alarm_dicts = []
        for alarm in alarms:
            alarm_log_dict = {'type': 'alarm', 'alarm_reader_id': alarm.id,
                              'msg': app_log_api.render_alarm_msg(alarm.alarm_log, conf_user_api.get_user_role(user_id))}
            alarm_dicts.append(alarm_log_dict)
        return alarm_dicts

    def on_close(self):
        """
        客户端关闭连接时，自动执行
        :return:
        """
        del_key = None
        for key, val in AlarmNoticeHandler.user_id_connect_map.items():
            if val == self:
                del_key = key
                break
        if del_key is not None:
            del AlarmNoticeHandler.user_id_connect_map[del_key]

    @staticmethod
    def notice_user(user_id, alarm):
        user_id = str(user_id)
        if user_id in AlarmNoticeHandler.user_id_connect_map.keys():
            connect = AlarmNoticeHandler.user_id_connect_map[user_id]
            logger.info(alarm)
            connect.write_message(json.dumps(alarm))


def notice_user():
    """通知用户进程"""
    conn = redis.Redis(host='127.0.0.1', port=6379)
    pubsub = conn.pubsub()
    pubsub.subscribe('alarm_channel')
    while True:
        messages = pubsub.listen()
        for message in messages:
            if message and message['type'] == 'message':
                msg = json.loads(message['data'].decode('utf-8'))
                user_id = msg['user_id']
                alarm = msg['alarm']
                if alarm['type'] == 'opr_msg':
                    user_id = "opr_msg_{}".format(user_id)
                AlarmNoticeHandler.notice_user(user_id, alarm)


if __name__ == "__main__":
    run()

