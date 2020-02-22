# coding=utf-8

from flowmeter.config.api import dtu_region as conf_region_api
from flowmeter.exceptions import DoesNotExistException
from flowmeter.settings import MAX_DTU_NO


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



