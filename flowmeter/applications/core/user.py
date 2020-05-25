# coding=utf-8

import datetime
import time
from flowmeter.config.api import user as conf_user_api
from flowmeter.common.api.query import QueryTerms
from flowmeter.common import const
from flowmeter.common.api.excel import Excel, ExcelField
from flowmeter.common.api import password as password_api
from flowmeter import settings
from flowmeter.exceptions import NotUniqueException
from flowmeter.config.api import dtu_region as conf_region_api


def transfer_user_obj_to_dict(users, attribute_list=None):
    """
    将用户对象转成字典
    :param users:
    :parameter attribute_list: 为None是默认获取全部属性，否则只获取attribute_list中出现的属性名
    :return:
    """
    user_dicts = []
    for user in users:

        user_dict = dict(user)
        __transfer_database_to_display(user_dict)

        if 'actions' in user_dict.keys():
            # 避免导出用户权限
            del user_dict['actions']

        if attribute_list is not None:
            # 将要删除的属性列表
            del_attr_list = []
            for key in user_dict.keys():
                # 如果key不在属性列表中，则删除
                if key not in attribute_list:
                    del_attr_list.append(key)

            # 删除多余的属性
            for attr in del_attr_list:
                del user_dict[attr]

        user_dicts.append(user_dict)
    return user_dicts


def __find_users_by_query_terms(query_terms, page=None):

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

    users, num = conf_user_api.get_users(query_box.get_filters() & query_role.get_filters() & query_time.get_filters(), page)

    return transfer_user_obj_to_dict(users), num


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

    return conf_user_api.create_user(user_info)


def __edit_user(user_info):

    conf_user_api.edit_user(user_info)


def __del_user(user_id):

    conf_user_api.del_user(user_id)


def __del_batch_user(user_ids):

    conf_user_api.del_batch_user(user_ids)


def find_admins_by_query_terms(query_terms, page=None):
    query_terms['role'] = const.RoleType.ADMIN
    return __find_users_by_query_terms(query_terms, page)


def __find_user_by_ids(user_ids):

    users = conf_user_api.find_user_by_ids(user_ids)
    return transfer_user_obj_to_dict(users)


def find_admins_by_ids(admin_ids):
    return __find_user_by_ids(admin_ids)


def find_manufacturers_by_ids(man_ids):
    return __find_user_by_ids(man_ids)


def find_dtu_users_by_ids(dtu_user_ids):
    return __find_user_by_ids(dtu_user_ids)


def __get_manufacturer_dtu_region(manufacturer_id):
    """
    获得每个供气商的dtu区间
    :param manufacturer_id:
    :return:
    """
    regions = conf_region_api.find_region_by_manufacturer_id(manufacturer_id)
    total_num = 0
    used_num = 0
    # 统计所有区间的总DTU数量和已经使用的个数
    for region in regions:
        total_num += region.right - region.left + 1
        used_num += region.used_num

    return {
        "total_num": total_num,
        "used_num": used_num
    }


def find_manufacturers_by_query_terms(query_terms, page=None):
    query_terms['role'] = const.RoleType.MANUFACTURER
    manufacturers, num = __find_users_by_query_terms(query_terms, page)
    for man in manufacturers:
        region = __get_manufacturer_dtu_region(man['id'])
        man['dtu_total_num'] = region['total_num']
        man['dtu_used_num'] = region['used_num']
    return manufacturers, num


def find_dtu_users_by_query_terms(query_terms, page=None):
    query_terms['role'] = const.RoleType.DTU_USER
    return __find_users_by_query_terms(query_terms, page)


def create_admin(admin_info):

    admin_info['role'] = const.RoleType.ADMIN
    __create_user(admin_info)


def create_manufacturer(manufacturer_info):

    manufacturer_info['role'] = const.RoleType.MANUFACTURER
    return __create_user(manufacturer_info)


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


def __user_import(filename, excel_fields):
    """
    从文件中批量导入用户
    :param filename: 文件名
    :return:
    """
    excel = Excel(excel_fields)
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
    require_list = [True, True, True, True, True, False, True]
    excel_fields = []
    for index in range(0, len(prop_list)):
        if require_list[index]:
            excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))
    admins = __user_import(filename, excel_fields)
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
    name_list = ['供气商名称', '联系电话', '邮箱', '状态', '备注', '创建时间']
    require_list = [True, True, True, True, True, False, True]
    excel_fields = []
    for index in range(0, len(prop_list)):
        if require_list[index]:
            excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))
    manufacturers = __user_import(filename, excel_fields)
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
    require_list = [True, True, True, True, True, False, True]
    excel_fields = []
    for index in range(0, len(prop_list)):
        if require_list[index]:
            excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))
    dtu_users = __user_import(filename, excel_fields)
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
    if 'create_time' in user_info.keys():
        user_info['create_time'] = str(create_time.strftime(settings.DATETIME_FORMAT_STR))

    if 'state' in user_info.keys():

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


def __user_export(user_dict_list, sheet_name, filename, excel_fields):
    """
    将用户列表导出到文件中
    """

    excel = Excel(excel_fields)
    excel.obj_dict_list = user_dict_list
    excel.write(filename, sheet_name)


def admin_export(admin_ids, filename):
    """
    将管理员导出到文件中
    :param admin_ids:
    :param filename:
    :return:
    """
    prop_list = ['name', 'phone', 'email', 'state', 'remark', 'create_time']
    name_list = ['用户名', '联系电话', '邮箱', '状态', '备注', '创建时间']
    excel_fields = []
    for index in range(0, len(prop_list)):
        excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))
    admin_dicts = find_admins_by_ids(admin_ids)
    __user_export(admin_dicts, '管理员列表', filename, excel_fields)


def manufacturer_export(man_ids, filename):
    """
    将厂商列表导出到文件中
    :param man_ids:
    :param filename:
    :return:
    """
    prop_list = ['name', 'phone', 'email', 'state', 'dtu_used_num', 'dtu_total_num', 'remark', 'create_time']
    name_list = ['供气商名称', '联系电话', '邮箱', '状态', 'DTU数量', 'DTU最大数量',  '备注', '创建时间']

    excel_fields = []
    for index in range(0, len(prop_list)):
        excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))

    manufacturers = find_manufacturers_by_ids(man_ids)
    __user_export(manufacturers, '供气商列表', filename, excel_fields)
    

def dtu_user_export(dtu_user_ids, filename):
    """
    将DTU用户导出到文件中
    :param dtu_user_ids:
    :param filename:
    :return:
    """
    prop_list = ['name', 'phone', 'email', 'state', 'remark', 'create_time']
    name_list = ['姓名', '联系电话', '邮箱', '状态', '备注', '创建时间']
    excel_fields = []
    for index in range(0, len(prop_list)):
        excel_fields.append(ExcelField.require_field(prop_list[index], name_list[index]))
    dtu_users = find_dtu_users_by_ids(dtu_user_ids)
    __user_export(dtu_users, '用户列表', filename, excel_fields)








