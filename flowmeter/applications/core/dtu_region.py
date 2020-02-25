# coding=utf-8
from flowmeter.common.api.query import QueryTerms
from flowmeter.config.api import dtu_region as conf_region_api
from flowmeter.exceptions import DoesNotExistException
from flowmeter.settings import MAX_DTU_NO
from flowmeter.applications.api import user as app_user_api


def find_can_alloc_region(total_num):

    # 按区间左边界升序排列
    regions = conf_region_api.find_all_regions()
    # 从编号0开始分配
    left = 0
    right = left + total_num - 1
    for index in range(0, len(regions) - 1):
        region = regions[index]
        next_region = regions[index + 1]
        left = region.right + 1
        right = left + total_num - 1
        # 如果当前选中区间的右边界，不超过下个区间的左边界，则代表选中
        if right < next_region.left:
            break

    if right > MAX_DTU_NO:
        raise DoesNotExistException('不存在DTU最大数目为：{}的可分配区间！'.format(total_num))

    return {
        "left": left,
        "right": right,
    }


def add_region(region_info):

    conf_region_api.add_region(region_info)


def transfer_dtu_region_obj_to_dict(region):
    """
    将DTU区间对象转成字典
    :return:
    """
    region_dict = region.get_dict()
    region_dict['total_num'] = region_dict['right'] - region_dict['left'] + 1
    region_dict['manufacturer_name'] = region_dict['manufacturer'].name
    region_dict['manufacturer_phone'] = region_dict['manufacturer'].phone
    # 删除多余的key
    del region_dict['right']
    del region_dict['manufacturer']
    return region_dict


def find_dtu_regions_by_query_terms(query_terms, page=None):

    # 查找指定条件供气商
    mans = app_user_api.find_manufacturers_by_query_terms(query_terms)
    # 提取所有供气商的id
    man_ids = [m['id'] for m in mans]
    # 构造查询框的查询条件
    query_box = QueryTerms.make_or_query_terms(manufacturer_id=man_ids)

    regions = conf_region_api.find_regions(query_box.get_filters(), page)

    return regions



