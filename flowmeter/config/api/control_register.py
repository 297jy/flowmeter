# coding=utf-8
import json

from flowmeter.config.core import control_register as core
from flowmeter.common.api.validators import param_check, StrCheck
from flowmeter.config.api import cache as conf_cache_api
from flowmeter.config.db.control_register_table import ControlRegister
from django.db import transaction


def find_control_registers():

    registers = core.find_control_registers({})

    return registers


def find_registers_by_field_val(field_val):

    registers = core.find_control_registers({'field_val': field_val})

    return registers


def find_register_by_opr_type(opr_type):

    register_str = conf_cache_api.get_hash('control_register', opr_type)
    if register_str is None:
        register = core.find_one_control_register({'opr_type': opr_type})
        register_str = json.dumps({'field_val': register.field_val, 'const_data': register.const_data})
        # 重新设置缓存
        conf_cache_api.set_hash('control_register', opr_type, register_str)
    else:
        register_dict = json.loads(register_str)
        register = ControlRegister()
        register.field_val = register_dict['field_val']
        register.const_data = register_dict['const_data']

    return register


def update_control_register(register_info):

    must_dict = {
        'id': int,
        'field_val': int,
        'remark': StrCheck.check_remark,
    }

    param_check(register_info, must_dict, extra=True)

    register_str = json.dumps({'field_val': register_info['field_val'], 'const_data': register_info['const_data']})

    with transaction.atomic():
        register = core.update_control_register(register_info)
        # 重新设置缓存
        conf_cache_api.set_hash('control_register', register.opr_type, register_str)