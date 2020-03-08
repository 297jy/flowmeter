# coding=utf-8

from flowmeter.applications.core import dtu as core
from flowmeter.config.api import dtu as conf_dtu_api
from flowmeter.config.api import dtu_region as conf_region_api
from flowmeter.common.api.validators import param_check
from flowmeter.common.api.validators import StrCheck


def add_dtu(dtu):
    """
    添加一个dtu
    :return:
    """
    must_dict = {
        "region_id": int,
        "user_id": int,
    }
    optional_dict = {
        "remark": StrCheck.check_remark,
    }
    param_check(dtu, must_dict, optional_dict)

    region = conf_region_api.find_region_by_id(dtu['region_id'])
    dtu['dtu_no'] = core.find_can_use_dtu_no(region)

    conf_dtu_api.add_dtu(dtu)

    core.update_region_used_num(region)


def find_dtu_by_query_terms(query_terms, page=None):
    """
    查找DTU区间
    """

    optional_dict = {
        "manufacturer_id": int,
        "dtu_user_id": int,
    }

    param_check(query_terms, optional_dict=optional_dict)

    filters = core.get_dtu_filter(query_terms.get('manufacturer_id'), query_terms.get('dtu_user_id'))

    dtus = conf_dtu_api.find_dtus(filters, page)

    dtu_dicts = []
    for dtu in dtus:
        dtu_dicts.append(core.get_dtu_dict(dtu))

    return dtu_dicts


def update_dtu_region(dtu_info):

    must_dict = {
        "id": int,
    }
    optional_dict = {
        'remark': StrCheck.check_remark,
    }
    param_check(dtu_info, must_dict, optional_dict)

    dtu = conf_dtu_api.find_dtu_by_id(dtu_info['id'])

    core.update_dtu(dtu, dtu_info)


def del_batch_dtu(dtu_ids):
    """
    :return:
    """

    conf_dtu_api.del_batch_dtu(dtu_ids)
    for dtu_id in dtu_ids:
        dtu = conf_dtu_api.find_dtu_by_id(dtu_id)
        core.update_region_used_num(dtu.region)

