# coding=utf-8

from django.shortcuts import render

from flowmeter.applications.api import auth as auth_api
from flowmeter.config.api import configure as conf_configure_api
from flowmeter.common.api import request as request_api

import logging
logger = logging.getLogger('log')


def index_view(request):
    """
    主页视图
    :param request:
    :return:
    """
    user = request_api.get_user(request)
    nav_bars = auth_api.structure_nav_bars_by_role(user['role'])

    port = conf_configure_api.get_configure_by_name(conf_configure_api.get_websocket_port_name())
    context = {'nav_bars': nav_bars, 'user': user, 'websocket_port': int(port)}
    return render(request, 'index.html', context)
