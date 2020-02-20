# coding=utf-8
from flowmeter.config.api import cache
from flowmeter.config.db.data_field_table import DataField
from flowmeter.exceptions import DoesNotExistException


def find_data_fields(field_info):

    fields = DataField.objects.filter(**field_info)

    return fields


def find_one_data_field(field_info):

    try:
        field = DataField.objects.get(**field_info)
        return field
    except DataField.DoesNotExist:
        return None


def update_data_field(field_info):

    try:
        field_id = field_info['id']
        field = DataField.objects.get(id=field_id)
        field.begin_address = field_info['begin_address']
        field.end_address = field_info['end_address']
        field.save()
    except DataField.DoesNotExist:
        raise DoesNotExistException("要编辑的数据域不存在，编辑失败！")