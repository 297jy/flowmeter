# coding=utf-8

from django.db import models
from flowmeter.config import const
from flowmeter.config.db.data_frame_format_table import DataFrameFormat


class DataField(models.Model):
    """
    数据域表
    """
    # 数据域名称
    name = models.CharField(max_length=const.FIELD_NAME_CHAR_LEN)
    # 在数据帧中的开始地址
    begin_address = models.IntegerField()
    # 在数据帧中的结束地址
    end_address = models.IntegerField()
    # 数据域属于的数据帧
    frame_format = models.ForeignKey(DataFrameFormat, on_delete=models.CASCADE)
