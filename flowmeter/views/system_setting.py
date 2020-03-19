# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin

from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.applications.api import control_register as app_register_api
from flowmeter.applications.api import data_field as app_data_field_api
from flowmeter.applications.api import system_setting as app_setting_api
from flowmeter.common.api import request as request_api


class SystemSettingActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_control_register': self.query_control_register,
            'update_control_register': self.update_control_register,
            'query_data_field': self.query_data_field,
            'update_data_field': self.update_data_field,
            'query_configure': self.query_configure,
            'update_configure': self.update_configure,
        }
        super().__init__(action_dict)

    def query_control_register(self, request):

        all_registers = app_register_api.get_control_registers()

        return Result.success(data=all_registers, count=len(all_registers))

    def update_control_register(self, request):

        register_info = request_api.get_param(request)

        app_register_api.update_control_register(register_info)

        return Result.success()

    def query_data_field(self, request):

        all_fields = app_data_field_api.get_data_fields()

        return Result.success(data=all_fields, count=len(all_fields))

    def update_data_field(self, request):

        field_info = request_api.get_param(request)

        app_data_field_api.update_data_field(field_info)

        return Result.success()

    def query_configure(self, request):

        all_configures = app_setting_api.query_system_setting()
        return Result.success(data=all_configures, count=len(all_configures))

    def update_configure(self, request):

        conf_info = request_api.get_param(request)

        app_setting_api.update_system_setting(conf_info)

        return Result.success()


@xframe_options_sameorigin
def control_register_view(request):

    return render(request, 'system_setting/control-register-list.html', {})


@xframe_options_sameorigin
def data_field_view(request):

    return render(request, 'system_setting/data-field-list.html', {})


@xframe_options_sameorigin
def configure_view(request):

    return render(request, 'system_setting/configure-list.html', {})


def system_setting_handler(request):

    result = SystemSettingActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))