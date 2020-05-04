# coding=utf-8

import redis

from flowmeter.common.common import deserialize_obj, serialize_obj

import logging
logger = logging.getLogger('log')

pool = redis.ConnectionPool(host='0.0.0.0', port=6379, max_connections=2000)

host = '0.0.0.0'


def is_exists(name):
    conn = redis.Redis(connection_pool=pool)
    timeout = conn.ttl(name)
    return timeout == 0


def get_int(name):
    """
    从redis中获取键名为name的整形值
    :param name:
    :return:
    """
    conn = redis.Redis(connection_pool=pool)
    val = conn.get(name)
    return int(val) if val else None


def set_int(name, val):
    conn = redis.Redis(connection_pool=pool)
    conn.set(name, val)


def get_list(name):
    conn = redis.Redis(connection_pool=pool)
    val = conn.get(name)
    return list(val) if val else []


def set_list(name, val_list):
    conn = redis.Redis(connection_pool=pool)
    conn.set(name, val_list)


def __is_obj(obj):
    """
    判断是否是对象
    :param obj:
    :return:
    """
    if obj is None:
        return obj

    base_type_list = [int, float, str, dict]
    for base in base_type_list:
        if isinstance(obj, base):
            return False
    return True


def add_sorted_set(name, obj, score):
    """
    添加到有序集合中
    :param obj: 要添加的对象
    :param name: 键名
    :parameter score 分数，分数越小越靠前
    :return:
    """

    if __is_obj(obj):
        obj = serialize_obj(obj)
    conn = redis.Redis(connection_pool=pool)
    conn.zadd(name, {obj: score})


def add_set(name, obj):
    # 如果是对象先序列化
    if __is_obj(obj):
        obj = serialize_obj(obj)
    conn = redis.Redis(connection_pool=pool)
    conn.sadd(name, obj)


def is_exists_set(name, obj):
    """
    判断元素是否存在集合中
    :param name:
    :param obj:
    :return:
    """
    # 如果是对象先序列化
    if __is_obj(obj):
        obj = serialize_obj(obj)
    conn = redis.Redis(connection_pool=pool)
    is_member = conn.sismember(name, obj)
    return True if is_member == 1 else False


def get_sorted_set_first(name, class_name=None):
    """
    获取有序集合的第一个元素
    :param class_name: 反序列化后的对象类名
    :param name:
    :return:
    """
    conn = redis.Redis(connection_pool=pool)
    res = conn.zrange(name, 0, 0)

    if len(res) == 0:
        return None

    val = res[0]
    return deserialize_obj(val, class_name) if __is_obj(val) else val


def get_zset_all_member(name, class_name=None):
    """
    获取有序集合的所有元素
    :param class_name: 反序列化后的对象类名
    :param name:
    :return:
    """
    conn = redis.Redis(connection_pool=pool)
    members = conn.zrange(name, 0, -1)
    res = []
    for member in members:
        res.append(deserialize_obj(member, class_name) if __is_obj(member) else member)

    return res


def set_obj(keyname, obj):
    obj = serialize_obj(obj)
    conn = redis.Redis(connection_pool=pool)
    conn.set(keyname, obj)


def get_obj(keyname, class_name=None):
    conn = redis.Redis(connection_pool=pool)
    obj = conn.get(keyname)
    obj = deserialize_obj(obj, class_name)
    return obj


def set_hash(name, key, val):
    conn = redis.Redis(connection_pool=pool)
    conn.hset(name, key, val)


def get_hash(name, key):
    conn = redis.Redis(connection_pool=pool)
    val = conn.hget(name, key)
    return val


def delete(keyname):
    conn = redis.Redis(connection_pool=pool)
    conn.delete(keyname)


def publish_message(channel_name, message):
    """
    发布消息
    :param message:
    :param channel_name: 通道名称
    :return:
    """
    conn = redis.Redis(connection_pool=pool)
    conn.publish(channel_name, message)


