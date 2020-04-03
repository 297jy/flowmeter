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
    user = request_api.get_user(request)
    nav_bars = auth_api.structure_nav_bars_by_role(user['role'])

    context = {'nav_bars': nav_bars, 'user': user}
    return render(request, 'index.html', context)
