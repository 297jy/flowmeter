# coding=utf-8

from django_redis import get_redis_connection
from flowmeter.exceptions import ParameterErrorException
from flowmeter.config.core import cache as core
from flowmeter.common.common import deserialize_obj, serialize_obj


def is_exists(name):
    conn = get_redis_connection('default')
    timeout = conn.ttl(name)
    return timeout == 0


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

    conn = get_redis_connection('default')
    if __is_obj(obj):
        obj = serialize_obj(obj)
    conn.zadd(name, {obj: score})


def add_set(name, obj):
    conn = get_redis_connection('default')
    # 如果是对象先序列化
    if __is_obj(obj):
        obj = serialize_obj(obj)
    conn.sadd(name, obj)


def is_exists_set(name, obj):
    """
    判断元素是否存在集合中
    :param name:
    :param obj:
    :return:
    """
    conn = get_redis_connection('default')
    # 如果是对象先序列化
    if __is_obj(obj):
        obj = serialize_obj(obj)

    return True if conn.sismember(name, obj) == 1 else False


def get_sorted_set_first(name, class_name=None):
    """
    获取有序集合的第一个元素
    :param class_name: 反序列化后的对象类名
    :param name:
    :return:
    """
    conn = get_redis_connection('default')
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
    conn = get_redis_connection('default')
    members = conn.zrange(name, 0, -1)

    res = []
    for member in members:
        res.append(deserialize_obj(member, class_name) if __is_obj(member) else member)

    return res


def set_obj(keyname, obj):
    conn = get_redis_connection('default')
    obj = serialize_obj(obj)
    conn.set(keyname, obj)


def get_obj(keyname, class_name=None):
    conn = get_redis_connection('default')
    obj = conn.get(keyname)
    obj = deserialize_obj(obj, class_name)
    return obj


def set_hash(name, key, val):
    conn = get_redis_connection('default')
    conn.hset(name, key, val)


def get_hash(name, key):
    conn = get_redis_connection('default')
    val = conn.hget(name, key)
    return val


def delete(keyname):
    conn = get_redis_connection('default')
    conn.delete(keyname)


