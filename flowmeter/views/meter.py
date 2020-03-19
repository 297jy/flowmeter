# coding=utf-8

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import meter as app_meter_api


class MeterActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_meter': self.query_meter,
            'add_meter': self.add_meter,
            'query_state': self.query_meter_state,
            'del_batch_meter': self.del_batch_meter,
            "update_meter": self.update_meter,
            "update_valve_state": self.update_valve_state,
            "update_recharge_state": self.update_recharge_state,
            "reset_meter": self.reset_meter,
            "query_meter_data": self.query_meter_data,
            "update_flow_ratio": self.update_flow_ratio,
            "recharge_meter": self.recharge_meter,
            "update_valve_address": self.update_valve_address,
            "update_valve_dtu": self.update_valve_dtu,
        }
        super().__init__(action_dict)

    def query_meter(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        meters = app_meter_api.find_meter_by_query_terms(param, page)

        return Result.success(data=meters, count=len(meters))

    def add_meter(self, request):

        param = request_api.get_param(request)

        app_meter_api.add_meter(param)

        return Result.success()

    def query_meter_state(self, request):

        param = request_api.get_param(request)

        state = app_meter_api.find_meter_state_by_id(param['state_id'])

        return Result.success(data=state)

    def del_batch_meter(self, request):

        param = request_api.get_param(request)

        app_meter_api.del_batch_meter(param.get('meter_ids'))

        return Result.success()

    def update_meter(self, request):

        meter_info = request_api.get_param(request)
        app_meter_api.update_meter(meter_info)

        return Result.success()

    def update_valve_state(self, request):

        meter_info = request_api.get_param(request)
        app_meter_api.update_valve_state(meter_info, request_api.get_user(request))
        return Result.success()

    def update_valve_dtu(self, request):

        valve_info = request_api.get_param(request)

        app_meter_api.update_valve_dtu(valve_info)
        return Result.success()

    def update_recharge_state(self, request):

        meter_info = request_api.get_param(request)

        app_meter_api.update_recharge_state(meter_info, request_api.get_user(request))
        return Result.success()

    def update_valve_address(self, request):

        valve_info = request_api.get_param(request)
        app_meter_api.update_valve_address(valve_info)
        return Result.success()

    def update_flow_ratio(self, request):

        meter_info = request_api.get_param(request)
        app_meter_api.update_flow_ratio(meter_info, request_api.get_user(request))
        return Result.success()

    def recharge_meter(self, request):

        param = request_api.get_param(request)
        app_meter_api.recharge_meter(param['meter_ids'], param['money'], request_api.get_user(request))
        return Result.success()

    def reset_meter(self, request):

        meter_info = request_api.get_param(request)
        app_meter_api.reset_meter(meter_info, request_api.get_user(request))
        return Result.success()

    def query_meter_data(self, request):
        meter_info = request_api.get_param(request)
        app_meter_api.query_meter_data(meter_info, request_api.get_user(request))
        return Result.success()


@xframe_options_sameorigin
def meter_view(request):

    return render(request, 'meter/meter-list.html', {})


@xframe_options_sameorigin
def meter_state_view(request):
    meter_id = request.GET.get('meter_id')
    view_data = app_meter_api.get_meter_state_view_info(meter_id)
    return render(request, 'meter/meter-state.html', view_data)


@xframe_options_sameorigin
def meter_add(request):
    return render(request, 'meter/meter-add.html', {})


def meter_handler(request):
    result = MeterActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))
