# coding=utf-8

from flowmeter.config.core import auth as core
from flowmeter.common.api.validators import param_check
from flowmeter.common.api.validators import StrCheck
from flowmeter.config.db.auth_table import Auth


def create_authority(authority):

    must_dict = {
        "name": StrCheck.check_auth_name,
        "permission_action": StrCheck.check_auth_permission_action,
    }
    optional_dict = {
        "remark": StrCheck.check_remark,
    }
    param_check(authority, must_dict, optional_dict)

    core.check_auth_unique(authority)
    core.create_authority(authority)


def edit_auth(auth_info):

    must_dict = {
        "id": int,
    }
    optional_dict = {
        "remark": StrCheck.check_remark,
    }
    param_check(auth_info, must_dict, optional_dict, extra=True)

    core.edit_auth(auth_info)


def find_all_auth():

    auths = Auth.objects.all()

    return auths


def find_auths_by_id_list(auth_ids):

    auths = Auth.objects.filter(id__in=auth_ids)

    return auths