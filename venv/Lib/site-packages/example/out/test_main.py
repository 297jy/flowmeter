
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from example.main import get_something


def test_get_something():
    assert (get_something('new') == 'something new')
