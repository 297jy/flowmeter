# coding=utf-8
"""
每天晚上12点整，执行的定时任务
"""
import json
import os

from flowmeter.celery import app
from flowmeter.config.api import history_data as conf_history_api
from flowmeter.config.api import cache as conf_cache_api
from flowmeter.celery_task.core import twelve_fixed_task as core

import logging
logger = logging.getLogger('log')


@app.task
def clean_junk_file():
    """
    清除垃圾文件定时任务
    :return:
    """
    tmp_dir = '/project/python/flowmeter/file/tmp'
    filelist = os.listdir(tmp_dir)
    for f in filelist:
        filepath = os.path.join(tmp_dir, f)
        os.remove(filepath)


@app.task
def statistic_meter_data():
    """
    统计仪表数据，用于生成报表信息
    :return:
    """
    data_dict = conf_history_api.find_recent_week_all_meters_history_data()
    for meter_id, data_list in data_dict.items():
        conf_cache_api.set_hash('statistic', meter_id, json.dumps(core.calculator_week_flow_usage(data_list)))

