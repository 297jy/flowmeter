# coding=utf-8
from django.db.models import F

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


def find_region_by_id(region_id):

    return core.find_one_region({'id': region_id})


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


def del_batch_region(region_ids):
    """
    :return:
    """

    core.del_batch_region(region_ids)


def find_can_used_regions_by_man_id(man_id):
    """
    查找man_id对应的区间列表
    :param man_id:
    :return:
    """
    regions = DtuRegion.objects.filter(manufacturer__id=man_id, used_num__lte=F('right') - F('left') + 1)\
        .values('id', 'left', 'right')
    region_infos = []
    for region in regions:
        region_infos.append(dict(region))
    return region_infos


def find_all_can_used_regions():
    regions = DtuRegion.objects.filter(used_num__lte=F('right') - F('left') + 1) \
        .values('id', 'left', 'right')
    region_infos = []
    for region in regions:
        region_infos.append(dict(region))
    return region_infos
