# coding=utf-8


import time
from django.db import models
from flowmeter.config import const


class Operator:
    """
    操作实体
    """
    # 查询
    QUERY = 'query'
    # 充值
    RECHARGE = 'recharge'
    # 打开预充值
    OPEN_RECHARGE = 'open_recharge'
    # 关闭预充值
    CLOSE_RECHARGE = 'close_recharge'
    # 开阀操作
    OPEN_VALVE = 'open_valve'
    # 关阀操作
    CLOSE_VALVE = 'close_valve'
    # 设置物理地址
    SET_METER_ADDRESS = 'set_meter_address'
    # 重启仪表
    RESET = 'reset'
    # 设置流量系数
    SET_FLOW_RATIO = 'set_flow_ratio'

    def __init__(self):
        self.opr_type = None
        self.val = None
        self.dtu_no = None
        self.address = None
        self.log_id = None
        self.meter_id = None
        self.opr_time = time.time()

    def init(self, dtu_no, meter_address, opr_type, log_id, meter_id, val=None):
        self.opr_type = opr_type
        self.val = val
        self.dtu_no = dtu_no
        self.address = meter_address
        self.log_id = log_id
        self.meter_id = meter_id
        self.opr_time = time.time()

    @staticmethod
    def create_query_opr(dtu_no, meter_address, log_id, meter_id):
        """
        查询操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.QUERY, log_id, meter_id)

        return opr

    @staticmethod
    def create_recharge_opr(dtu_no, meter_address, log_id, meter_id, val):
        """
        充值操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.RECHARGE, log_id, meter_id, val)
        return opr

    @staticmethod
    def create_open_recharge_opr(dtu_no, meter_address, log_id, meter_id):
        """
        开启预充值操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.OPEN_RECHARGE, log_id, meter_id)
        return opr

    @staticmethod
    def create_close_recharge_opr(dtu_no, meter_address, log_id, meter_id):
        """
        关闭预充值操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.CLOSE_RECHARGE, log_id, meter_id)
        return opr

    @staticmethod
    def create_open_valve_opr(dtu_no, meter_address, log_id, meter_id):
        """
        打开阀门操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.OPEN_VALVE, log_id, meter_id)
        return opr

    @staticmethod
    def create_close_valve_opr(dtu_no, meter_address, log_id, meter_id):
        """
        关闭阀门操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.CLOSE_VALVE, log_id, meter_id)
        return opr

    @staticmethod
    def create_set_meter_address_opr(dtu_no, meter_address, log_id, meter_id, val):
        """
        设置仪表地址操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.SET_METER_ADDRESS, log_id, meter_id, val)
        return opr

    @staticmethod
    def create_reset_opr(dtu_no, meter_address, log_id, meter_id):
        """
        重启仪表操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.RESET, log_id, meter_id)
        return opr

    @staticmethod
    def create_set_flow_ratio_opr(dtu_no, meter_address, log_id, meter_id, val):
        """
        设置流量系数操作
        :return:
        """
        opr = Operator()
        opr.init(dtu_no, meter_address, Operator.QUERY, log_id, meter_id, val)
        return opr

    def get_dict(self):

        return {
            'opr_type': self.opr_type,
            "val": self.val,
            "dtu_no": self.dtu_no,
            "meter_address": self.address,
            "log_id": self.log_id,
        }

    def keys(self):
        return 'opr_type', 'val', 'dtu_no', 'address', 'log_id', 'meter_id', 'opr_time'

    def __getitem__(self, item):
        return getattr(self, item)


class UnExecutedOpr(models.Model):
    """
    未执行的远程操作
    """

    # 操作时间
    opr_time = models.FloatField()
    # DTU心跳包编号
    dtu_no = models.IntegerField()
    # 对应的日志ID
    log_id = models.IntegerField(null=True)
    # 物理地址
    address = models.IntegerField()
    opr_type = models.CharField(max_length=const.OPR_TYPE_CHAR_LEN)
    val = models.FloatField(null=True)
    meter_id = models.IntegerField(default=0)

    def keys(self):
        return 'opr_time', 'dtu_no', 'log_id', 'address', 'opr_type', 'meter_id'

    def __getitem__(self, item):
        return getattr(self, item)

    class Meta:
        ordering = ['opr_time']
        index_together = ['dtu_no', 'address', 'opr_type']


class WaitOpr(models.Model):
    """
    已经向服务器发送命令，但是服务器还没响应的操作
    """

    # 操作时间
    opr_time = models.FloatField()
    # DTU心跳包编号
    dtu_no = models.IntegerField()
    # 对应的日志ID
    log_id = models.IntegerField(null=True)
    # 物理地址
    address = models.IntegerField()
    opr_type = models.CharField(max_length=const.OPR_TYPE_CHAR_LEN)
    val = models.FloatField(null=True)
    meter_id = models.IntegerField(default=0)

    def keys(self):
        return 'opr_time', 'dtu_no', 'log_id', 'address', 'opr_type', 'meter_id'

    def __getitem__(self, item):
        return getattr(self, item)

    class Meta:
        ordering = ['opr_time']
        index_together = ['dtu_no', 'address', 'opr_type', 'opr_time']


