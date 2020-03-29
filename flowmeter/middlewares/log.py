# coding=utf-8

import datetime
import json
from django.utils.deprecation import MiddlewareMixin
from flowmeter.common.api import request as request_api
from flowmeter.config.db.log_table import SystemLog
from flowmeter.config.api import cache as conf_cache_api
from flowmeter.applications.api import log as app_log_api


class LogMiddleware(MiddlewareMixin):
    """
    日志中间件，主要用于记录系统日志
    """
    @staticmethod
    def __render_action_type_str(action, params):
        """
        渲染信息字符串
        :return:
        """
        log_dict_str = conf_cache_api.get_hash('log_configure', action)
        if log_dict_str is None:
            return None
        log_dict = json.loads(log_dict_str)

        # 获得行为类型模板
        msg = log_dict['msg']
        data_field = log_dict['data_field']
        # 渲染系统日志行为类型字段
        data_list = []
        for data in data_field:
            if data:
                data_list.append(data)
        return msg.format(*data_list)

    def process_request(self, request):

        action = request_api.get_action(request)

        if action is not None:
            params = request_api.get_param(request)
            action_type = LogMiddleware.__render_action_type_str(action, params)
            request_api.set_param(request, 'action_type', action_type)

    def process_response(self, request, response):

        action_type = request_api.get_action_type(request)

        if action_type is not None:
            user = request_api.get_user(request)
            log_dict = {
                'action_type': action_type,
                'opr_user_id': user['id'],
                'opr_time': datetime.datetime.now(),
                'state': SystemLog.SUCCESS_STATE
            }
            app_log_api.add_system_log(log_dict)

        return response

    def process_exception(self, request, exception):

        action_type = request_api.get_action_type(request)

        if action_type is not None:
            user = request_api.get_user(request)
            log_dict = {
                'action_type': action_type,
                'opr_user_id': user['id'],
                'opr_time': datetime.datetime.now(),
                'state': SystemLog.ERROR_STATE,
                'msg': str(exception)
            }
            request_api.set_param(request, 'action_type', None)
            app_log_api.add_system_log(log_dict)

        return None

