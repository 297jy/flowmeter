# coding=utf-8
from django.db import models
from flowmeter.config.const import DATA_CHAR_LEN
from flowmeter.config.db.meter_table import Meter


class MeterHistoryData(models.Model):
    """
    流量计历史数据
    """
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    # 记录的数据
    data = models.FloatField(max_length=DATA_CHAR_LEN)
    # 记录的日期
    time = models.DateField(db_index=True)
