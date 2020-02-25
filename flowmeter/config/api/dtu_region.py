# coding=utf-8

from flowmeter.config.core import dtu_region as core
from flowmeter.common.api.validators import param_check
from flowmeter.config.db.dtu_region_table import DtuRegion


def add_region(region_info):
    """
    添加区间
    :param region_info:
    :return:
    """
    must_dict = {
        "manufacturer_id": int,
        "left": int,
        "right": int,
        "used_num": int,
    }
    param_check(region_info, must_dict)

    core.add_region(region_info)


def find_all_regions():

    return core.find_regions({})


def find_regions(filters=None, page=None):

    if page is None:
        if filters:
            regions = DtuRegion.objects.filter(filters)
        else:
            regions = DtuRegion.objects.all()
    else:
        start_index = page.limit * (page.index - 1)
        end_index = page.index * page.limit
        if filters:
            regions = DtuRegion.objects.filter(filters)[start_index: end_index]
        else:
            regions = DtuRegion.objects.all()[start_index: end_index]

    return regions


def find_region_by_manufacturer_id(manufacturer_id):
    """
    查找供气商对应的DTU区间
    :param manufacturer_id:
    :return:
    """
    return core.find_regions({'manufacturer_id': manufacturer_id})


def update_region(region_info):
    """
    更新区间
    :param region_info:
    :return:
    """
    must_dict = {
        "id": int,
        "left": int,
        "right": int,
        "manufacturer_id": int,
        "used_num": int,
    }
    param_check(region_info, must_dict,)

    region = core.find_one_region({"id": region_info['id']})
    core.update_region(region, region_info)


def del_region(region_id):

    region = core.find_one_region({'id': region_id})
    core.del_region(region)

