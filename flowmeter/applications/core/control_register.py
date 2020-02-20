# coding=utf-8

from flowmeter.config.api import control_register
from flowmeter.common.common import transfer_hex_str

import logging

logger = logging.getLogger('log')


def transfer_data_to_display(reg_dict):
    """
    将数据库中的数据，转为用户看的数据
    :return:
    """
    reg_dict['field_val'] = transfer_hex_str(reg_dict['field_val'])
    if reg_dict['const_data']:
        reg_dict['const_data'] = transfer_hex_str(reg_dict['const_data'])
    else:
        reg_dict['const_data'] = ''


def transfer_display_to_data(reg_dict):
    """
    将用户看的数据,转为数据库中的数据
    :return:
    """
    address = reg_dict['field_val']
    address = address[2:]
    reg_dict['field_val'] = int(address, 16)
    if reg_dict['const_data']:
        reg_dict['const_data'] = int(reg_dict['const_data'][2:], 16)
    else:
        reg_dict['const_data'] = None


def get_control_registers():

    registers = control_register.find_control_registers()

    register_dicts = []
    for register in registers:
        register_dicts.append(register.get_dict())

    return register_dicts


def update_control_register(register_info):

    control_register.update_control_register(register_info)
