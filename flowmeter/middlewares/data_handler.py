# coding=utf-8

import json
import re
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from flowmeter.common.api import request as request_api
from flowmeter.views.common import Result
from flowmeter.applications.api.auth import is_action_allowed


class DataHandlerMiddleware(MiddlewareMixin):
    """
    数据转换中间件，将前端传递过来的字符串转成接口需要的类型
    """
    @staticmethod
    def __get_data_type(field_name):
        """
        获得字段真正的类型
        :return:
        """
        if field_name in ['id', 'meter_id', 'address', 'valve_state', 'dtu_no', 'manufacturer_id', 'dtu_user_id',
                          'dtu_id', 'recharge_state', 'money', 'region_id', 'user_id', 'total_num', 'valve_dtu_id',
                          'valve_address', 'state_id', 'admin_id']:
            return int

        if field_name in ['surplus_gas_limits', 'flow_ratio']:
            return float

        return None

    @staticmethod
    def __del_empty_field(params):
        """
        删除空字段
        :param params
        :return:
        """
        del_list = []
        for field, val in params.items():
            if val is None:
                del_list.append(field)
        # 删除空字段
        for field in del_list:
            del params[field]

    @staticmethod
    def __transfer_data_type(params):

        for field, val in params.items():
            data_type = DataHandlerMiddleware.__get_data_type(field)
            if data_type:
                params[field] = data_type(val)

    def process_request(self, request):

        params = request_api.get_param(request)

        # 删除空字段
        DataHandlerMiddleware.__del_empty_field(params)
        # 转换数据类型
        DataHandlerMiddleware.__transfer_data_type(params)

        request_api.set_param(request, params)



