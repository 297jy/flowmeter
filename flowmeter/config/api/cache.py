# coding=utf-8

from django_redis import get_redis_connection
from flowmeter.exceptions import ParameterErrorException
from flowmeter.config.core import cache as core


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


def get_list(name):
    conn = get_redis_connection('default')
    val = conn.get(name)
    return list(val) if val else []


def set_list(name, val_list):
    conn = get_redis_connection('default')
    conn.set(name, val_list)


def add_sorted_set(name, val, score):
    """
    添加到有序集合中
    :param val: 要添加的值
    :param name: 键名
    :parameter score 分数，分数越小越靠前
    :return:
    """
    if isinstance(val, dict) is False:
        raise ParameterErrorException('val：{}，不是字典类型！'.format(val))

    val = core.serialized_dict(val)
    conn = get_redis_connection('default')
    conn.zadd(name, {val: score})


def get_sorted_set_first(name):
    """
    获取有序集合的第一个元素
    :param name:
    :return:
    """
    conn = get_redis_connection('default')
    res = conn.zrange(name, 0, 0)
    if len(res) > 0:
        return core.deserialized_dict(res[0])
    else:
        return None
