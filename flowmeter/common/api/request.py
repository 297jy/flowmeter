# coding=utf-8

import json

from django.http import FileResponse
from flowmeter.common.common import Page
from flowmeter.config.api import flag as conf_flag_api


def get_user(request):
    """
    从Http request请求对象中获取已经登录的用户对象
    :param request:
    :return:
    """
    user = request.session.get('user')
    return user


def set_user(request, user):

    user = user.get_dict()
    user['role_version'] = conf_flag_api.get_role_version(user['role'])
    user.pop('create_time')
    request.session['user'] = user


def get_action(request):
    """
    从Http request请求对象中获取要执行的动作
    :param request:
    :return:
    """
    action = None
    if request.method == 'GET':
        action = request.GET.get('action')
    elif request.method == 'POST':
        action = request.POST.get('action')
    return str(action) if action else None


def get_param(request):
    """
    获取前端传递过来的请求参数
    :param request:
    :return:
    """
    param = '{}'
    if request.method == 'GET':
        param = request.GET.get('param', '{}')
    elif request.method == 'POST':
        param = request.POST.get('param', '{}')

    if isinstance(param, str):
        param = json.loads(param)

    # 删除csrf token
    if request.method == 'POST':
        if 'csrfmiddlewaretoken' in param.keys():
            del param['csrfmiddlewaretoken']
    return param


def get_path(request):
    """
    获取访问路径
    :param request:
    :return:
    """
    path = request.path_info

    return path


def is_login(request):

    if get_user(request):
        return True
    else:
        return False


def get_page(request):
    """
    获取分页对象
    :param request:
    :return:
    """
    if request.method == 'GET':
        index = request.GET.get('page')
        limit = request.GET.get('limit')
        if index is None or limit is None:
            return None
        else:
            return Page(int(index), int(limit))
    else:
        return None


def get_file(request):
    """
    获取文件对象
    :param request:
    :return:
    """
    file = None
    if request.method == 'POST':
        file = request.FILES.get('file')
    return file


def get_file_response(file, filename):

    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response
