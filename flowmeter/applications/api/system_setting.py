# coding=utf-8

from flowmeter.config.api import configure as conf_configure_api
from flowmeter.applications.core import system_setting as core
from flowmeter.common.api.validators import param_check, StrCheck


def query_system_setting():
    """
    查询所有的系统设置
    :return:
    """
    confs = conf_configure_api.get_all_configure()

    conf_dicts = []
    for conf in confs:
            conf_dicts.append(core.get_configure_dict(conf))

    return conf_dicts


def update_system_setting(conf_info):
    """
    更改系统设置
    :return:
    """
    must_dict = {
        "name": StrCheck.check_configure_name,
        "val": StrCheck.check_value,
    }
    param_check(conf_info, must_dict)

    conf_configure_api.update_configure(conf_info)



