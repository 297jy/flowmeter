# coding=utf-8

import datetime

from django.db.models import Count
from django.db.utils import IntegrityError
from flowmeter.common.const import RoleType
from flowmeter.config.db.user_table import User
from flowmeter.config.db.dtu_table import Dtu
from flowmeter.config.core import user as user_core
from flowmeter.config.api import role as role_api
from flowmeter.common.api.validators import StrCheck, WhiteListCheck, IntCheck, ListCheck
from flowmeter.common.api.validators import param_check
from flowmeter.exceptions import NotUniqueException


def get_users(filters=None, page=None):
    """
    根据查询条件，查找用户
    :param page: 分页对象
    :param filters:
    :return:
    """
    if page is None:
        if filters:
            users = User.objects.filter(filters)
        else:
            users = User.objects.all()
    else:
        start_index = page.limit * (page.index - 1)
        end_index = page.index * page.limit
        if filters:
            users = User.objects.filter(filters)[start_index: end_index]
        else:
            users = User.objects.all()[start_index: end_index]
    return users


def get_admin_num():
    admin_num = User.objects.filter(role=RoleType.ADMIN).count()
    return admin_num


def get_manufacturer_num():
    manufacturer_num = User.objects.filter(role=RoleType.MANUFACTURER).count()
    return manufacturer_num


def get_dtu_user_num():
    dtu_num = User.objects.filter(role=RoleType.DTU_USER).count()
    return dtu_num


def get_all_admin_ids():
    ids = User.objects.values('id').filter(role=RoleType.ADMIN)

    return [admin_id['id'] for admin_id in ids]


def get_user_by_id(user_id):

    user = user_core.get_user({'id': user_id})

    return user


def get_user_by_name(name):

    user = user_core.get_user({"name": name})

    return user


def get_dtu_user_num_by_man_id(man_id):

    num = Dtu.objects.filter(region__manufacturer__id=man_id).aggregate(Count('user'))

    return num['user__count']


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

    user = User.objects.create(**user_info)
    return user


def switch_user_state_by_id(user_id):

    user = user_core.get_user({'id': user_id})
    user_core.switch_user_state(user)


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
    try:
        user_core.edit_user(user, user_info)
    except IntegrityError as ex:
        msg = str(ex)
        if msg.find("phone") != -1:
            raise NotUniqueException("联系电话：{} 已存在，编辑失败！".format(user_info['phone']))
        else:
            raise NotUniqueException("邮箱：{} 已存在，编辑失败！".format(user_info['email']))
    
    
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
    # 如果要删除的用户为空，直接返回
    if len(user_ids) == 0:
        return
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


def find_user_by_ids(user_ids):
    users = User.objects.filter(id__in=user_ids)
    return users


def find_dtu_users_of_man(man_id):
    dtu_user_infos = Dtu.objects.filter(region__manufacturer__id=man_id).values('user__id', 'user__phone', 'user__name')\
        .distinct()
    dtu_users = []
    for dtu_user_info in dtu_user_infos:
        dtu_users.append({
            "id": dtu_user_info['user__id'],
            "name": dtu_user_info['user__name'],
            "phone": dtu_user_info['user__phone']
        })
    return dtu_users


def find_dtu_users_of_admin():
    dtu_user_infos = User.objects.filter(role=RoleType.DTU_USER).values('id', 'phone', 'name')\
        .distinct('id')
    return dtu_user_infos
