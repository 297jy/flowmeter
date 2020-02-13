# coding=utf-8

import json
import re
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from flowmeter.common.api import request as request_api
from flowmeter.views.common import Result
from flowmeter.applications.api.auth import is_action_allowed


class AuthMiddleware(MiddlewareMixin):
    """
    权限检查中间件，如果没有相应的权限就拦截
    """
    @staticmethod
    def __not_check_login(path):
        """
        不用检查登录的路径
        :param path:
        :return:
        """
        no_check_list = ['/login/', '/handler/login/', '/error/']

        for white in no_check_list:
            if re.match(white, path):
                return True

        return False

    @staticmethod
    def __not_check_auth(path, action):
        """
        不用检查权限的路径或行为
        :param path:
        :return:
        """
        path_white_list = ['/index/', '/welcome/', '/error/']
        action_white_list = ['file_upload']

        if action in action_white_list:
            return True

        for white in path_white_list:
            if re.match(white, path):
                return True

        return False

    def process_request(self, request):

        path = request_api.get_path(request)

        if AuthMiddleware.__not_check_login(path):
            return

        # 如果用户没登录，就先重定向到登录页
        if request_api.is_login(request) is False:
            # 如果是GET请求，则重定向
            if request.method == 'GET':
                return redirect('/login/')
            else:
                return HttpResponse(json.dumps(dict(Result.error('请先登录！'))))

        # 检查用户是否拥有执行当前action的权限
        action = request_api.get_action(request)

        if AuthMiddleware.__not_check_auth(path, action):
            return

        # 如过action为空，表示不需要检查权限
        if action is None:
            return
        user = request_api.get_user(request)
        if is_action_allowed(user, action) is False:
            if request.method == 'GET':
                return redirect('/error/403/')
            else:
                return HttpResponse(json.dumps(dict(Result.error('权限不足,请联系管理员添加权限！'))))

