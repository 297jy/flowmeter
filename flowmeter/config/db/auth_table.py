# coding=utf-8
from django.db import models
from flowmeter.config import const
from flowmeter.config.db.auth_category_table import AuthCategory


class Auth(models.Model):
    """
        权限表
    """
    # 权限名称
    name = models.CharField(max_length=const.NAME_CHAR_LEN)
    # 权限分类
    category = models.ForeignKey(AuthCategory, on_delete=models.CASCADE)
    # 该权限允许执行的动作
    permission_action = models.CharField(max_length=const.REMARK_CHAR_LEN)
    # 权限备注
    remark = models.CharField(max_length=const.REMARK_CHAR_LEN, null=True)

    class Meta:
        ordering = ['id']
