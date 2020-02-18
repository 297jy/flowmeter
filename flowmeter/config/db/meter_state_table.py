# coding=utf-8

from django.db import models

from flowmeter.config import const


class MeterState(models.Model):

    # 在线状态
    STATE_ONLINE = 'online'
    # 离线状态
    STATE_OFFLINE = 'offline'
    # 阀门状态,1代表关阀,2代表开阀
    valve_state = models.CharField(default=const.UNKNOWN_STATE, max_length=8)
    # 充值状态,1代表关闭充值功能,2代表开启充值功能
    recharge_state = models.CharField(default=const.UNKNOWN_STATE, max_length=8)
    # 电池欠压状态
    battery_pressure_state = models.CharField(default=const.UNKNOWN_STATE, max_length=8)
    # 阀门异常标志
    valve_error_flag = models.IntegerField(default=const.UNKNOWN_VALUE)
    # 欠费状态
    owe_state = models.IntegerField(default=const.UNKNOWN_VALUE)
    # 传感器异常标志
    sensor_error_flag = models.IntegerField(default=const.UNKNOWN_VALUE)
    # 仪表状态
    state = models.CharField(default=const.UNKNOWN_STATE, max_length=8)
