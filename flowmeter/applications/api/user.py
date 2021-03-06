# coding=utf-8

from flowmeter.common.api.validators import param_check
from flowmeter.common.api.validators import StrCheck, ListCheck, IntCheck, WhiteListCheck
from flowmeter.applications.core import user as user_core
from flowmeter.common.const import RoleType
from flowmeter.config.api import user as conf_user_api
from flowmeter.exceptions import NotUniqueException
from flowmeter.config.db.user_table import User
from flowmeter.common.api import file as file_api


def find_admins_by_query_terms(query_terms, page=None):
    """
    根据查询条件来查询管理员
    查询条件包括：管理员创建的时间，邮箱，手机，备注
    :param page: 分页对象
    :param query_terms: {
                            "begin_time": "管理员查询创建的开始时间",
                            "end_time": "管理员查询创建的结束时间",
                            "query_box": "网页查询框的值",
                        }
    :return: 查询到的管理员列表
    """

    optional_dict = {
        "begin_time": str,
        "end_time": str,
        "query_box": str,
    }
    param_check(query_terms, must_dict={}, optional_dict=optional_dict)

    admins, num = user_core.find_admins_by_query_terms(query_terms, page)

    return admins, num


def switch_admin_state_by_id(admin_id):

    user_core.switch_admin_state_by_id(admin_id)


def switch_manufacturer_state_by_id(manufacturer_id):

    user_core.switch_manufacturer_state_by_id(manufacturer_id)


def switch_dtu_user_state_by_id(dtu_user_id):

    user_core.switch_dtu_user_state_by_id(dtu_user_id)


def find_manufacturers_by_query_terms(query_terms, page=None):
    """
    根据查询条件来查询厂商
    查询条件包括：厂商创建的时间，邮箱，手机，备注
    :param page: 分页对象
    :param query_terms: {
                            "begin_time": "厂商查询创建的开始时间",
                            "end_time": "厂商查询创建的结束时间",
                            "query_box": "网页查询框的值",
                        }
    :return: 查询到的厂商列表
    """

    optional_dict = {
        "begin_time": str,
        "end_time": str,
        "query_box": str,
    }
    param_check(query_terms, must_dict={}, optional_dict=optional_dict)

    manufacturers, num = user_core.find_manufacturers_by_query_terms(query_terms, page)

    return manufacturers, num


def find_dtu_users_by_query_terms(query_terms, page=None):
    """
    根据查询条件来查询dtu用户
    查询条件包括：dtu用户创建的时间，邮箱，手机，备注
    :param page:
    :param query_terms: {
                            "begin_time": "dtu用户查询创建的开始时间",
                            "end_time": "dtu用户查询创建的结束时间",
                            "query_box": "网页查询框的值",
                        }
    :return: 查询到的dtu用户列表
    """
    optional_dict = {
        "begin_time": int,
        "end_time": int,
        "query_box": str,
    }
    param_check(query_terms, must_dict={}, optional_dict=optional_dict)

    dtu_users, num = user_core.find_dtu_users_by_query_terms(query_terms, page)

    return dtu_users, num


def find_dtu_users_of_man(man_id):
    return conf_user_api.find_dtu_users_of_man(man_id)


def create_admin(admin_info):
    """
    创建管理员账号
    :param admin_info:
    :return:
    """
    must_dict = {
        "name":  StrCheck.check_admin_name,
        "email": StrCheck.check_email,
        "phone": StrCheck.check_phone,
    }
    optional_dict = {
        "remark": StrCheck.check_remark
    }
    param_check(admin_info, must_dict, optional_dict)

    user_core.create_admin(admin_info)


def create_manufacturer(manufacturer_info):
    """
    创建厂商账号
    :param manufacturer_info:
    :return:
    """
    must_dict = {
        "name": StrCheck.check_admin_name,
        "email": StrCheck.check_email,
        "phone": StrCheck.check_phone,
    }
    optional_dict = {
        "remark": StrCheck.check_remark
    }
    param_check(manufacturer_info, must_dict, optional_dict)

    return user_core.create_manufacturer(manufacturer_info)


def create_dtu_user(dtu_user_info):
    """
    创建DTU用户账号
    :param dtu_user_info:
    :return:
    """
    must_dict = {
        "name": StrCheck.check_admin_name,
        "email": StrCheck.check_email,
        "phone": StrCheck.check_phone,
    }
    optional_dict = {
        "remark": StrCheck.check_remark
    }
    param_check(dtu_user_info, must_dict, optional_dict)

    user_core.create_dtu_user(dtu_user_info)


