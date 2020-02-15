# coding=utf-8

from django.db import models
from flowmeter.config import const


class DataFrameFormat(models.Model):
    """
    数据帧格式表
    """
    # 数据帧格式名称
    name = models.CharField(max_length=const.FIELD_NAME_CHAR_LEN)
    # 备注
    remark = models.CharField(max_length=const.REMARK_CHAR_LEN)
