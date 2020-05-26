# coding=utf-8

import datetime
import json

from flowmeter.common.api.validators import param_check
from flowmeter.common.common import get_before_date
from flowmeter.config.db.history_data_table import MeterHistoryData
from flowmeter.config.api import cache as conf_cache_api

import logging
LOG = logging.getLogger('log')


def add_meter_history_data(data_info):
    must_dict = {
        "meter_id": int,
        "data": float,
        "time": datetime.date
    }
    param_check(data_info, must_dict)
    MeterHistoryData.objects.create(**data_info)


def add_batch_meter_history_data(data_infos):
    """
    批量添加流量计历史数据
    :param data_infos:
    :return:
    """
    history_datas = []
    for data_info in data_infos:
        must_dict = {
            "meter_id": int,
            "data": float,
            "time": datetime.date
        }
        param_check(data_info, must_dict)
        history_datas.append(MeterHistoryData(**data_info))

    MeterHistoryData.objects.bulk_create(history_datas)


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


def sync_meter_history_data():
    """
    同步所有仪表的所有历史数据
    :return:
    """
    now_date = datetime.datetime.now().date()
    month_begin_date = datetime.datetime(year=now_date.year-1, month=now_date.month, day=1).date()
    datas = MeterHistoryData.objects.all().order_by('time').values('data', 'meter__id', 'time')
    year_data_map = {}
    month_data_map = {}
    flow_data_map = {}

    for meter_data in datas:
        meter_id = meter_data['meter__id']
        # 统计最近几年
        year_str = meter_data['time'].strftime('%Y年')
        year_map = year_data_map.get(meter_id, {})
        year_map[year_str] = year_map.get(year_str, 0) + meter_data['data']
        year_data_map[meter_id] = year_map

        # 统计最近12个月
        if month_begin_date <= meter_data['time']:
            month_str = meter_data['time'].strftime('%Y年%m月')
            month_map = month_data_map.get(meter_id, {})
            month_map[month_str] = month_map.get(month_str, 0) + meter_data['data']
            month_data_map[meter_id] = month_map

        flow_data_map[meter_id] = flow_data_map.get(meter_id, 0) + meter_data['data']

    LOG.info("month_statistic:{}".format(month_data_map))
    # 更新缓存中的数据
    for key, val in year_data_map.items():
        conf_cache_api.set_hash('year_statistic', key, json.dumps(val))
    for key, val in month_data_map.items():
        conf_cache_api.set_hash('month_statistic', key, json.dumps(val))
    for key, val in flow_data_map.items():
        conf_cache_api.set_hash('flow_statistic', key, val)


def get_meter_year_data(meter_id):
    """
    获取最近几年的历史数据
    :param meter_id:
    :return:
    """
    data_str = conf_cache_api.get_hash('year_statistic', meter_id)
    if data_str:
        return json.loads(data_str.decode('utf-8'))
    else:
        return {}


def get_meter_month_data(meter_id):
    """
    获取最近12个月
    :param meter_id:
    :return:
    """
    data_str = conf_cache_api.get_hash('month_statistic', meter_id)
    if data_str:
        return json.loads(data_str.decode('utf-8'))
    else:
        return {}


def get_meter_flow_data(meter_id):
    """
    获取流量计总用气量
    :param meter_id:
    :return:
    """
    data = conf_cache_api.get_hash('flow_statistic', meter_id)
    if not data:
        data = 0
    return float(data.decode('utf-8'))



