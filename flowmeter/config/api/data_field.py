# coding=utf-8

from flowmeter.config.core import data_field as core
from flowmeter.common.api.validators import param_check, StrCheck


def find_data_fields():

    fields = core.find_data_fields({})

    return fields


def update_data_field(field_info):

    must_dict = {
        'id': int,
        'begin_address': int,
        'end_address': int,
    }
    param_check(field_info, must_dict, extra=True)

    core.update_data_field(field_info)