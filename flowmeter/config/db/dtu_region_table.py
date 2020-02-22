# coding=utf-8

from django.db import models
from flowmeter.config.db.user_table import User


class DtuRegion(models.Model):

    """
    厂商对应的可分配区间
    """

    # 左区间
    left = models.IntegerField()
    # 右区间
    right = models.IntegerField()
    # 区间对应的厂商
    manufacturer = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    # 该区间已经使用的数量
    used_num = models.IntegerField()

    class Meta:
        ordering = ['left']
