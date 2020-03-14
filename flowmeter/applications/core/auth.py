# coding=utf-8

from operator import itemgetter
from flowmeter.config.db.auth_table import Auth
from flowmeter.config.api import user as conf_user_api, cache
from flowmeter.config.api import role as conf_role_api
from flowmeter.config.api import navigation_bar as conf_nav_bar_api
from flowmeter.config.api import flag as conf_flag_api
from flowmeter.exceptions import DoesNotExistException
from flowmeter.common.api.password import password_encryption
from flowmeter.common import const

import logging

logger = logging.getLogger('log')


def get_action_list():
    """
    获取全部的权限列表
    :return:
    """

    if cache.is_exists('action_list'):
        action_list = cache.get_list('action_list')
    else:
        # 如果缓存中不存在action_list，就从数据库中获取，并添加进缓存中
        auth_list = Auth.objects.all()
        action_list = [auth.permission_action for auth in auth_list]
        cache.set_list('action_list', action_list)

    return action_list


def get_action_bit_num(action):
    """
    获取action 在权限码中的位数
    :param action:
    :return:
    """
    action_list = get_action_list()
    action_bit_num = action_list.index(action)
    return action_bit_num


def find_user_by_account(account):
    """
    根据输入的账号来查找用户
    :param account:
    :return:
    """
    user = None
    try:
        user = conf_user_api.get_user_by_phone(account)
    except DoesNotExistException:
        pass

    try:
        user = conf_user_api.get_user_by_email(account)
    except DoesNotExistException:
        pass

    return user


def password_validate(input_password, really_password):

    password = password_encryption(input_password)
    if password == really_password:
        return True
    else:
        logger.warning('用户输入的密码错误！')
        return False


def find_nav_bars_by_role(role):
    """
    查询属于role角色的全部导航条
    :param role:
    :return:
    """

    auths = conf_role_api.get_auth_by_role(role)

    nav_bar_list = []
    for auth in auths:
        # 添加每个权限对应的导航栏
        nav_bars = conf_nav_bar_api.find_navigation_bars_by_auth_id(auth.id)
        nav_bar_list.extend(nav_bars)
    # 添加不需要权限的导航栏
    nav_bar_list.extend(conf_nav_bar_api.find_navigation_bars_by_auth_id())
    return nav_bar_list


def structure_nav_bars(nav_bars):
    """
    根据导航栏，构造出父导航栏与子导航栏之间的对应关系
    :param nav_bars:
    :return:
    """
    # 父导航条
    nav_bar_list = []
    # 子导航条
    child_nav_bar_list = []

    for nav in nav_bars:
        # 找到所有父导航条
        if nav.fid == -1:
            nav_dict = nav.get_dict()
            nav_dict['childs'] = []
            nav_bar_list.append(nav_dict)
        else:
            child_nav_bar_list.append(nav.get_dict())

    for nav in child_nav_bar_list:
        # 接着在列表中找到对应的父导航栏
        for f_nav in nav_bar_list:
            if f_nav['id'] == nav['fid']:
                f_nav['childs'].append(nav)
                break

    nav_bar_list = sorted(nav_bar_list, key=itemgetter('order'))

    return nav_bar_list


def check_user_is_forbidden(user):

    """
    检查用户的账号是否被禁用
    :param user:
    :return:
    """
    if user.state == const.UserStateType.FORBIDDEN_STATE:
        return True
    else:
        return False


def check_role_auth_change(now_auths, auth_ids):
    """
    检查角色权限是否发生改变
    :param now_auths:
    :param auth_ids:
    :return:
    """
    if len(now_auths) == len(auth_ids):
        for now_auth in now_auths:
            if str(now_auth.id) not in auth_ids:
                return True
    else:
        return True

    return False


def increase_role_version(role_name):
    """
    增加角色版本
    :param role_name:
    :return:
    """
    version = conf_flag_api.get_role_version(role_name)
    conf_flag_api.set_role_version(role_name, version + 1)