def edit_admin(admin_info):
    """
    编辑一个管理员
    :param admin_info:
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
    user_core.transfer_display_to_database(admin_info)
    param_check(admin_info, must_dict, optional_dict)

    user_core.edit_admin(admin_info)


def edit_manufacturer(manufacturer_info):
    """
    编辑厂商
    :param manufacturer_info:
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
    user_core.transfer_display_to_database(manufacturer_info)
    param_check(manufacturer_info, must_dict, optional_dict)

    user_core.edit_manufacturer(manufacturer_info)


def edit_dtu_user(dtu_user_info):
    """
    编辑一个DTU用户
    :param dtu_user_info:
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
    user_core.transfer_display_to_database(dtu_user_info)
    param_check(dtu_user_info, must_dict, optional_dict)

    user_core.edit_dtu_user(dtu_user_info)


def del_admin(admin_id):
    """
    删除一个管理员
    :param admin_id:
    :return:
    """

    IntCheck.check_is_int(admin_id)

    user_core.del_admin(admin_id)


def del_manufacturer(manufacturer_id):
    """
    删除一个厂商
    :param manufacturer_id:
    :return:
    """

    IntCheck.check_is_int(manufacturer_id)

    user_core.del_manufacturer(manufacturer_id)


def del_dtu_user(dtu_user_id):
    """
    删除一个DTU用户
    :param dtu_user_id:
    :return:
    """
    IntCheck.check_is_int(dtu_user_id)

    user_core.del_dtu_user(dtu_user_id)


def del_batch_admin(admin_ids):
    """
    批量删除管理员
    :param admin_ids: 管理员id列表
    :return:
    """

    ListCheck.check_is_int_list(admin_ids)

    user_core.del_batch_admin(admin_ids)


def del_batch_manufacturer(manufacturer_ids):
    """
    批量删除厂商
    :param manufacturer_ids: 厂商id列表
    :return:
    """

    ListCheck.check_is_int_list(manufacturer_ids)

    user_core.del_batch_manufacturer(manufacturer_ids)


def del_batch_dtu_user(dtu_user_ids):
    """
    批量删除DTU用户
    :param dtu_user_ids: DTU用户id列表
    :return:
    """

    ListCheck.check_is_int_list(dtu_user_ids)

    user_core.del_batch_dtu_user(dtu_user_ids)


def check_email_unique(email):
    """
    校验邮箱是否唯一
    :param email:
    :return:
    """
    try:
        conf_user_api.check_email_unique(email)
    except NotUniqueException:
        return False
    return True


def check_phone_unique(phone):
    """
    校验联系电话是否唯一
    :param phone:
    :return:
    """
    try:
        conf_user_api.check_phone_unique(phone)
    except NotUniqueException:
        return False
    return True


def check_name_unique(name):
    """
    校验名称是否唯一
    :param name:
    :return:
    """
    try:
        conf_user_api.check_name_unique(name)
    except NotUniqueException:
        return False
    return True


def admin_export(admin_ids, filename):
    """
    将管理员导出到文件中
    :param admin_ids:
    :param filename:
    :return:
    """
    StrCheck.check_not_null(filename)
    user_core.admin_export(admin_ids, filename)


def manufacturer_export(man_ids, filename):
    """
    将厂商列表导出到文件中
    :param filename:
    :return:
    """
    StrCheck.check_not_null(filename)
    user_core.manufacturer_export(man_ids, filename)


def dtu_user_export(dtu_user_ids, filename):
    """
    将DTU用户导出到文件中
    :param dtu_user_ids:
    :param filename:
    :return:
    """
    StrCheck.check_not_null(filename)
    user_core.dtu_user_export(dtu_user_ids, filename)


def admin_import(filename):
    """
    将文件中的管理员列表导入到系统中
    :param filename:
    :return:
    """
    StrCheck.check_not_null(filename)
    user_core.admin_import(filename)


def manufacturer_import(filename):
    """
    将文件中的厂商列表导入到系统中
    :param filename:
    :return:
    """
    StrCheck.check_not_null(filename)
    user_core.manufacturer_import(filename)


def dtu_user_import(filename):
    """
    将文件中的DTU用户列表导入到系统中
    :param filename:
    :return:
    """
    StrCheck.check_not_null(filename)
    user_core.dtu_user_import(filename)


def find_dtu_users_of_select_box(user):

    if user['role'] == RoleType.MANUFACTURER:
        dtu_users = conf_user_api.find_dtu_users_of_man(user['id'])
    else:
        dtu_users = conf_user_api.find_dtu_users_of_admin()

    return user_core.transfer_user_obj_to_dict(dtu_users)


def find_dtu_by_user_id(user_id):

    user = User.objects.prefetch_related('dtu_set').get(id=user_id)

    dtus = user.dtu_set.all()

    return user_core.transfer_user_obj_to_dict(dtus, ['id', 'dtu_no', 'remark'])


def find_dtu_users_by_man_id(man_id):

    return user_core.transfer_user_obj_to_dict(conf_user_api.find_dtu_users_of_man(man_id))

























