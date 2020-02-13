# coding=utf-8

import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import user as app_user_api


class AdminActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_admin': self.query_admin
        }
        super().__init__(action_dict)

    def query_admin(self, request):

        param = request_api.get_param(request)

        admins = app_user_api.find_admins_by_query_terms({})

        return Result.success(data=admins)

    def add(self, request):

        admin_info = request_api.get_param(request)

        app_user_api.create_admin(admin_info)

        return Result.success()


@xframe_options_sameorigin
def admin_view(request):

    return render(request, 'admin/admin-list.html', {})


@xframe_options_sameorigin
def admin_add(request):

    return render(request, 'admin/admin-add.html', {})


def admin_handler(request):

    result = AdminActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))

