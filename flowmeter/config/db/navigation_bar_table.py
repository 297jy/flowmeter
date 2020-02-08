# coding=utf-8

from django.db import models
from flowmeter.config.db.auth_table import Auth
from flowmeter.config import const


class NavigationBar(models.Model):
    """
    导航栏表，只做二级导航
    """
    # 导航栏图标
    icon = models.CharField(max_length=const.NAVIGATION_BAR_ICON_CHAR_LEN, default='')
    # 导航栏名字
    name = models.CharField(max_length=const.NAVIGATION_BAR_NAME_CHAR_LEN)
    # 父导航栏的id
    fid = models.IntegerField(default=-1)
    # 导航栏对应的需要的权限
    auth = models.ForeignKey(Auth, on_delete=models.CASCADE)
    # 导航条排列顺序
    order = models.IntegerField(default=0)
    # 导航条对应的url
    url = models.CharField(max_length=const.URL_CHAR_LEN, default='')

    class Meta:
        ordering = ['order']

    def get_dict(self):
        return {
            "icon": self.icon,
            "name": self.name,
            "url": self.url,
        }