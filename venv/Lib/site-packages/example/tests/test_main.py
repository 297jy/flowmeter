from example.main import get_something


def test_get_something():
    assert get_something('new') == 'something new'
