# coding=utf-8

from django.db import models
from flowmeter.config.const import VALVE_TYPE_CHAR_LEN
from flowmeter.config.db.dtu_table import Dtu


class Valve(models.Model):
    """
    仪表绑定的阀门
    """
    # 共享通信链路阀门，通过modbus协议地址来通信
    SHARE_TYPE = 'share'
    # 独立的通信链路阀门，通过dtu来通信
    INDEPENDENT_TYPE = 'independent'
    # 内嵌在流量计上，无独立阀门控制器
    INLINE_TYPE = 'inline'
    # 阀门类型
    valve_type = models.CharField(max_length=VALVE_TYPE_CHAR_LEN)
    # 阀门绑定的dtu
    dtu = models.OneToOneField(Dtu, on_delete=models.CASCADE, null=True)
    # 阀门绑定的modbus协议地址
    address = models.IntegerField(null=True)
    # 阀门绑定的dtu
    valve_dtu = models.ForeignKey(Dtu, on_delete=models.CASCADE, null=True, related_name='dtu_valve',
                                  db_column='dtu_valve_id')
