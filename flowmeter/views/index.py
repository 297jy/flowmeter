# coding=utf-8

from django.shortcuts import render

from flowmeter.applications.api import auth as auth_api
from flowmeter.common.api import request as request_api


def index_view(request):
    """
    主页视图
    :param request:
    :return:
    """
    nav_bars = auth_api.structure_nav_bars_by_role('admin')

    context = {'nav_bars': nav_bars, 'user': request_api.get_user(request)}
    return render(request, 'index.html', context)
