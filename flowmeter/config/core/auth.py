# coding=utf-8

from flowmeter.config.db.auth_table import Auth
from flowmeter.exceptions import NotUniqueException
from flowmeter.exceptions import DoesNotExistException


def create_authority(authority):

    Auth.objects.create(authority)


def edit_auth(auth_info):

    try:
        auth = Auth.objects.get(id=auth_info['id'])
        auth.remark = auth_info.get('remark', '')
        auth.save()
    except Auth.DoesNotExist:
        raise DoesNotExistException("该权限不存在！")


def check_auth_unique(auth_info):

    not_unique = False
    try:
        auth = Auth.objects.get(name=auth_info['name'])
        if auth.id != auth_info.get('id', -1):
            not_unique = True
    except Auth.DoesNotExist:
        pass
    except Auth.MultipleObjectsReturned:
        not_unique = True

    if not_unique:
        raise NotUniqueException("该权限已经存在！")





