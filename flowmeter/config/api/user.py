# coding=utf-8

import copy
import datetime
from django.db import models
from django.db.models import Q
from django.db import transaction
from flowmeter.config.db import user_table
from flowmeter.config.db.user_table import User
from flowmeter.config.core import user as user_core
from flowmeter.config.api import role as role_api
from flowmeter.common.api.validators import StrCheck, WhiteListCheck, IntCheck, ListCheck
from flowmeter.common.api.validators import param_check
from flowmeter.common import const
from flowmeter.exceptions import NotUniqueException


def get_users(filters=None):
    """
    根据查询条件，查找用户
    :param filters:
    :return:
    """
    if filters:
        users = User.objects.filter(filters)
    else:
        users = User.objects.all()
    return users


def get_user_by_name(name):

    user = user_core.get_user({"name": name})

    return user


def get_user_by_phone(phone):

    user = user_core.get_user({"phone": phone})

    return user


def get_user_by_email(email):

    user = user_core.get_user({"email": email})

    return user


def create_user(user_info):
    """
    创建一个系统用户
    :param user_info: 系统用户的基本信息
    :return:
    """
    must_dict = {
        "name": StrCheck.check_admin_name,
        "email": StrCheck.check_email,
        "phone": StrCheck.check_phone,
        "password": StrCheck.check_password,
        "role": WhiteListCheck.check_role_type,
    }
    optional_dict = {
        "remark": StrCheck.check_remark,
        "state": WhiteListCheck.check_user_state_type,
        "create_time": float,
    }
    param_check(user_info, must_dict, optional_dict)

    check_user_unique(user_info)

    role = role_api.get_role(user_info.get('role'))
    user_info['role'] = role
    user_info['create_time'] = datetime.datetime.now()

    User.objects.create(**user_info)


def edit_user(user_info):
    """
    编辑一个系统用户
    :param user_info: 系统用户的基本信息
    :return:
    """
    must_dict = {
        "id": int,
        "name": StrCheck.check_admin_name,
        "email": StrCheck.check_email,
        "phone": StrCheck.check_phone,
        "state": WhiteListCheck.check_user_state_type,
    }
    optional_dict = {
        "remark": StrCheck.check_remark
    }
    param_check(user_info, must_dict, optional_dict)

    user = user_core.get_user({"id": user_info.get('id')})

    # 开启事务，当一下操作发生错误时，回滚
    with transaction.atomic():
        # 深拷贝 用户信息字典，防止编辑用户信息时产生的副作用
        user_info = copy.deepcopy(user_info)
        # 准备用户编辑需要的用户信息
        user_core.prepare_edit_user_info(user_info, user)
        # 先删除原来的用户，否则一下判断用户的唯一性可能会失败
        del_user(user_info.get('id'))
        # 检查用户信息的唯一性，比如：邮箱、电话、名称是否唯一
        check_user_unique(user_info)
        # 进行真正的编辑操作
        user_core.edit_user(user_info)
    
    
def del_user(user_id):
    """
    删除系统用户
    :param user_id: 
    :return: 
    """
    IntCheck.check_is_int(user_id)
    user_core.del_user(user_id)


def del_batch_user(user_ids):
    """
    批量删除系统用户
    :param user_ids:
    :return:
    """
    ListCheck.check_is_int_list(user_ids)
    user_core.del_batch_user(user_ids)


def check_user_unique(user_info):
    """
    校验新创建的用户是否唯一
    :param user_info:
    :return:
    """
    must_dict = {
        "email": StrCheck.check_email,
        "phone": StrCheck.check_phone,
    }
    param_check(user_info, must_dict, None, extra=True)

    check_email_unique(user_info.get('email'))
    check_phone_unique(user_info.get('phone'))


def check_email_unique(email):
    """
    校验邮箱是否唯一
    :param email:
    :return:
    """
    if not user_core.check_user_unique({'email': email}):
        raise NotUniqueException("邮箱：{}已存在！".format(email))


def check_phone_unique(phone):
    """
    校验联系电话是否唯一
    :param phone:
    :return:
    """
    if not user_core.check_user_unique({'phone': phone}):
        raise NotUniqueException("联系电话：{}已存在！".format(phone))


def check_name_unique(name):
    """
    校验名称是否唯一
    :param name:
    :return:
    """
    if not user_core.check_user_unique({'name': name}):
        raise NotUniqueException("名称：{}已存在！".format(name))

