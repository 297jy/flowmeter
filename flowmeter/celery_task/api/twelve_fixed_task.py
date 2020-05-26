# coding=utf-8
"""
每天晚上12点整，执行的定时任务
"""
import os
import datetime
from flowmeter.config.api import history_data as conf_history_api
from flowmeter.config.api import meter as conf_meter_api
from flowmeter.settings import TMP_FILE_DIRECTORY_PATH

import logging
logger = logging.getLogger('log')


def clean_junk_file():
    """
    清除垃圾文件定时任务
    :return:
    """
    filelist = os.listdir(TMP_FILE_DIRECTORY_PATH)
    for f in filelist:
        filepath = os.path.join(TMP_FILE_DIRECTORY_PATH, f)
        os.remove(filepath)


def statistic_meter_data():
    """
    统计仪表数据，用于生成报表信息
    :return:
    """
    logger.info("开始定时统计历史数据！")
    meters = conf_meter_api.get_all_meters()
    meter_datas = []
    for meter in meters:
        meter_datas.append({
            "meter_id": meter.id,
            "data": meter.total_flow - meter.yesterday_total_flow,
            "time": (datetime.datetime.now() - datetime.timedelta(days=1)).date(),
        })
    conf_history_api.add_batch_meter_history_data(meter_datas)
    conf_history_api.sync_meter_history_data()

    for meter in meters:
        meter.yesterday_total_flow = meter.total_flow
        meter.save()


def main():

    statistic_meter_data()


if __name__ == "__main__":
    main()
