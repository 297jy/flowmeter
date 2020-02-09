# coding=utf-8

import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from flowmeter.views.common import ActionHandlerBase
from flowmeter.views.common import Result
from flowmeter.common.api import request as request_api
from flowmeter.applications.api.auth import validate_and_get_user


def logout_view(request):

    request.session['user'] = None
    return redirect('/login/')
