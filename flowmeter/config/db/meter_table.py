# coding=utf-8

from django.db import models
from flowmeter.config.db.dtu_table import Dtu
from flowmeter.config.db.user_table import User
from flowmeter.config.db.valve_table import Valve
from flowmeter.config import const


class Meter(models.Model):

    # 所属于的DTU
    dtu = models.ForeignKey(Dtu, on_delete=models.CASCADE)
    # 在DTU内部的相对地址
    address = models.IntegerField(default=const.UNKNOWN_VALUE)
    # 仪表上一次采集数据的时间
    last_update_time = models.DateTimeField()
    # 剩余气量
    surplus_gas = models.FloatField(default=const.UNKNOWN_VALUE)
    # 阀门状态,1代表关阀,2代表开阀
    valve_state = models.CharField(default=const.UNKNOWN_STATE, max_length=8)
    # 充值状态,1代表关闭充值功能,2代表开启充值功能
    recharge_state = models.CharField(default=const.UNKNOWN_STATE, max_length=8)
    # 剩余气体限值
    surplus_gas_limits = models.FloatField(default=const.UNKNOWN_VALUE)
    # 流量系数
    flow_ratio = models.FloatField(default=const.UNKNOWN_VALUE)
    # 仪表状态
    state = models.CharField(default=const.UNKNOWN_STATE, max_length=8)
    # 瞬时流量
    flow_rate = models.FloatField(default=const.UNKNOWN_VALUE)
    # 累计流量
    total_flow = models.FloatField(default=const.UNKNOWN_VALUE)
    # 温度
    temperature = models.FloatField(default=const.UNKNOWN_VALUE)
    # 电池欠压状态
    battery_pressure_state = models.CharField(default=const.UNKNOWN_STATE, max_length=8)
    # 阀门异常标志
    valve_error_flag = models.IntegerField(default=const.UNKNOWN_VALUE)
    # 电压
    power = models.FloatField(default=const.UNKNOWN_VALUE)
    # 欠费状态
    owe_state = models.IntegerField(default=const.UNKNOWN_VALUE)
    # 传感器异常标志
    sensor_error_flag = models.IntegerField(default=const.UNKNOWN_VALUE)
    # 温度
    version = models.FloatField(default=const.UNKNOWN_VALUE)
    # 仪表备注
    remark = models.CharField(max_length=const.REMARK_CHAR_LEN)
    # 仪表的使用用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    valve = models.ForeignKey(Valve, on_delete=models.CASCADE)
