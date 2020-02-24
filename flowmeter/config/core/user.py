# coding=utf-8
from flowmeter.config.db.user_table import User
from flowmeter.common import const
from flowmeter.common.api import query
from flowmeter.exceptions import DoesNotExistException
import logging

logger = logging.getLogger('log')


def __get_check_unique_fields_by_role(role):
    if role == const.RoleType.ADMIN:
        return ['email', 'phone']
    elif role == const.RoleType.MANUFACTURER:
        return ['email', 'phone', 'name']
    elif role == const.RoleType.DTU_USER:
        return ['email', 'phone']
    else:
        return []


def check_user_unique(filters):
    """
    判断是否存在符合条件的系统用户
    :param filters: 过滤条件
    :return:
    """
    try:
        User.objects.get(**filters)
    except User.DoesNotExist:
        return True
    except User.MultipleObjectsReturned:
        return False
    return False


def prepare_edit_user_info(user_info, user):
    """
    用户编辑操作开始前的准备工作
    :param user_info: 用户信息字典
    :param user: 用户对象
    :return:
    """
    user_info['password'] = user.password
    user_info['create_time'] = user.create_time
    user_info['role_id'] = user.role.name


def get_user(user_info):
    """
    获取一个用户对象
    :param user_info: 用户查询信息
    :return:
    """
    try:
        user = User.objects.get(**user_info)
        return user
    except User.DoesNotExist:
        raise DoesNotExistException('该用户不存在！')


def edit_user(user, user_info):
    """
    编辑系统用户
    :param user:
    :param user_info: 系统用户的基本信息
    :return:
    """
    for prop, val in user_info.items():
        setattr(user, prop, val)
    user.save()


def switch_user_state(user):
    """
    转换用户的状态
    :param user:
    :return:
    """
    if user.state == const.UserStateType.ENABLE_STATE:
        user.state = const.UserStateType.FORBIDDEN_STATE
    else:
        user.state = const.UserStateType.ENABLE_STATE

    user.save()


def del_user(user_id):
    """
    删除系统用户
    :param user_id:
    :return:
    """
    try:
        user = User.objects.get(id=user_id)
        user.delete()
    except Exception as ex:
        logger.warning('删除用户发生错误：{}'.format(ex))


def del_batch_user(user_ids):
    """
    批量删除用户
    :param user_ids:
    :return:
    """
    query_terms = query.QueryTerms.make_or_query_terms(**{'id': user_ids})

    User.objects.filter(query_terms.get_filters()).delete()


