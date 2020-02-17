# coding=utf-8

from django.db import models
from flowmeter.config.const import NAME_CHAR_LEN, REMARK_CHAR_LEN


class ControlRegister(models.Model):

    name = models.CharField(max_length=NAME_CHAR_LEN)

    address = models.IntegerField()

    const_data = models.IntegerField()

    remark = models.CharField(max_length=REMARK_CHAR_LEN)