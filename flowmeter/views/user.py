# coding=utf-8

import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import user as app_user_api


class UserActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_admin': self.query_admin,
            'check_email_unique': self.check_email_unique,
            'check_phone_unique': self.check_phone_unique,
            'create_admin': self.create_admin,
            "edit_admin": self.edit_admin,
        }
        super().__init__(action_dict)

    def query_admin(self, request):

        param = request_api.get_param(request)

        admins = app_user_api.find_admins_by_query_terms(param)

        return Result.success(data=admins)

    def create_admin(self, request):

        admin_info = request_api.get_param(request)

        app_user_api.create_admin(admin_info)

        return Result.success()

    def edit_admin(self, request):

        admin_info = request_api.get_param(request)

        app_user_api.edit_admin(admin_info)

        return Result.success()

    def check_email_unique(self, request):

        param = request_api.get_param(request)
        email = param.get('email')
        is_unique = app_user_api.check_email_unique(email)

        return Result.success(data=is_unique)

    def check_phone_unique(self, request):
        param = request_api.get_param(request)
        phone = param.get('phone')

        is_unique = app_user_api.check_phone_unique(phone)

        return Result.success(data=is_unique)


@xframe_options_sameorigin
def admin_view(request):

    return render(request, 'admin/admin-list.html', {})


@xframe_options_sameorigin
def admin_add(request):

    return render(request, 'admin/admin-add.html', {})


def user_handler(request):

    result = UserActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))