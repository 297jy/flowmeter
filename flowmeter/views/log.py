# coding=utf-8

import json
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin

from flowmeter.settings import TMP_FILE_DIRECTORY_PATH
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import log as app_log_api
from flowmeter.applications.api import file as app_file_api


class LogActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_opr_log': self.query_opr_log,
            'del_opr_log': self.del_opr_log,
            'query_system_log': self.query_system_log,
            "del_system_log": self.del_system_log,
            'query_alarm_log': self.query_alarm_log,
            "del_alarm_log": self.del_alarm_log,
            'export_system_log': self.export_system_log,
            'export_alarm_log': self.export_alarm_log,
            'export_opr_log': self.export_opr_log,
            'read_alarm_log': self.read_alarm_log,
        }
        super().__init__(action_dict)

    def query_opr_log(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        logs = app_log_api.find_logs_by_query_terms(param, page)

        return Result.success(data=logs, count=len(logs))

    def query_system_log(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        logs = app_log_api.find_system_logs_by_query_terms(param, page)

        return Result.success(data=logs, count=len(logs))

    def query_alarm_log(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        logs = app_log_api.find_alarm_logs_by_query_terms(param, page)

        return Result.success(data=logs, count=len(logs))

    def del_system_log(self, request):

        param = request_api.get_param(request)

        app_log_api.del_system_logs(param['system_log_ids'])

        return Result.success()

    def del_alarm_log(self, request):

        param = request_api.get_param(request)

        app_log_api.del_opr_logs(param['alarm_log_ids'])

        return Result.success()

    def del_opr_log(self, request):

        param = request_api.get_param(request)

        app_log_api.del_opr_logs(param['opr_log_ids'])

        return Result.success()

    def export_system_log(self, request):

        param = request_api.get_param(request)
        name = app_file_api.generate_excel_file_name()
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_log_api.systemlog_export(param['systemlog_ids'], filename)

        return Result.success(data=name)

    def export_alarm_log(self, request):

        param = request_api.get_param(request)
        name = app_file_api.generate_excel_file_name()
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_log_api.alarmlog_export(param['alarmlog_ids'], filename)

        return Result.success(data=name)

    def export_opr_log(self, request):

        param = request_api.get_param(request)
        name = app_file_api.generate_excel_file_name()
        filename = os.path.join(TMP_FILE_DIRECTORY_PATH, name)

        app_log_api.oprlog_export(param['oprlog_ids'], filename)

        return Result.success(data=name)

    def read_alarm_log(self, request):

        param = request_api.get_param(request)

        app_log_api.read_alarm_log(param['alarm_id'])

        return Result.success()


@xframe_options_sameorigin
def opr_log_view(request):

    return render(request, 'log/opr_log-list.html', {})


@xframe_options_sameorigin
def system_log_view(request):

    return render(request, 'log/system_log-list.html', {})


@xframe_options_sameorigin
def alarm_log_view(request):

    return render(request, 'log/alarm_log-list.html', {})


def log_handler(request):

    result = LogActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))