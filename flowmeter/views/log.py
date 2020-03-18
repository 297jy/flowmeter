# coding=utf-8

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import log as app_log_api


class LogActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_opr_log': self.query_opr_log,
            'del_opr_log': self.del_opr_log,
        }
        super().__init__(action_dict)

    def query_opr_log(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        logs = app_log_api.find_logs_by_query_terms(param, page)

        return Result.success(data=logs, count=len(logs))

    def del_opr_log(self, request):

        param = request_api.get_param(request)

        app_log_api.del_opr_logs(param['opr_log_ids'])

        return Result.success()


@xframe_options_sameorigin
def opr_log_view(request):

    return render(request, 'log/opr_log-list.html', {})


def log_handler(request):

    result = LogActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))