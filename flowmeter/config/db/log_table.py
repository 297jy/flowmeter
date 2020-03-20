# coding=utf-8

from django.db import models
from flowmeter.config.db.user_table import User
from flowmeter.config.db.meter_table import Meter
from flowmeter.config.const import STATE_CHAR_LEN, OPR_TYPE_CHAR_LEN, ALARM_TYPE_CHAR_LEN, VALUE_CHAR_LEN, \
    ACTION_TYPE_CHAR_LEN, MSG_CHAR_LEN


class Log(models.Model):
    """
    日志抽象基类
    """
    SUCCESS_STATE = 'success'
    ERROR_STATE = 'error'
    WAITE_STATE = 'wait'

    # 操作时间
    opr_time = models.DateTimeField()

    class Meta:
        abstract = True


class SystemLog(Log):
    """
    系统日志
    """
    LOGIN_SUCCESS = 'success'
    LOGIN_ERROR = 'error'

    # 系统日志的值
    action_type = models.CharField(max_length=ACTION_TYPE_CHAR_LEN)
    # 操作状态
    state = models.CharField(max_length=STATE_CHAR_LEN)
    # 操作用户
    opr_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 信息
    msg = models.CharField(max_length=MSG_CHAR_LEN, default='')


class OprLog(Log):
    """
    操作日志
    """
    # 操作名称
    opr_type = models.CharField(max_length=OPR_TYPE_CHAR_LEN)
    # 操作状态
    state = models.CharField(max_length=STATE_CHAR_LEN)
    # 操作的仪表
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    # 操作值
    val = models.CharField(max_length=VALUE_CHAR_LEN)
    # 操作用户
    opr_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['opr_time']


class AlarmLog(Log):
    """
    告警日志
    """
    ALARM_EXCEED_LIMIT = 'exceed_limit'
    ALARM_INTERRUPT = 'interrupt'
    ALARM_SUB_VALVE = 'sub_valve'
    ALARM_VALVE_ERROR = 'valve_error'
    ALARM_SENSOR_ERROR = 'sensor_error'

    # 发生告警事件的仪表
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)
    # 告警事件类型
    alarm_type = models.CharField(max_length=ALARM_TYPE_CHAR_LEN)
