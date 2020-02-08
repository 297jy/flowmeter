# coding=utf-8

import json

from django.shortcuts import render

from flowmeter.applications.api import auth as auth_api
from django.http import HttpResponse
from django.template import loader


def index_view(request):
    """
    主页视图
    :param request:
    :return:
    """

    nav_bars = auth_api.structure_nav_bars_by_role('admin')

    context = {'nav_bars': nav_bars}
    return render(request, 'index.html', context)
