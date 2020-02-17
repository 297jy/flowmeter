# coding=utf-8

from flowmeter.config.core import navigation_bar as core
from flowmeter.common.api.validators import param_check
from flowmeter.common.api.validators import StrCheck
from flowmeter.common.api.validators import IntCheck


def create_navigation_bar(navigation_bar_info):
    """
    创建一个导航栏对象
    :param navigation_bar_info:
    :return:
    """
    must_dict = {
        "name": StrCheck.check_navigation_bar_name,
        "icon": StrCheck.check_navigation_bar_icon,
        "url": StrCheck.check_url,
    }
    param_check(navigation_bar_info, must_dict)

    core.check_navigation_bar_unique(navigation_bar_info)
    core.create_navigation_bar(navigation_bar_info)


def edit_navigation_bar(navigation_bar):
    """
    编辑导航栏
    :param navigation_bar:
    :return:
    """
    must_dict = {
        "id": int,
        "auth_id": int,
        "icon": StrCheck.check_navigation_bar_icon,
        "name": StrCheck.check_navigation_bar_name,
        "order": int,
    }
    param_check(navigation_bar, must_dict)

    core.check_navigation_bar_unique(navigation_bar)
    core.edit_navigation_bar(navigation_bar)


def find_navigation_bars_by_auth_id(auth_id=None):
    """
    根据auth_id，查询全部的导航条
    :param auth_id:
    :return:
    """

    navigation_bars = core.find_navigation_bars_by_auth_id(auth_id)

    return navigation_bars




