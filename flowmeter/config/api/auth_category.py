# coding=utf-8

from flowmeter.config.core import auth_category as core
from flowmeter.common.api.validators import param_check
from flowmeter.common.api.validators import StrCheck


def create_auth_category(category):

    must_dict = {
        'name': StrCheck.check_auth_category_name,
    }
    optional_dict = {
        'remark': StrCheck.check_remark,
    }
    param_check(category, must_dict, optional_dict)

    core.create_auth_category(category)