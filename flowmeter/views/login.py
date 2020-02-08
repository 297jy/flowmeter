# coding=utf-8

import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from flowmeter.views.common import ActionHandlerBase
from flowmeter.views.common import Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api.auth import validate_and_get_user


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

        user = validate_and_get_user(account, password)
        # 如果校验通过
        if user is not None:
            request_api.set_user(request, user)
            return Result.success('登录成功！')
        else:
            return Result.error('账号不存在或密码错误！')


def login_view(request):

    if request_api.is_login(request):
        return redirect('/index/')
    return render(request, 'login.html', {})


def login_handler(request):

    result = LoginActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))
