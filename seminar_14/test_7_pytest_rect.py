from rectangle import Rectangle
import pytest


@pytest.fixture
def r1():
    return Rectangle(4, 8)


@pytest.fixture
def r2():
    return Rectangle(2, 4)


def test_init_rectangle():
    assert Rectangle(4, 8) is not None, 'Error'


def test_init_rectangle_incorrect():
    with pytest.raises(ValueError):
        Rectangle(-3, 5)

def test_add_is_rectangle(r1, r2):
    assert isinstance(r1 + r2, Rectangle)

def test_is_area_integer(r1):
    assert isinstance(r1.area(), int)


if __name__ == '__main__':
    pytest.main(['-v'])
