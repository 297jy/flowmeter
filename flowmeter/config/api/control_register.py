# coding=utf-8

from flowmeter.config.core import control_register as core
from flowmeter.common.api.validators import param_check, StrCheck


def find_control_registers():

    registers = core.find_control_registers({})

    return registers


def update_control_register(register_info):

    must_dict = {
        'id': int,
        'address': int,
        'remark': StrCheck.check_remark,
    }

    param_check(register_info, must_dict, extra=True)

    core.update_control_register(register_info)