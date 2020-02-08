# coding=utf-8

import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from flowmeter.views.common import ActionHandlerBase
from flowmeter.views.common import Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api.auth import user_validate


class LoginActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'login': self.login
        }
        super().__init__(action_dict)

    def login(self, request):

        param = request_api.get_param(request)
        account = param.get('account', '')
        password = param.get('password', '')

        # 如果校验通过
        if user_validate(account, password):
            return Result.success({})
        else:
            return Result.error('账号不存在或密码错误！')


def login_view(request):

    return render(request, 'login.html', {})


def login_handler(request):

    result = LoginActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))
