# coding=utf-8

from django.db import models
from flowmeter.config.db.dtu_table import Dtu
from flowmeter.config.db.user_table import User
from flowmeter.config.db.valve_table import Valve
from flowmeter.config.db.meter_state_table import MeterState
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
    # 剩余气体限值
    surplus_gas_limits = models.FloatField(default=const.UNKNOWN_VALUE)
    # 流量系数
    flow_ratio = models.FloatField(default=const.UNKNOWN_VALUE)
    # 瞬时流量
    flow_rate = models.FloatField(default=const.UNKNOWN_VALUE)
    # 累计流量
    total_flow = models.FloatField(default=const.UNKNOWN_VALUE)
    # 温度
    temperature = models.FloatField(default=const.UNKNOWN_VALUE)
    # 电压
    power = models.FloatField(default=const.UNKNOWN_VALUE)
    # 温度
    version = models.FloatField(default=const.UNKNOWN_VALUE)
    # 仪表备注
    remark = models.CharField(max_length=const.REMARK_CHAR_LEN)
    # 仪表的使用用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 仪表对应的阀门控制器
    valve = models.OneToOneField(Valve, on_delete=models.CASCADE)
    # 仪表对应的各种状态
    state = models.OneToOneField(MeterState, on_delete=models.CASCADE)
