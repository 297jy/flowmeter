# coding=utf-8

import os
import json
from flowmeter.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flowmeter.settings')


def __check_init():
    """
    检查是否已经初始化完毕
    :return:
    """
    flag_file_path = os.path.join(BASE_DIR, 'file', 'init.flag')
    if os.path.exists(flag_file_path):
        return True
    else:
        return False


def __init_authorities():
    """
    初始化用户可能拥有的所有权限
    :return:
    """
    # 权限分类和权限之间的映射关系字典
    cate_auth_map = {

        "管理员管理": [
            {
                "name": "添加管理员",
                "permission_action": "create_admin",
            },
            {
                "name": "编辑管理员",
                "permission_action": "edit_admin",
            },
            {
                "name": "删除管理员",
                "permission_action": "del_admin",
            },
            {
                "name": "导入管理员",
                "permission_action": "import_admin",
            },
            {
                "name": "导出管理员",
                "permission_action": "export_admin",
            },
            {
                "name": "查询管理员",
                "permission_action": "query_admin",
            },
        ],

        "厂商管理": [
            {
                "name": "添加厂商",
                "permission_action": "create_manufacturer",
            },
            {
                "name": "编辑厂商",
                "permission_action": "edit_manufacturer",
            },
            {
                "name": "删除厂商",
                "permission_action": "del_manufacturer",
            },
            {
                "name": "导入厂商",
                "permission_action": "import_manufacturer",
            },
            {
                "name": "导出厂商",
                "permission_action": "export_manufacturer",
            },
            {
                "name": "查询厂商",
                "permission_action": "query_manufacturer",
            },
        ],

        "DTU用户管理": [
            {
                "name": "添加DTU用户",
                "permission_action": "create_dtu_user",
            },
            {
                "name": "编辑DTU用户",
                "permission_action": "edit_dtu_user",
            },
            {
                "name": "删除DTU用户",
                "permission_action": "del_dtu_user",
            },
            {
                "name": "导入DTU用户",
                "permission_action": "import_dtu_user",
            },
            {
                "name": "导出DTU用户",
                "permission_action": "export_dtu_user",
            },
            {
                "name": "查询DTU用户",
                "permission_action": "query_dtu_user",
            },
        ],
        "日志管理": [
            {
                "name": "查询系统日志",
                "permission_action": "query_system_log",
            },
            {
                "name": "删除系统日志",
                "permission_action": "del_system_log",
            },
            {
                "name": "查询操作日志",
                "permission_action": "query_operator_log",
            },
            {
                "name": "删除系统日志",
                "permission_action": "del_operator_log",
            },
            {
                "name": "查询警报日志",
                "permission_action": "del_alarm_log",
            },
            {
                "name": "删除警报日志",
                "permission_action": "del_alarm_log",
            },
            {
                "name": "查询登录日志",
                "permission_action": "query_login_log",
            },
            {
                "name": "删除登录日志",
                "permission_action": "del_login_log",
            },
        ],

    }

    flag_file_path = os.path.join(BASE_DIR, 'file', 'category_auth_map')
    f = open(flag_file_path, 'wt')
    f.write(json.dumps(cate_auth_map))
    f.close()


def main():
    __init_authorities()


if __name__ == '__main__':
    main()