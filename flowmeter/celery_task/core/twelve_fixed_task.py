# coding=utf-8


def calculator_week_flow_usage(datas):
    """
    计算仪表最近一周的流量使用情况
    :return:
    """
    # 如果系统开始统计的时间少于8天，就需要填充0
    zero_num = 8 - len(datas)
    usage_list = [i - i for i in range(0, zero_num)]

    for index in range(1, len(datas)):
        # 今天的总用气量，减去前一天的总用气量就是今天的新增加的用气量
        usage_list.append(datas[index] - datas[index - 1])

    return usage_list

