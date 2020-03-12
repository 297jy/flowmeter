# coding=utf-8

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import auth as app_auth_api


class AuthActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_role': self.query_role,
            'edit_role': self.edit_role,
            'edit_role_auth': self.edit_role_auth,
        }
        super().__init__(action_dict)

    def query_role(self, request):

        roles = app_auth_api.query_all_role()

        return Result.success(data=roles, count=len(roles))

    def edit_role(self, request):

        param = request_api.get_param(request)
        app_auth_api.edit_role(param)

        return Result.success()

    def edit_role_auth(self, request):

        param = request_api.get_param(request)
        app_auth_api.edit_role_auth(param.get('role_name'), param.get('auth_ids'))

        return Result.success()


@xframe_options_sameorigin
def role_view(request):

    return render(request, 'auth/role-list.html', {})


@xframe_options_sameorigin
def auth_view(request):

    role_name = request.GET.get('name')

    role = app_auth_api.query_role_by_name(role_name)
    role_auth_ids = [auth.id for auth in role.authorities.all()]

    cates = app_auth_api.get_all_auth_category()
    auths = app_auth_api.get_all_auth()

    role_auths = []
    # 先遍历每个权限种类
    for cate in cates:
        cate_auths = []

        # 全选标志
        check_all = True

        for auth in auths:

            if auth['id'] in role_auth_ids:
                auth['checked'] = True
            else:
                # 如果有的没选中，则把全选标志置为False
                if auth['category_id'] == cate['id']:
                    check_all = False

            # 找到对应种类的权限
            if auth['category_id'] == cate['id']:
                cate_auths.append(auth)

        role_auth = {
            "name": cate['name'],
            "auths": cate_auths,
            "check_all": check_all,
        }

        role_auths.append(role_auth)

    return render(request, 'auth/role-auth.html', {"role_auths": role_auths, "name": role.name, "label": role.label})


def auth_handler(request):

    result = AuthActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))