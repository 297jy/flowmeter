# coding=utf-8

from flowmeter.config.db.role_table import Role
from flowmeter.config.db.role_table import RoleAuth
from flowmeter.config.core import role as core
from flowmeter.common.api.validators import StrCheck

import logging

logger = logging.getLogger('log')


def get_role(name):
    """
    根据角色名称来查找角色对象
    :param name:
    :return:
    """
    role = None
    try:
        role = Role.objects.get(name=name)
    except Role.DoesNotExist:
        logger.info('找不到名称为：{}，的角色对象'.format(name))
    return role


def add_auth_of_role(role, auth):
    """
    给角色添加权限
    :param role:
    :param auth:
    :return:
    """
    pass


def get_auth_by_role(role):
    """
    获取该角色的所有权限
    :param role:
    :return:
    """
    StrCheck.check_not_null(role)

    authorities = core.get_auth_by_role(role)
    return authorities


def get_allowed_actions_of_role_name(role_name):
    """
    获取该角色所有允许执行的action
    :param role_name: 角色名
    :return:
    """
    authorities = get_auth_by_role(role_name)

    action_list = []
    for auth in authorities:
        actions = auth.permission_action.split(';')
        action_list.extend(actions)
    return action_list


def get_all_role():
    """
    获取全部角色
    :return:
    """
    return Role.objects.all()



