# coding=utf-8

from flowmeter.applications.core import control_register as core

import logging

from flowmeter.common.api.validators import StrCheck, param_check

logger = logging.getLogger('log')


def get_control_registers():

    registers = core.get_control_registers()
    for reg in registers:
        core.transfer_data_to_display(reg)
    return registers


def update_control_register(register_info):

    must_dict = {
        'id': int,
        'address': str,
        'const_data': str,
        'remark': StrCheck.check_remark,
    }
    param_check(register_info, must_dict, extra=True)

    core.transfer_display_to_data(register_info)
    core.update_control_register(register_info)