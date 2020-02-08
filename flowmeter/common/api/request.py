# coding=utf-8

import json


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
        param = request.GET.get('param', {})
    elif request.method == 'POST':
        param = request.POST.get('param', {})
    return json.loads(param)


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


