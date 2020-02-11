# coding=utf-8

import json
import re
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from flowmeter.common.api import request as request_api
from flowmeter.views.common import Result
from flowmeter.applications.api.auth import is_action_allowed


class ErrorHandlerMiddleware(MiddlewareMixin):
    """
    错误处理中间件
    """
    def process_exception(self, request, exception):
        print("这里是 Test2 的 process_exception")
        print(str(exception))
        result = Result.error(msg=str(exception))
        return HttpResponse(json.dumps(dict(result)))
