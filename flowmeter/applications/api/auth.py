# coding=utf-8
from django.db import transaction

from flowmeter.common.api.validators import StrCheck
from flowmeter.common.api.validators import param_check
from flowmeter.applications.core import auth as core
from flowmeter.exceptions import ForbiddenException
from flowmeter.config.api import role as conf_role_api
from flowmeter.config.api import auth_category as conf_category_api
from flowmeter.config.api import auth as conf_auth_api
from flowmeter.config.api import flag as conf_flag_api
from flowmeter.config.api import user as conf_user_api
from flowmeter.common.api import request as request_api

import logging

logger = logging.getLogger('log')


def __check_role_version_expire(user):
    now_version = conf_flag_api.get_role_version(user['role'])
    if user['role_version'] < now_version:
        return True
    return False


def is_action_allowed(request, action):
    """
    判断用户是否被允许执行某个动作
    :param request:
    :param action: 当前正要执行的动作
    :return:
    """
    auths = get_user_auths(request)
    if action in auths:
        allowed = True
    else:
        allowed = False
    return allowed


def get_user_auths(request):
    user = request_api.get_user(request)
    # 角色权限过期，就重新加载权限
    if __check_role_version_expire(user):
        user_obj = conf_user_api.get_user_by_id(user['id'])
        request_api.set_user(request, user_obj)
        user = request_api.get_user(request)
    return user.get('actions', [])


def structure_nav_bars_by_role(role):
    """
    根据角色构造出对应的一二级导航栏
    :param role:
    :return:
    """
    StrCheck.check_not_null(role)

    nav_bars = core.find_nav_bars_by_role(role)
    nav_bars = core.structure_nav_bars(nav_bars)

    return nav_bars


def validate_and_get_user(account, password):
    """
    用户校验，校验失败返回None,校验成功返回用户对象
    :return:
    """
    StrCheck.check_is_str(account)
    StrCheck.check_is_str(password)

    user = core.find_user_by_account(account)

    if user is None:
        logger.warning('账号：{}，不存在！'.format(account))
        return None

    # 检查用户是否被停用
    if core.check_user_is_forbidden(user):
        raise ForbiddenException("该账号已被禁用，请联系管理员！")

    # 如果密码验证通过
    if core.password_validate(password, user.password):
        return user
    else:
        return None


def query_all_role():

    roles = conf_role_api.get_all_role()
    role_dicts = []
    for r in roles:
        role_dicts.append(r.get_dict())

    return role_dicts


def query_role_by_name(role_name):

    role = conf_role_api.get_role(role_name)

    return role


def edit_role(role_info):

    must_dict = {
        "name": StrCheck.check_role_name,
        "label": StrCheck.check_role_name,
        "remark": StrCheck.check_remark
    }
    param_check(role_info, must_dict)

    role = conf_role_api.get_role(role_info['name'])

    role.label = role_info['label']
    role.remark = role_info['remark']

    role.save()


def get_all_auth_category():

    cates = conf_category_api.find_all_auth_category()
    category_list = []
    for cate in cates:
        category_list.append(cate.get_dict())

    return category_list


def get_all_auth():

    auths = conf_auth_api.find_all_auth()
    auth_list = []

    for auth in auths:
        auth_list.append(auth.get_dict())

    return auth_list


def edit_role_auth(role_name, auth_ids):

    role = conf_role_api.get_role(role_name)

    if core.check_role_auth_change(role.authorities.all(), auth_ids):

        auths = conf_auth_api.find_auths_by_id_list(auth_ids)

        with transaction.atomic():
            # 清空原有权限
            role.authorities.clear()
            # 添加到新的权限
            for auth in auths:
                role.authorities.add(auth)
            role.save()
            # 增加角色版本号
            core.increase_role_version(role_name)







