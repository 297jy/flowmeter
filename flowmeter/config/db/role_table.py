# coding=utf-8
from django.db import models
from flowmeter.config import const
from flowmeter.config.db.auth_table import Auth


class Role(models.Model):
    """
        角色表，只用于管理员表，存储每个管理员拥有的权限
    """
    name = models.CharField(max_length=const.NAME_CHAR_LEN, primary_key=True)
    remark = models.CharField(max_length=const.REMARK_CHAR_LEN, null=True)
    label = models.CharField(max_length=const.NAME_CHAR_LEN, default='')

    authorities = models.ManyToManyField(Auth, through='RoleAuth')

    def __eq__(self, other):
        return self.name == other

    def get_dict(self):
        return {
            "name": self.name,
            "label": self.label,
            "remark": self.remark,
        }


class RoleAuth(models.Model):
    """
    角色表和权限表的中间表，用于角色与权限之间的多对多关系映射
    """
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
