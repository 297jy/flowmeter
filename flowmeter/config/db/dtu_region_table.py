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
    manufacturer = models.ForeignKey(User, on_delete=models.CASCADE)
    # 该区间已经使用的数量
    used_num = models.IntegerField()

    class Meta:
        ordering = ['manufacturer', 'left']

    def get_dict(self):
        return {
            "left": self.left,
            "right": self.right,
            "manufacturer": self.manufacturer,
            "used_num": self.used_num,
        }
