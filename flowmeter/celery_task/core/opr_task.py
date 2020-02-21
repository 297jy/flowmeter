# coding=utf-8

from flowmeter.config.api import meter as conf_meter_api
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.db.operator_table import Operator


def get_opr_handler(opr_type):
    """
    根据操作类型，获取对应的
    :param opr_type:
    :return:
    """
    pass


def __add_surplus_gas(dtu_no, address, num):
    """
    增加剩余气量
    :param dtu_no:
    :param address:
    :param num: 增加的数目
    :return:
    """
    meter = conf_meter_api.find_meter(dtu_no, address)
    meter.surplus_gas = meter.surplus_gas + num
    meter.save()


def __set_meter_address(dtu_no, address, new_address):
    """
    更改物理地址
    :param dtu_no:
    :param address:
    :param new_address:
    :return:
    """
    meter = conf_meter_api.find_meter(dtu_no, address)
    meter.address = new_address
    meter.save()


def __set_flow_ratio(dtu_no, address, flow_ratio):
    """
    更新仪表流量系数
    :param dtu_no:
    :param address:
    :param flow_ratio:
    :return:
    """
    meter = conf_meter_api.find_meter(dtu_no, address)
    meter.flow_ratio = flow_ratio
    meter.save()


def update_meter_data(dtu_no, data):
    """
    更新仪表数据
    :param dtu_no:
    :param data:
    :return:
    """
    opr_type = data['opr_type']
    if opr_type == Operator.QUERY:
        conf_meter_api.update_meter_data(dtu_no, data['address'], data)
    elif opr_type == Operator.RECHARGE:
        __add_surplus_gas(dtu_no, data['address'], data['val'])
    elif opr_type == Operator.SET_METER_ADDRESS:
        __set_meter_address(dtu_no, data['address'], data['val'])
    elif opr_type == Operator.SET_FLOW_RATIO:
        __set_flow_ratio(dtu_no, data['address'], data['val'])
