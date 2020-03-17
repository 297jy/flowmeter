# coding=utf-8


def update_meter_state(old_state, new_state):
    """
    更新仪表状态
    :return:
    """
    update_flag = False

    # 遍历字典存在的属性
    for field, val in new_state.items():

        if getattr(old_state, field) != val:
            update_flag = True
            setattr(old_state, field, val)

    if update_flag:
        old_state.save()

