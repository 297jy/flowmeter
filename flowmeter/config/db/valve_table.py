# coding=utf-8

from django.db import models
from flowmeter.config.db.dtu_table import Dtu
from flowmeter.config.db.meter_table import Meter


class Valve(models.Model):
    """
    仪表绑定的阀门控制器
    """
    # 共享通信链路阀门，通过modbus协议地址来通信
    SHARE_TYPE = 'share'
    # 独立的通信链路阀门，通过dtu来通信
    INDEPENDENT_TYPE = 'independent'
    # 内嵌在流量计上，无独立阀门控制器
    INLINE_TYPE = 'inline'
    # 阀门绑定的dtu
    dtu = models.ForeignKey(Dtu, on_delete=models.CASCADE, null=True)
    # 阀门绑定的modbus协议地址
    address = models.IntegerField(null=True)
    # 阀门控制器对应的仪表
    meter = models.OneToOneField(Meter, on_delete=models.CASCADE, null=True)