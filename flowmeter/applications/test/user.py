# coding=utf-8

import time
import datetime
from django.test import TestCase
from flowmeter.applications.api import user as user_api
from flowmeter.config.db import role_table
from flowmeter.config.db import user_table
from flowmeter.common import const
from flowmeter.common.api.password import password_encryption
from flowmeter.common.api.file import del_file
from flowmeter.common.const import DEFAULT_PASSWORD
from flowmeter.exceptions import NotUniqueException, DoesNotExistException


class TestUserApi(TestCase):

    def setUp(self):
        # 初始化角色
        role_table.Role.objects.create(name=const.RoleType.ADMIN)
        role_table.Role.objects.create(name=const.RoleType.MANUFACTURER)
        role_table.Role.objects.create(name=const.RoleType.DTU_USER)

        # 初始化用户
        for num in range(0, 10):
            user_table.User.objects.create(name="aaa" + str(num),
                                           email=str(num) + "347704262@qq.com",
                                           phone="2385059208" + str(num),
                                           create_time=datetime.datetime(2020, 2, num+1),
                                           password=password_encryption(DEFAULT_PASSWORD),
                                           role_id=const.RoleType.ADMIN
                                           )

            user_table.User.objects.create(name="mmm" + str(num),
                                           email=str(num) + "347704261@qq.com",
                                           phone="1385059208" + str(num),
                                           create_time=datetime.datetime(2020, 2, num+1),
                                           password=password_encryption(DEFAULT_PASSWORD),
                                           role_id=const.RoleType.MANUFACTURER
                                           )

            user_table.User.objects.create(name="ddd" + str(num),
                                           email=str(num) + "347704263@qq.com",
                                           phone="3385059208" + str(num),
                                           create_time=datetime.datetime(2020, 2, num+1),
                                           password=password_encryption(DEFAULT_PASSWORD),
                                           role_id=const.RoleType.DTU_USER
                                           )

    def test_find_admins_by_query_terms(self):

        # 查询全部管理员
        admins = user_api.find_admins_by_query_terms({})
        self.assertEqual(len(admins), 10)

        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa'})
        self.assertEqual(len(admins), 10)

        admins = user_api.find_admins_by_query_terms({'query_box': 'bbb'})
        self.assertEqual(len(admins), 0)

        admins = user_api.find_admins_by_query_terms({'query_box': '13477'})
        self.assertEqual(len(admins), 1)

        admins = user_api.find_admins_by_query_terms({'query_box': '238'})
        self.assertEqual(len(admins), 10)

        admins = user_api.find_admins_by_query_terms(
            {'end_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple()))})
        self.assertEqual(len(admins), 3)

        admins = user_api.find_admins_by_query_terms(
            {'begin_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple()))})
        self.assertEqual(len(admins), 8)

        admins = user_api.find_admins_by_query_terms(
            {'begin_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple())),
             'end_time': int(time.mktime(datetime.datetime(2020, 2, 5).timetuple()))})
        self.assertEqual(len(admins), 3)

    def test_find_manufacturers_by_query_terms(self):

        manufacturers = user_api.find_manufacturers_by_query_terms({})
        self.assertEqual(len(manufacturers), 10)

        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm'})
        self.assertEqual(len(manufacturers), 10)

        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'bbb'})
        self.assertEqual(len(manufacturers), 0)

        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': '23477'})
        self.assertEqual(len(manufacturers), 1)

        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': '138'})
        self.assertEqual(len(manufacturers), 10)

        manufacturers = user_api.find_manufacturers_by_query_terms(
            {'end_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple()))})
        self.assertEqual(len(manufacturers), 3)

        manufacturers = user_api.find_manufacturers_by_query_terms(
            {'begin_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple()))})
        self.assertEqual(len(manufacturers), 8)

        manufacturers = user_api.find_manufacturers_by_query_terms(
            {'begin_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple())),
             'end_time': int(time.mktime(datetime.datetime(2020, 2, 5).timetuple()))})
        self.assertEqual(len(manufacturers), 3)

    def test_find_dtu_user_by_query_terms(self):
        dtu_users = user_api.find_dtu_users_by_query_terms({})
        self.assertEqual(len(dtu_users), 10)

        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd'})
        self.assertEqual(len(dtu_users), 10)

        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'bbb'})
        self.assertEqual(len(dtu_users), 0)

        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': '33477'})
        self.assertEqual(len(dtu_users), 1)

        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': '338'})
        self.assertEqual(len(dtu_users), 10)

        dtu_users = user_api.find_dtu_users_by_query_terms(
            {'end_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple()))})
        self.assertEqual(len(dtu_users), 3)

        dtu_users = user_api.find_dtu_users_by_query_terms(
            {'begin_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple()))})
        self.assertEqual(len(dtu_users), 8)

        dtu_users = user_api.find_dtu_users_by_query_terms(
            {'begin_time': int(time.mktime(datetime.datetime(2020, 2, 3).timetuple())),
             'end_time': int(time.mktime(datetime.datetime(2020, 2, 5).timetuple()))})
        self.assertEqual(len(dtu_users), 3)

    def test_edit_admin(self):

        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa0'})
        admin = admins[0]

        admin_dict = admin.get_dict()
        admin_dict['name'] = 'new' + admin.name
        admin_dict.pop('remark')
        admin_dict.pop('create_time')

        user_api.edit_admin(admin_dict)
        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa0'})
        admin = admins[0]
        self.assertEqual(admin.name, 'newaaa0')

        admin_dict['phone'] = '23850592088'
        error = False
        try:
            user_api.edit_admin(admin_dict)
        except NotUniqueException:
            error = True
        self.assertTrue(error)

        error = False
        admin_dict['id'] = 1000
        try:
            user_api.edit_admin(admin_dict)
        except DoesNotExistException:
            error = True
        self.assertTrue(error)

    def test_edit_manufacturer(self):

        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm0'})
        manufacturer = manufacturers[0]

        manufacturer_dict = manufacturer.get_dict()
        manufacturer_dict['name'] = 'new' + manufacturer.name
        manufacturer_dict.pop('remark')
        manufacturer_dict.pop('create_time')

        user_api.edit_manufacturer(manufacturer_dict)
        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm0'})
        manufacturer = manufacturers[0]
        self.assertEqual(manufacturer.name, 'newmmm0')

        manufacturer_dict['phone'] = '13850592084'
        error = False
        try:
            user_api.edit_manufacturer(manufacturer_dict)
        except NotUniqueException:
            error = True
        self.assertTrue(error)

        error = False
        manufacturer_dict['id'] = 1000
        try:
            user_api.edit_manufacturer(manufacturer_dict)
        except DoesNotExistException:
            error = True
        self.assertTrue(error)

    def test_edit_dtu_user(self):

        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd0'})
        dtu_user = dtu_users[0]

        dtu_user_dict = dtu_user.get_dict()
        dtu_user_dict['name'] = 'new' + dtu_user.name
        dtu_user_dict.pop('remark')
        dtu_user_dict.pop('create_time')

        user_api.edit_dtu_user(dtu_user_dict)
        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd0'})
        dtu_user = dtu_users[0]
        self.assertEqual(dtu_user.name, 'newddd0')

        dtu_user_dict['phone'] = '33850592085'
        error = False
        try:
            user_api.edit_dtu_user(dtu_user_dict)
        except NotUniqueException:
            error = True
        self.assertTrue(error)

        error = False
        dtu_user_dict['id'] = 1000
        try:
            user_api.edit_dtu_user(dtu_user_dict)
        except DoesNotExistException:
            error = True
        self.assertTrue(error)

    def test_del_admin(self):

        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa0'})
        admin = admins[0]
        user_api.del_admin(admin.id)
        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa0'})
        self.assertEqual(len(admins), 0)

    def test_del_manufacturer(self):

        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm0'})
        manufacturer = manufacturers[0]
        user_api.del_manufacturer(manufacturer.id)
        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm0'})
        self.assertEqual(len(manufacturers), 0)

    def test_del_dtu_user(self):

        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd0'})
        dtu_user = dtu_users[0]
        user_api.del_dtu_user(dtu_user.id)
        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd0'})
        self.assertEqual(len(dtu_users), 0)

    def test_del_batch_admin(self):

        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa'})
        admin_ids = [admin.id for admin in admins]
        user_api.del_batch_dtu_user(admin_ids)
        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa'})
        self.assertEqual(len(admins), 0)

    def test_del_batch_manufacturer(self):

        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm'})
        manufacturer_ids = [manufacturer.id for manufacturer in manufacturers]
        user_api.del_batch_manufacturer(manufacturer_ids)
        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm'})
        self.assertEqual(len(manufacturers), 0)

    def test_del_batch_dtu_user(self):

        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd'})
        dtu_user_ids = [dtu_user.id for dtu_user in dtu_users]
        user_api.del_batch_dtu_user(dtu_user_ids)
        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd'})
        self.assertEqual(len(dtu_users), 0)

    def test_admin_import_and_export(self):

        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa'})
        # 开始导出
        user_api.admin_export({'query_box': 'aaa'}, '/admin.xls')
        admin_ids = [admin.id for admin in admins]

        user_api.del_batch_admin(admin_ids)
        # 测试是否被删除成功
        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa'})
        self.assertEqual(len(admins), 0)

        # 开始导入
        user_api.admin_import('/admin.xls')
        # 测试是否导入成功
        admins = user_api.find_admins_by_query_terms({'query_box': 'aaa'})
        self.assertEqual(len(admins), 10)

        # 清理生成的额外文件
        del_file('/admin.xls')

    def test_manufacturer_import_and_export(self):

        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'aaa'})
        # 开始导出
        user_api.manufacturer_export({'query_box': 'mmm'}, '/manufacturer.xls')
        manufacturer_ids = [manufacturer.id for manufacturer in manufacturers]

        user_api.del_batch_manufacturer(manufacturer_ids)
        # 测试是否被删除成功
        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm'})
        self.assertEqual(len(manufacturers), 0)

        # 开始导入
        user_api.manufacturer_import('/manufacturer.xls')
        # 测试是否导入成功
        manufacturers = user_api.find_manufacturers_by_query_terms({'query_box': 'mmm'})
        self.assertEqual(len(manufacturers), 10)

        # 清理生成的额外文件
        del_file('/manufacturer.xls')

    def test_dtu_user_import_and_export(self):

        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd'})
        # 开始导出
        user_api.dtu_user_export({'query_box': 'ddd'}, '/dtu_user.xls')
        dtu_user_ids = [dtu_user.id for dtu_user in dtu_users]

        user_api.del_batch_dtu_user(dtu_user_ids)
        # 测试是否被删除成功
        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd'})
        self.assertEqual(len(dtu_users), 0)

        # 开始导入
        user_api.dtu_user_import('/dtu_user.xls')
        # 测试是否导入成功
        dtu_users = user_api.find_dtu_users_by_query_terms({'query_box': 'ddd'})
        self.assertEqual(len(dtu_users), 10)

        # 清理生成的额外文件
        del_file('/dtu_user.xls')




