# coding=utf-8

import json


def serialized_dict(val):
    """
    字典序列化
    :return:
    """
    res = json.dumps(val)
    return res


def deserialized_dict(val):
    """
    反序列化成字典
    :return:
    """
    res = json.loads(val)
    return res
