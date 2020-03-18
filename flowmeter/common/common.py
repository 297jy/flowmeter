# coding=utf-8

import json


class Page:
    """
    分页对象
    """
    def __init__(self, index, limit):
        # 页的索引
        self.index = index
        # 每页最多数据条数
        self.limit = limit


def extract_data_in_dict(data, keys):
    """
    从data字典提取keys列表中存在的键和相对应的值
    :param data: 字典
    :param keys: 需要提取的键列表
    :return:
    """
    res = {}
    for key in keys:
        val = data.get(key)
        # 只提取data中存在的值
        if val:
            res[key] = val
    return res


def get_allowed_action_of_role(role):
    """
    获取该角色所有能够执行的action
    :param role:
    :return:
    """
    authorities = role.authorities.all()

    action_list = []
    for auth in authorities:
        actions = auth.permission_action.split(';')
        action_list.extend(actions)
    return action_list


def get_page_data(datas, page, limit):
    """
    用于分页查询，获取某页的数据
    :param datas: 待分页的数据
    :param page: 当前页数
    :param limit: 每页最多显示的数据条数
    :return:
    """

    start_index = limit * (page - 1)
    end_index = limit * page

    return datas[start_index: end_index]


def transfer_hex_str(num):

    char_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    hex_str = ""

    if num < 0:
        num = num + 2 ** 32

    while num >= 16:
        digit = num % 16
        hex_str = char_dict.get(digit, str(digit)) + hex_str
        num //= 16
    hex_str = char_dict.get(num, str(num)) + hex_str
    hex_str = '0x' + hex_str
    return hex_str


def deserialize_obj(obj_str, class_name=None):
    """
    反序列化成简单对象
    :param obj_str 待反序列化的对象字符串
    :param class_name:
    :return: class_name为None时直接返回对象字典，否则返回指定对象
    """

    if obj_str is None:
        return None

    obj_dict = json.loads(obj_str)

    if class_name is None:
        return obj_dict

    obj = class_name()
    for key, val in obj_dict:
        setattr(obj, key, val)
    return obj


def serialize_obj(obj):
    """
    将对象序列化成字符串
    :param obj:
    :return:
    """
    obj_dict = dict(obj)
    obj_str = json.dumps(obj_dict)
    return obj_str


def get_obj_attr(obj, attr_name):
    """
    获得对象的某个属性
    :param obj:
    :param attr_name:
    :return:
    """
    attr_name += '.'
    while len(attr_name) > 0:
        index = attr_name.find('.')
        obj = getattr(obj, attr_name[0: index])
        attr_name = attr_name[index + 1: len(attr_name)]
    return obj


def get_att_name(att_name):
    """
    获取属性名
    :param att_name:
    :return:
    """
    att = att_name.replace(".", "_")
    return att


def transfer_obj_to_dict(objs, attribute_list, display_fun):
    """
    将对象转成字典
    :param display_fun: 将数据库值，转为显示给用户的值的处理函数
    :param objs: 对象列表
    :parameter attribute_list: 为None是默认获取全部属性，否则只获取attribute_list中出现的属性名
    :return:
    """
    dicts = []
    for obj in objs:

        obj_dict = {}
        for att in attribute_list:
            att_name = get_att_name(att)
            obj_dict[att_name] = get_obj_attr(obj, att)
        display_fun(obj_dict)

        dicts.append(obj_dict)
    return dicts
