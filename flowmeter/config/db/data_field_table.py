# coding=utf-8

from django.db import models
from flowmeter.config import const


class DataField(models.Model):
    """
    数据域表
    """
    # 前端显示给用户看的数据域名称
    name = models.CharField(max_length=const.NAME_CHAR_LEN)
    # 在数据帧中的开始地址
    begin_address = models.IntegerField()
    # 在数据帧中的结束地址
    end_address = models.IntegerField()
    # 数据域名称
    field_name = models.CharField(max_length=const.FIELD_NAME_CHAR_LEN)

    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "begin_address": self.begin_address,
            "end_address": self.end_address,
            "field_name": self.field_name,
        }

