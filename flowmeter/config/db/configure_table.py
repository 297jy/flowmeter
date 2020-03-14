# coding=utf-8

from django.db import models
from flowmeter.config import const


class Configure(models.Model):
    """
    系统配置表
    """
    # 配置名
    name = models.CharField(max_length=const.NAME_CHAR_LEN)
    # 中文配置名
    label = models.CharField(max_length=const.NAME_CHAR_LEN)
    # 配置值
    val = models.CharField(max_length=const.VALUE_CHAR_LEN)