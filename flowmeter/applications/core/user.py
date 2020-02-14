# coding=utf-8

import datetime
import time
from flowmeter.config.api import user as conf_user_api
from flowmeter.common.api.query import QueryTerms
from flowmeter.common import const
from flowmeter.common.api.excel import Excel
from flowmeter.common.api import password as password_api
from flowmeter import settings
from flowmeter.exceptions import NotUniqueException


def __transfer_user_obj_to_dict(users):
    """
    将用户对象转成字典
    :param users:
    :return:
    """
    user_dicts = []
    for user in users:
        user_dict = user.get_dict()
        __transfer_database_to_display(user_dict)
        del user_dict['actions']
        user_dicts.append(user_dict)
    return user_dicts


def __find_users_by_query_terms(query_terms):

    query_box = query_terms.get('query_box')
    begin_time = query_terms.get('begin_time')
    if begin_time:
        begin_time = datetime.datetime.strptime(begin_time, '%Y-%m-%d')
    end_time = query_terms.get('end_time')
    if end_time:
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')
    role = query_terms.get('role')

    # 构造查询框的查询条件
    query_box = QueryTerms.make_or_query_terms(name__icontains=query_box,
                                               email__icontains=query_box,
                                               phone__icontains=query_box,
                                               remark__icontains=query_box,
                                               create_time__gte=begin_time,
                                               create_time__lte=end_time)
    # 构造创建时间的查询条件
    query_time = QueryTerms.make_and_query_terms(create_time__gte=begin_time, create_time__lte=end_time)
    # 构造角色的查询条件
    query_role = QueryTerms.make_and_query_terms(role=role)

    users = conf_user_api.get_users(query_box.get_filters() & query_role.get_filters() & query_time.get_filters())

    return __transfer_user_obj_to_dict(users)


def __switch_user_state_by_id(user_id):

    conf_user_api.switch_user_state_by_id(user_id)


def switch_admin_state_by_id(admin_id):

    __switch_user_state_by_id(admin_id)


def switch_manufacturer_state_by_id(manufacturer_id):
    __switch_user_state_by_id(manufacturer_id)


def switch_dtu_user_state_by_id(dtu_user_id):
    __switch_user_state_by_id(dtu_user_id)


def __create_user(user_info):

    # 设置默认的用户密码
    user_info['password'] = password_api.password_encryption(const.DEFAULT_PASSWORD)

    conf_user_api.create_user(user_info)


def __edit_user(user_info):

    conf_user_api.edit_user(user_info)


def __del_user(user_id):

    conf_user_api.del_user(user_id)


def __del_batch_user(user_ids):

    conf_user_api.del_batch_user(user_ids)


def find_admins_by_query_terms(query_terms):
    query_terms['role'] = const.RoleType.ADMIN
    return __find_users_by_query_terms(query_terms)


def find_manufacturers_by_query_terms(query_terms):
    query_terms['role'] = const.RoleType.MANUFACTURER
    return __find_users_by_query_terms(query_terms)


def find_dtu_users_by_query_terms(query_terms):
    query_terms['role'] = const.RoleType.DTU_USER
    return __find_users_by_query_terms(query_terms)


def create_admin(admin_info):

    admin_info['role'] = const.RoleType.ADMIN
    __create_user(admin_info)


def create_manufacturer(manufacturer_info):

    manufacturer_info['role'] = const.RoleType.MANUFACTURER
    __create_user(manufacturer_info)


def create_dtu_user(dtu_user_info):

    dtu_user_info['role'] = const.RoleType.DTU_USER
    __create_user(dtu_user_info)


def edit_admin(admin_info):

    __edit_user(admin_info)


def edit_manufacturer(manufacturer_info):

    __edit_user(manufacturer_info)


def edit_dtu_user(dtu_user_info):

    __edit_user(dtu_user_info)


def del_admin(admin_id):

    __del_user(admin_id)


def del_manufacturer(manufacturer_id):

    __del_user(manufacturer_id)


def del_dtu_user(dtu_user_id):

    __del_user(dtu_user_id)


def del_batch_admin(admin_id):

    __del_batch_user(admin_id)


def del_batch_manufacturer(manufacturer_id):

    __del_batch_user(manufacturer_id)


def del_batch_dtu_user(dtu_user_id):

    __del_batch_user(dtu_user_id)


def __user_import(filename, prop_list, name_list):
    """
    从文件中批量导入用户
    :param filename: 文件名
    :param prop_list: 用户属性列表
    :param name_list: excel表格中的列名
    :return:
    """
    excel = Excel(prop_list=prop_list, name_list=name_list)
    excel.read(filename)
    users = excel.obj_dict_list
    for user in users:
        transfer_display_to_database(user)

    return users


