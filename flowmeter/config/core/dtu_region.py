# coding=utf-8
from flowmeter.common.api import query
from flowmeter.config.db.dtu_region_table import DtuRegion


def add_region(region_info):

    DtuRegion.objects.create(**region_info)


def find_regions(region_info):

    regions = DtuRegion.objects.filter(**region_info)

    return regions


def find_one_region(region_info):

    try:
        region = DtuRegion.objects.get(**region_info)
        return region
    except DtuRegion.DoesNotExist:
        return None


def update_region(region, region_info):

    for key, val in region_info:
        setattr(region, key, val)

    region.save()


def del_region(region):
    """
    删除区间
    :param region:
    :return:
    """
    region.delete()


def del_batch_region(region_ids):
    """
    批量删除DTU区间
    :return:
    """
    query_terms = query.QueryTerms.make_or_query_terms(**{'id': region_ids})

    DtuRegion.objects.filter(query_terms.get_filters()).delete()

