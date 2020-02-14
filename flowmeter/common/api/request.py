# coding=utf-8

import json

from django.http import FileResponse


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


def get_page_num(request):
    """
    获取当前表格的页数
    :param request:
    :return:
    """
    page_num = None
    if request.method == 'GET':
        page_num = int(request.GET.get('page', 0))
    return page_num


def get_page_limit(request):
    """
    获取每页最多显示的数据条数
    :param request:
    :return:
    """
    limit = None
    if request.method == 'GET':
        limit = int(request.GET.get('limit', 0))
    return limit


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

    print(filename)
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response
