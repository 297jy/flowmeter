# coding=utf-8

from flowmeter.config.db.navigation_bar_table import NavigationBar
from flowmeter.exceptions import NotUniqueException, DoesNotExistException


def check_navigation_bar_unique(navigation_bar_info):
    """
    检查导航栏是否已经存在
    :param navigation_bar_info:
    :return:
    """
    not_unique = False

    try:
        navigation_bar = NavigationBar.objects.get(name=navigation_bar_info.get('name'))
        navigation_bar_id = navigation_bar_info.get('id', -1)
        if navigation_bar.id != navigation_bar_id:
            not_unique = True
    except NavigationBar.MultipleObjectsReturned:
        not_unique = True
    except NavigationBar.DoesNotExist:
        pass

    if not_unique:
        raise NotUniqueException("该导航栏已存在！")


def create_navigation_bar(navigation_bar_info):
    """
    创建一个导航栏对象
    :param navigation_bar_info:
    :return:
    """

    NavigationBar.objects.create(**navigation_bar_info)


def edit_navigation_bar(navigation_bar_info):

    try:
        navigation_bar = NavigationBar.objects.get(id=navigation_bar_info['id'])
        navigation_bar.name = navigation_bar_info['name']
        navigation_bar.auth_id = navigation_bar_info['auth_id']
        navigation_bar.icon = navigation_bar_info['icon']
        navigation_bar.save()
    except NavigationBar.DoesNotExist:
        raise DoesNotExistException("该导航栏不存在！")


def find_navigation_bars_by_auth_id(auth_id):

    navigation_bars = NavigationBar.objects.filter(auth_id=auth_id)

    return navigation_bars


