# coding=utf-8

from flowmeter.config.api import cache
from flowmeter.config.db.flag_table import Flag


def get_role_version(role_name):
    """
    获取权限版本，用于判断是否要重新加载用户角色权限
    :return:
    """
    # 合成键值
    key = "{}_version".format(role_name)
    # 如果不存在缓存中，则从数据库中读取
    if cache.is_exists(key) is False:
        version = Flag.objects.get(name=key)
        version = int(version.val)
        cache.set_int(key, version)
    else:
        version = cache.get_int(key)
    return version


def set_role_version(role_name, new_version):
    """
    获取权限版本，用于判断是否要重新加载用户角色权限
    :return:
    """
    # 合成键值
    key = "{}_version".format(role_name)
    version = Flag.objects.get(name=key)
    version.val = str(new_version)
    version.save()
    # 更新缓存内容
    cache.set_int(key, new_version)
