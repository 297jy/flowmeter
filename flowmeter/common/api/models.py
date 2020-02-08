# coding=utf-8
from django.db.models import Q


def compose_or_query_terms(filters):
    """
    组成or查询条件
    :param filters: dict,
    :return:
    """
    condition = None
    for filter_name, filter_val in filters:
        if condition:
            condition = condition | Q(filter_name=filter_val)
        else:
            condition = Q(filter_name=filter_val)
    return condition


def compose_and_query_terms(filters):
    """
        组成or查询条件
        :param filters: dict,
        :return:
        """
    condition = None
    for filter_name, filter_val in filters:
        if condition:
            condition = condition & Q(filter_name=filter_val)
        else:
            condition = Q(filter_name=filter_val)
    return condition
