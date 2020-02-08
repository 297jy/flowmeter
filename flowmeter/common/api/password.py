# coding=utf-8

import hashlib
from flowmeter.common.core import password as password_core


def password_encryption(password):
    """
    将password进行md5加密
    :param password:
    :return:
    """
    salt = password_core.get_salt(password)

    obj = hashlib.md5(salt.encode('utf-8'))
    obj.update(password.encode('utf-8'))
    password = obj.hexdigest()

    return password
