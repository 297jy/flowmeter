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

