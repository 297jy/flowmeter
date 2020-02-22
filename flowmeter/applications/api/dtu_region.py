# coding=utf-8

from flowmeter.applications.core import dtu_region as core


def add_region(manufacturer_id, total_num):
    """
    添加一个dtu区间
    :param manufacturer_id:
    :param total_num:
    :return:
    """
    region_info = core.find_can_alloc_region(total_num)
    region_info['manufacturer_id'] = manufacturer_id
    region_info['used_num'] = 0
    core.add_region(region_info)


