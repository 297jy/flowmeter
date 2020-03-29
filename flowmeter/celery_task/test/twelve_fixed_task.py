# coding=utf-8

import time
import datetime
from django.test import TestCase
from flowmeter.config.db.history_data_table import MeterHistoryData
from flowmeter.celery_task.api import twelve_fixed_task as celery_tweleve_api


class TestUserApi(TestCase):

    def setUp(self):
        now_datetime = datetime.datetime.now()
        # 初始化角色
        MeterHistoryData.objects.create(meter_id=11, data=1000, time=(now_datetime - datetime.timedelta(days=1)).date())
        MeterHistoryData.objects.create(meter_id=11, data=1200, time=now_datetime.date())

    def test_statistic_meter_data(self):
        celery_tweleve_api.statistic_meter_data()


