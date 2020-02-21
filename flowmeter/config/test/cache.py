# coding=utf-8

from django.test import TestCase
from flowmeter.config.api import cache


class TestCacheApi(TestCase):

    def setUp(self):

        pass

    def test_zset_redis(self):

        di = {
            'testsfd': 'xxxx'
        }
        cache.add_sorted_set('test1', di, 1)
        print(cache.get_sorted_set_first('test1'))




