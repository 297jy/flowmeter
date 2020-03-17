# coding=utf-8

import datetime


class Operator:
    """
    操作实体
    """

    QUERY = 'query'
    RECHARGE = 'recharge'
    OPEN_RECHARGE = 'open_recharge'
    CLOSE_RECHARGE = 'close_recharge'
    OPEN_VALVE = 'open_valve'
    CLOSE_VALVE = 'close_valve'
    SET_METER_ADDRESS = 'set_meter_address'
    RESET = 'reset'
    SET_FLOW_RATIO = 'set_flow_ratio'

    def __init__(self):
        self.user_id = None
        self.opr_type = None
        self.val = None
        self.dtu_no = None
        self.meter_address = None
        self.log_id = None
        self.valve_dtu_no = None
        self.valve_address = None

    def init(self, user_id, dtu_no, meter_address, opr_type, log_id, val=None):
        self.user_id = user_id
        self.opr_type = opr_type
        self.val = val
        self.dtu_no = dtu_no
        self.meter_address = meter_address
        self.log_id = log_id

    @staticmethod
    def create_query_opr(user_id, dtu_no, meter_address, log_id):
        """
        查询操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.QUERY, log_id)

        return opr

    @staticmethod
    def create_recharge_opr(user_id, dtu_no, meter_address, log_id, val):
        """
        充值操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.RECHARGE, log_id, val)
        return opr

    @staticmethod
    def create_open_recharge_opr(user_id, dtu_no, meter_address, log_id):
        """
        开启预充值操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.OPEN_RECHARGE, log_id)
        return opr

    @staticmethod
    def create_close_recharge_opr(user_id, dtu_no, meter_address, log_id):
        """
        关闭预充值操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.CLOSE_RECHARGE, log_id)
        return opr

    @staticmethod
    def create_open_valve_opr(user_id, dtu_no, meter_address, log_id):
        """
        打开阀门操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.OPEN_VALVE, log_id)
        return opr

    @staticmethod
    def create_close_valve_opr(user_id, dtu_no, meter_address, log_id):
        """
        关闭阀门操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.CLOSE_VALVE, log_id)
        return opr

    @staticmethod
    def create_set_meter_address_opr(user_id, dtu_no, meter_address, log_id, val):
        """
        设置仪表地址操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.SET_METER_ADDRESS, log_id, val)
        return opr

    @staticmethod
    def create_reset_opr(user_id, dtu_no, meter_address, log_id):
        """
        重启仪表操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.RESET, log_id)
        return opr

    @staticmethod
    def create_set_flow_ratio_opr(user_id, dtu_no, meter_address, log_id, val):
        """
        设置流量系数操作
        :return:
        """
        opr = Operator()
        opr.init(user_id, dtu_no, meter_address, Operator.QUERY, log_id, val)
        return opr

    def get_dict(self):

        return {
            'user_id': self.user_id,
            'opr_type': self.opr_type,
            "val": self.val,
            "dtu_no": self.dtu_no,
            "meter_address": self.meter_address,
            "log_id": self.log_id,
        }

    def keys(self):
        return 'user_id', 'opr_type', 'opr_time', 'val', 'dtu_no', 'meter_address', 'log_id'

    def __getitem__(self, item):
        return getattr(self, item)


