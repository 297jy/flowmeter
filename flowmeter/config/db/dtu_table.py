# coding=utf-8

from django.db import models
from flowmeter.config.const import REMARK_CHAR_LEN
from flowmeter.config.db.dtu_region_table import DtuRegion


class Dtu(models.Model):

    # DTU所属于的区间
    region = models.ForeignKey(DtuRegion, on_delete=models.CASCADE)
    # DTU备注
    remark = models.CharField(max_length=REMARK_CHAR_LEN)
