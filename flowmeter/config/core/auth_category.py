# coding=utf-8

from flowmeter.config.db.auth_category_table import AuthCategory


def create_auth_category(category):

    AuthCategory.objects.create(category)