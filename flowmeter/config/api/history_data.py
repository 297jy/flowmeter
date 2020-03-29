# coding=utf-8

import datetime

from flowmeter.common.api.validators import param_check
from flowmeter.common.common import get_before_date
from flowmeter.config.db.history_data_table import MeterHistoryData


def add_meter_history_data(data_info):
    must_dict = {
        "meter_id": int,
        "data": float,
        "time": datetime.date
    }
    param_check(data_info, must_dict)
    MeterHistoryData.objects.create(**data_info)


def find_recent_week_all_meters_history_data():
    """
    获取所有仪表最近一周的，仪表历史数据
    :return:
    """
    # 获得一周前的日期
    week_before_date = get_before_date(days=7)

    datas = MeterHistoryData.objects.filter(time__gte=week_before_date, time__lte=datetime.datetime.now().date())\
        .values('data', 'meter__id')
    res = {}
    for data in datas:
        data_list = res.get(data['meter__id'], [])
        data_list.append(data['data'])
        res[data['meter__id']] = data_list

    return res