def admin_import(filename):
    """
    从EXCEL中导入管理员
    :param filename:
    :return:
    """
    prop_list = ['name', 'phone', 'email', 'state', 'remark', 'create_time']
    name_list = ['用户名', '联系电话', '邮箱', '状态', '备注', '创建时间']
    admins = __user_import(filename, prop_list, name_list)
    for admin in admins:
        try:
            create_admin(admin)
        except NotUniqueException:
            pass


def manufacturer_import(filename):
    """
    从EXCEL中导入厂商
    :param filename:
    :return:
    """
    prop_list = ['name', 'phone', 'email', 'state', 'remark', 'create_time']
    name_list = ['厂商名称', '联系电话', '邮箱', '状态', '备注', '创建时间']
    manufacturers = __user_import(filename, prop_list, name_list)
    for manufacturer in manufacturers:
        create_manufacturer(manufacturer)


def dtu_user_import(filename):
    """
    从EXCEL中导入DTU用户
    :param filename:
    :return:
    """
    prop_list = ['name', 'phone', 'email', 'state', 'remark', 'create_time']
    name_list = ['姓名', '联系电话', '邮箱', '状态', '备注', '创建时间']
    dtu_users = __user_import(filename, prop_list, name_list)
    for dtu_user in dtu_users:
        create_dtu_user(dtu_user)


def __transfer_database_to_display(user_info):
    """
    将数据库中的值，转为前端显示的值
    :param user_info:
    :return:
    """
    # 格式化用户创建日期
    create_time = user_info.get('create_time')
    user_info['create_time'] = str(create_time.strftime(settings.DATETIME_FORMAT_STR))
    # 将英文的状态值，转化为中文
    state = user_info['state']
    if state == const.UserStateType.ENABLE_STATE:
        state = '启用'
    elif state == const.UserStateType.FORBIDDEN_STATE:
        state = '禁用'
    user_info['state'] = state


def transfer_display_to_database(user_info):
    """
    将前端显示的值，转为存储在数据库中的值
    :param user_info:
    :return:
    """

    # 将字符串转成日期时间戳
    if 'create_time' in user_info:
        create_time = user_info['create_time']
        user_info['create_time'] = \
            time.mktime(datetime.datetime.strptime(create_time, settings.DATETIME_FORMAT_STR).timetuple())

    # 将中文的状态值，转化为英文
    if 'state' in user_info:
        state = user_info['state']
        if state == '启用':
            state = const.UserStateType.ENABLE_STATE
        elif state == '禁用':
            state = const.UserStateType.FORBIDDEN_STATE
        user_info['state'] = state

    if 'phone' in user_info:
        phone = user_info['phone']
        if isinstance(phone, float) or isinstance(phone, int):
            user_info['phone'] = str(int(phone))

    if 'name' in user_info:
        name = user_info['name']
        if isinstance(name, float) or isinstance(name, int):
            user_info['name'] = str(int(name))


def __user_export(query_terms, sheet_name, filename, prop_list, name_list):
    """
    将用户列表导出到文件中
    """

    user_dict_list = __find_users_by_query_terms(query_terms)

    excel = Excel(prop_list=prop_list, name_list=name_list)
    excel.obj_dict_list = user_dict_list
    excel.write(filename, sheet_name)


def admin_export(query_terms, filename):
    """
    将管理员导出到文件中
    :param query_terms:
    :param filename:
    :return:
    """
    query_terms['role'] = const.RoleType.ADMIN
    prop_list = ['name', 'phone', 'email', 'state', 'remark', 'create_time']
    name_list = ['用户名', '联系电话', '邮箱', '状态', '备注', '创建时间']
    __user_export(query_terms, '管理员列表', filename, prop_list, name_list)


def manufacturer_export(query_terms, filename):
    """
    将厂商列表导出到文件中
    :param query_terms:
    :param filename:
    :return:
    """
    query_terms['role'] = const.RoleType.MANUFACTURER
    prop_list = ['name', 'phone', 'email', 'state', 'remark', 'create_time']
    name_list = ['厂商名称', '联系电话', '邮箱', '状态', '备注', '创建时间']
    __user_export(query_terms, '厂商列表', filename, prop_list, name_list)


def dtu_user_export(query_terms, filename):
    """
    将DTU用户导出到文件中
    :param query_terms:
    :param filename:
    :return:
    """
    query_terms['role'] = const.RoleType.DTU_USER
    prop_list = ['name', 'phone', 'email', 'state', 'remark', 'create_time']
    name_list = ['姓名', '联系电话', '邮箱', '状态', '备注', '创建时间']
    __user_export(query_terms, '用户列表', filename, prop_list, name_list)








