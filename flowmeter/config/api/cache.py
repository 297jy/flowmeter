# coding=utf-8

from django_redis import get_redis_connection
from flowmeter.exceptions import ParameterErrorException
from flowmeter.config.core import cache as core
from flowmeter.common.common import deserialize_obj, serialize_obj


def is_exists(name):
    conn = get_redis_connection('default')
    exists = conn.exists(name)
    return exists


def get_int(name):
    """
    从redis中获取键名为name的整形值
    :param name:
    :return:
    """
    conn = get_redis_connection('default')
    val = conn.get(name)
    return int(val) if val else None


def set_int(name, val):
    conn = get_redis_connection('default')
    conn.set(name, val)


def get_list(name):
    conn = get_redis_connection('default')
    val = conn.get(name)
    return list(val) if val else []


def set_list(name, val_list):
    conn = get_redis_connection('default')
    conn.set(name, val_list)


def add_sorted_set(name, obj, score):
    """
    添加到有序集合中
    :param obj: 要添加的对象
    :param name: 键名
    :parameter score 分数，分数越小越靠前
    :return:
    """

    obj = serialize_obj(obj)
    conn = get_redis_connection('default')
    conn.zadd(name, {obj: score})


def get_sorted_set_first(name, class_name=None):
    """
    获取有序集合的第一个元素
    :param class_name: 反序列化后的对象类名
    :param name:
    :return:
    """
    conn = get_redis_connection('default')
    res = conn.zrange(name, 0, 0)
    return deserialize_obj(res[0], class_name) if len(res) > 0 else None


def set_obj(keyname, obj):
    conn = get_redis_connection('default')
    obj = serialize_obj(obj)
    conn.set(keyname, obj)


def get_obj(keyname, class_name=None):
    conn = get_redis_connection('default')
    obj = conn.get(keyname)
    return deserialize_obj(obj, class_name) if obj else None


def delete(keyname):
    conn = get_redis_connection('default')
    conn.delete(keyname)


