# coding=utf-8

from flowmeter.config.api import data_field
from flowmeter.common.common import transfer_hex_str

import logging

logger = logging.getLogger('log')


def transfer_data_to_display(field_dict):
    """
    将数据库中的数据，转为用户看的数据
    :return:
    """
    field_dict['begin_address'] = transfer_hex_str(field_dict['begin_address'])
    field_dict['end_address'] = transfer_hex_str(field_dict['end_address'])


def transfer_display_to_data(field_dict):
    """
    将用户看的数据,转为数据库中的数据
    :return:
    """
    begin_address = field_dict['begin_address']
    begin_address = begin_address[2:]
    # 16进制转整数
    field_dict['begin_address'] = int(begin_address, 16)
    end_address = field_dict['end_address']
    end_address = end_address[2:]
    # 16进制转整数
    field_dict['end_address'] = int(end_address, 16)


def get_data_fields():

    fields = data_field.find_data_fields()

    field_dicts = []
    for field in fields:
        field_dicts.append(field.get_dict())

    return field_dicts


def update_data_field(field_info):

    data_field.update_data_field(field_info)
