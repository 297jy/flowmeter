# coding=utf-8

from flowmeter.applications.core import data_field as core

import logging

from flowmeter.common.api.validators import StrCheck, param_check

logger = logging.getLogger('log')


def get_data_fields():

    fields = core.get_data_fields()
    for field in fields:
        core.transfer_data_to_display(field)
    return fields


def update_data_field(field_info):

    must_dict = {
        'id': int,
        'begin_address': str,
        'end_address': str,
    }
    param_check(field_info, must_dict, extra=True)

    core.transfer_display_to_data(field_info)
    core.update_data_field(field_info)