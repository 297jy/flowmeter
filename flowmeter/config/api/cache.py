# coding=utf-8
from django_redis import get_redis_connection


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
