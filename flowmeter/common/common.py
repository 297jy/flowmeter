# coding=utf-8


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
