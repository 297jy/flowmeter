# coding=utf-8

from django.views.decorators.clickjacking import xframe_options_sameorigin
from flowmeter.applications.api import auth as auth_api
from django.http import HttpResponse
from django.template import loader


@xframe_options_sameorigin
def welcome_view(request):
    """
    欢迎页面
    :param request:
    :return:
    """

    template = loader.get_template('welcome.html')
    return HttpResponse(template.render({}))