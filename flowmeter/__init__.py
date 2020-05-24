# coding:utf-8

from __future__ import absolute_import, unicode_literals
try:
    from flowmeter.celery import app as celery_app

    __all__ = ('celery_app',)
except:
    pass
