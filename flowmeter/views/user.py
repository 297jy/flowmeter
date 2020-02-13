# coding=utf-8

import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import user as app_user_api
from flowmeter.common import common


class UserActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_admin': self.query_admin,
            'check_email_unique': self.check_email_unique,
            'check_phone_unique': self.check_phone_unique,
            'create_admin': self.create_admin,
            "edit_admin": self.edit_admin,
            "switch_admin_state": self.switch_admin_state,
            "del_batch_admin": self.del_batch_admin,
        }
        super().__init__(action_dict)

    def query_admin(self, request):

        param = request_api.get_param(request)

        all_admins = app_user_api.find_admins_by_query_terms(param)

        page = request_api.get_page_num(request)
        limit = request_api.get_page_limit(request)
        admins = common.get_page_data(all_admins, page, limit)

        return Result.success(data=admins, count=len(all_admins))

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

    def switch_admin_state(self, request):

        param = request_api.get_param(request)
        admin_id = param.get('admin_id')

        app_user_api.switch_admin_state_by_id(admin_id)

        return Result.success()

    def del_batch_admin(self, request):

        param = request_api.get_param(request)
        admin_ids = param.get('admin_ids')

        app_user_api.del_batch_admin(admin_ids)

        return Result.success()


@xframe_options_sameorigin
def admin_view(request):

    return render(request, 'admin/admin-list.html', {})


@xframe_options_sameorigin
def admin_add(request):

    return render(request, 'admin/admin-add.html', {})


@xframe_options_sameorigin
def admin_import(request):

    return render(request, 'admin/admin-import.html', {})


def user_handler(request):

    result = UserActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))