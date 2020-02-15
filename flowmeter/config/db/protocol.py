# coding=utf-8

from django.db import models
from flowmeter.config import const
from flowmeter.config.db.data_frame_format_table import DataFrameFormat


class Protocol(models.Model):
    """
    通讯协议表
    """
    # 通讯协议名称
    name = models.CharField(max_length=const.PROTOCOL_NAME_CHAR_LEN)
    # 协议对应的数据帧格式
    frame_format = models.ForeignKey(DataFrameFormat, on_delete=models.CASCADE)
    # 备注
    remark = models.CharField(max_length=const.REMARK_CHAR_LEN)
