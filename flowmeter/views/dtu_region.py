# coding=utf-8

import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.views.common import ActionHandlerBase, Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api import dtu_region as app_region_api


class DtuRegionActionHandler(ActionHandlerBase):

    def __init__(self):

        action_dict = {
            'query_dtu_region': self.query_dtu_region,
        }
        super().__init__(action_dict)

    def query_dtu_region(self, request):

        param = request_api.get_param(request)
        page = request_api.get_page(request)

        regions = app_region_api.find_regions_by_query_terms(param, page)

        return Result.success(data=regions, count=len(regions))


@xframe_options_sameorigin
def region_view(request):

    return render(request, 'dtu_region/dtu_region-list.html', {})


@xframe_options_sameorigin
def region_add(request):

    return render(request, 'dtu_region/dtu_region-list.html', {})


def region_handler(request):

    result = DtuRegionActionHandler().handle(request)
    return HttpResponse(json.dumps(dict(result)))