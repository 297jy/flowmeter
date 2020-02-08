# coding=utf-8
from flowmeter.config.db.role_table import Role
from flowmeter.config.db.role_table import RoleAuth
import logging

logger = logging.getLogger('log')


def get_role_by_name(name):
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
    role = get_role_by_name(role)
    authorities = role.authorities.all()
    return authorities



