# coding=utf-8

from flowmeter.applications.core import dtu_region as core
from flowmeter.common.api.validators import param_check


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


def find_regions_by_query_terms(query_terms, page=None):
    """
    查找DTU区间
    """

    optional_dict = {
        "query_box": str,
    }
    param_check(query_terms, optional_dict=optional_dict)

    regions = core.find_dtu_regions_by_query_terms(query_terms, page)

    region_dicts = []
    for region in regions:
        region_dict = core.transfer_dtu_region_obj_to_dict(region)
        region_dicts.append(region_dict)

    return region_dicts


