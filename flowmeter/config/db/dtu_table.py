# coding=utf-8

from django.db import models
from flowmeter.config.const import REMARK_CHAR_LEN
from flowmeter.config.db.dtu_region_table import DtuRegion
from flowmeter.config.db.user_table import User


class Dtu(models.Model):

    # DTU所属于的区间
    region = models.ForeignKey(DtuRegion, on_delete=models.CASCADE)
    # DTU备注
    remark = models.CharField(max_length=REMARK_CHAR_LEN)
    # 心跳包编号
    dtu_no = models.IntegerField(unique=True)
    # 仪表的使用用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


