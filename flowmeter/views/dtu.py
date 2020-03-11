# coding=utf-8

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import dtu as app_dtu_api


class DtuActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_dtu': self.query_dtu,
            "add_dtu": self.add_dtu,
            "update_dtu": self.update_dtu,
            "del_batch_dtu": self.del_batch_dtu,
        }
        super().__init__(action_dict)

    def query_dtu(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        if 'manufacturer_id' in param:
            if param['manufacturer_id']:
                param['manufacturer_id'] = int(param['manufacturer_id'])
            else:
                del param['manufacturer_id']

        if 'dtu_user_id' in param:
            if param['dtu_user_id']:
                param['dtu_user_id'] = int(param['dtu_user_id'])
            else:
                del param['dtu_user_id']

        dtus = app_dtu_api.find_dtu_by_query_terms(param, page)

        return Result.success(data=dtus, count=len(dtus))

    def add_dtu(self, request):

        param = request_api.get_param(request)

        param['region_id'] = int(param['region_id'])
        param['user_id'] = int(param['user_id'])
        if 'address' in param:
            param['address'] = int(param['address'])
        if 'valve_dtu' in param:
            param['valve_dtu'] = int(param['valve_dtu'])
        app_dtu_api.add_dtu(param)

        return Result.success()

    def update_dtu(self, request):

        param = request_api.get_param(request)

        param['id'] = int(param['id'])

        app_dtu_api.update_dtu_region(param)

        return Result.success()

    def del_batch_dtu(self, request):

        param = request_api.get_param(request)
        dtu_ids = param.get('dtu_ids')

        app_dtu_api.del_batch_dtu(dtu_ids)

        return Result.success()


@xframe_options_sameorigin
def dtu_view(request):

    return render(request, 'dtu/dtu-list.html', {})


@xframe_options_sameorigin
def dtu_add(request):

    return render(request, 'dtu/dtu-add.html', {})


def dtu_handler(request):

    result = DtuActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))