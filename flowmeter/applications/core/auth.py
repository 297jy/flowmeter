# coding=utf-8

from flowmeter.config.db.auth_table import Auth
from flowmeter.config.api import cache
from flowmeter.config.api import user as conf_user_api
from flowmeter.config.api import role as conf_role_api
from flowmeter.config.api import navigation_bar as conf_nav_bar_api
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
        nav_bars = conf_nav_bar_api.find_navigation_bars_by_auth_id(auth.id)
        nav_bar_list.extend(nav_bars)

    return nav_bar_list


def structure_nav_bars(nav_bars):
    """
    根据导航栏，构造出父导航栏与子导航栏之间的对应关系
    :param nav_bars:
    :return:
    """
    nav_bar_list = []
    for nav in nav_bars:
        # 先找到父导航条
        if nav.fid == -1:
            nav_bar = nav.get_dict()

            # 找到该父导航栏的所有子导航栏
            child_nav_bar_list = []
            for child_nav in nav_bars:
                if child_nav.fid == nav.id:
                    child_nav_bar_list.append(child_nav.get_dict())
            if len(child_nav_bar_list) > 0:
                nav_bar['childs'] = child_nav_bar_list
            nav_bar_list.append(nav_bar)

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





