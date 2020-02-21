# coding=utf-8

from django.test import TestCase
from flowmeter.config.api import meter


class TestMeterApi(TestCase):

    def setUp(self):

        pass

    def test_find_meter(self):

        meter.find_meter(1, 1)
