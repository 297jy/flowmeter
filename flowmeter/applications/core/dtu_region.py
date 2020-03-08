# coding=utf-8
from flowmeter.common.api.query import QueryTerms
from flowmeter.config.api import dtu_region as conf_region_api
from flowmeter.exceptions import DoesNotExistException, ParameterErrorException
from flowmeter.settings import MAX_DTU_NO
from flowmeter.applications.api import user as app_user_api


def find_can_alloc_region(total_num):

    # 按区间左边界升序排列
    regions = conf_region_api.find_all_regions()
    if len(regions) == 0:
        return {
            "left": 0,
            "right": total_num,
        }

    left = 0
    right = left + total_num - 1

    for region in regions:

        # 如果当前选中区间的右边界，不超过下个区间的左边界，则代表选中
        if right < region.left:
            break
        left = region.right + 1
        right = left + total_num - 1

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
    if len(man_ids) == 0:
        return []

    # 构造查询框的查询条件
    query_box = QueryTerms.make_or_query_terms(manufacturer_id=man_ids)

    regions = conf_region_api.find_regions(query_box.get_filters(), page)

    return regions


def is_total_num_legal(region, total_num):
    """
    判断DTU区间最大数目是否合法
    :param region:
    :param total_num:
    :return:
    """
    # 新的右边界
    new_right = region.left + total_num - 1
    # 按区间左边界升序排列
    regions = conf_region_api.find_all_regions()

    can_expand = True
    for reg in regions:
        if reg.id == region.id:
            continue
        if reg.left <= new_right <= reg.right or reg.left <= region.left <= reg.right:
            can_expand = False

    return can_expand


def update_region_total_num(region, total_num):
    """
    更新DTU区间的最大数目
    :param region:
    :param total_num:
    :return:
    """
    region.right = region.left + total_num - 1
    region.save()


def check_region_can_del(region_id):
    """
    判断该DTU区间是否可被删除，不能删除就抛异常
    :param region_id:
    :return:
    """
    region = conf_region_api.find_region_by_id(region_id)
    if region.used_num != 0:
        raise ParameterErrorException("供气商名称：{}，DTU起始编号为：{}的区间上已经存在DTU，删除失败！")
