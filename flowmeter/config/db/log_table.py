# coding=utf-8

from django.db import models
from flowmeter.config.db.user_table import User
from flowmeter.config.db.meter_table import Meter
from flowmeter.config.const import STATE_CHAR_LEN, OPR_TYPE_CHAR_LEN, ALARM_TYPE_CHAR_LEN


class Log(models.Model):
    """
    日志抽象基类
    """
    SUCCESS_STATE = 'success'
    ERROR_STATE = 'error'
    WAITE_STATE = 'wait'

    # 操作用户
    opr_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 操作时间
    opr_time = models.DateTimeField()
    # 操作状态
    state = models.CharField(max_length=STATE_CHAR_LEN)

    class Meta:
        abstract = True


class LoginLog(Log):
    """
    登录日志
    """
    LOGIN_SUCCESS = 'success'
    LOGIN_ERROR = 'error'


class OprLog(Log):
    """
    操作日志
    """
    # 操作名称
    opr_name = models.CharField(max_length=OPR_TYPE_CHAR_LEN)


class AlarmLog(Log):
    """
    告警日志
    """
    EXCEED_LIMIT_ALARM = 'exceed_limit'
    INTERRUPT = 'interrupt'
    SUB_VALVE = 'sub_valve'

    # 发生告警事件的仪表用户
    meter_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_alarm')
    # 发生告警事件的仪表
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    # 告警事件类型
    alarm_type = models.CharField(max_length=ALARM_TYPE_CHAR_LEN)