# coding=utf-8

from django.db import models
from flowmeter.config import const
from flowmeter.config.db import role_table
from flowmeter.common.const import UserStateType
from flowmeter.common.common import get_allowed_action_of_role


class User(models.Model):

    name = models.CharField(max_length=const.NAME_CHAR_LEN)
    password = models.CharField(max_length=const.PASSWORD_CHAR_LEN)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    create_time = models.DateTimeField()
    state = models.CharField(max_length=16, default=UserStateType.ENABLE_STATE)
    remark = models.CharField(max_length=const.REMARK_CHAR_LEN, default='')
    # 用户角色，基本角色包括：管理员、厂商、流量计用户
    role = models.ForeignKey(role_table.Role, on_delete=models.CASCADE)

    class Meta:
        pass

    def get_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "create_time": self.create_time,
            "state": self.state,
            "remark": self.remark,
            "actions": get_allowed_action_of_role(self.role)
        }
