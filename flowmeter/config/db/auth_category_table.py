# coding=utf-8

from django.db import models
from flowmeter.config import const


class AuthCategory(models.Model):
    """
        权限分类表
    """
    # 分类名称
    name = models.CharField(max_length=const.AUTH_CATEGORY_NAME_CHAR_LEN)
    # 权限分类备注
    remark = models.CharField(max_length=const.REMARK_CHAR_LEN, null=True)
