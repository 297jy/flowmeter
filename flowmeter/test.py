# coding=utf-8

import os, django
"""
from flowmeter.applications.api import user as user_api
from flowmeter.config.api import cache
"""
"""
# 新建管理员，DTU用户，厂商
for index in range(4, 10):
    user_api.create_manufacturer({
        "name": "bbb" + str(index),
        "email": str(index) + "4477042621@qq.com",
        "phone": "4385059208" + str(index),
    })
    
user_api.create_dtu_user({
    "name": "陈伟强1",
    "email": "1347704261@qq.com",
    "phone": "13003950221",
})

user_api.create_manufacturer({
    "name": "陈伟强2",
    "email": "1347704263@qq.com",
    "phone": "13850563840",
})
"""

"""
def test_edit_admin():
    admins = user_api.find_admins_by_query_terms({'query_box': 'newabc4'})
    admin = admins[0]

    admin_dict = admin.get_dict()
    admin_dict['name'] = 'abc115'
    admin_dict.pop('remark')
    admin_dict.pop('create_time')

    user_api.edit_admin(admin_dict)


def test_del_file():
    os.remove('D://test.xls')


def test_chinese_len():

    val = "陈伟强a"

    for c in val:
        print(c)


def test_create_admin():

    user_api.create_admin({
        'name': '陈伟强',
        "email": '1347704262@qq.com',
        'phone': '13850592086',
    })


def test_zset_redis():

    cache.add('test', 1, 2)

"""


class A:
    def __init__(self):
        self.test = None
        pass


if __name__ == "__main__":

    # test_edit_admin()
    # test_del_file()
    # test_chinese_len()
    # test_create_admin()
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(user_api.check_email_unique('1347704262@qq.com'))
    # test_zset_redis()
    test = {
        "test": "test"
    }
    test.update({"a": "a"})
    print(test)
    a = A()
    getattr(a, 'test')
    pass