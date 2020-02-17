# coding=utf-8

from django.db import models
from flowmeter.config.const import NAME_CHAR_LEN, REMARK_CHAR_LEN


class ControlRegister(models.Model):
    # 名称
    name = models.CharField(max_length=NAME_CHAR_LEN)
    # 地址
    address = models.IntegerField()
    # 固定数据
    const_data = models.IntegerField(null=True)
    # 备注
    remark = models.CharField(max_length=REMARK_CHAR_LEN, default='')

    def get_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "const_data": self.const_data,
            "remark": self.remark,
        }