# coding=utf-8

from flowmeter.config.db.control_register_table import ControlRegister
from flowmeter.exceptions import DoesNotExistException


def find_control_registers(register_info):

    registers = ControlRegister.objects.filter(**register_info)

    return registers


def update_control_register(register_info):

    try:
        reg_id = register_info['id']
        register = ControlRegister.objects.get(id=reg_id)
        register.address = register_info['field_val']
        register.const_data = register_info['const_data']
        register.remark = register_info['remark']
        register.save()
    except ControlRegister.DoesNotExist:
        raise DoesNotExistException("要编辑的控制寄存器不存在，编辑失败！")
