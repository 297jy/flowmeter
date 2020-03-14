# coding=utf-8

from django.db import models
from flowmeter.config import const


class Flag(models.Model):
    """
    系统标志表，存放一些系统中间标志数据
    """
    # 标志名
    name = models.CharField(max_length=const.NAME_CHAR_LEN)
    # 标志值
    val = models.CharField(max_length=const.VALUE_CHAR_LEN)