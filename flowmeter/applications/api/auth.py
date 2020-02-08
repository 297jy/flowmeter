# coding=utf-8

from flowmeter.common.api.validators import StrCheck
from flowmeter.applications.core import auth as core
import logging

logger = logging.getLogger('log')


def is_action_allowed(user, action):
    """
    判断用户是否被允许执行某个动作
    :param user: 要执行动作的用户
    :param action: 当前正要执行的动作
    :return:
    """
    actions = [authority.permission_action for authority in user.role.authorities]

    if action in actions:
        allowed = True
    else:
        allowed = False
    return allowed


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


def user_validate(account, password):
    """
    用户校验
    :return:
    """
    StrCheck.check_is_str(account)
    StrCheck.check_is_str(password)

    user = core.find_user_by_account(account)

    if user is None:
        logger.warning('账号：{}，不存在！'.format(account))
        return False

    return core.password_validate(password, user.password)






