from hw_14_task_1 import NegativeValueError, Rectangle
import pytest


@pytest.fixture
def r1():
    return Rectangle(5)


@pytest.fixture
def r2():
    return Rectangle(3, 4)


@pytest.fixture
def r3():
    return Rectangle(10, 1)


def test_width(r1):
    assert r1.width == 5


def test_height(r2):
    assert r2.height == 4


def test_perimeter(r1):
    assert r1.perimeter() == 20


def test_area(r2):
    assert r2.area() == 12


def test_addition(r2):
    r5 = Rectangle(5, 1)
    r4 = r5 + r2
    assert r4.width == 8
    assert r4.height == 5.0


def test_negative_width():
    with pytest.raises(NegativeValueError):
        Rectangle(-5)


def test_negative_height():
    with pytest.raises(NegativeValueError):
        Rectangle(5, -4)


def test_set_width(r1):
    r1.wight = 10
    assert r1.wight == 10


def test_set_negative_width(r1):
    with pytest.raises(NegativeValueError):
        r1.width = -10


def test_set_height(r2):
    r2.height = 6
    assert r2.height == 6


def test_set_negative_height(r2):
    with pytest.raises(NegativeValueError):
        r2.height = -6


def test_subtraction(r2, r3):
    r7 = r3 - r2
    assert r7.width == 1
    assert r7.height == 3.0


def test_subtraction_negative_result(r2, r3):
    with pytest.raises(NegativeValueError):
        r6 = r2 - r3


# def test_subtraction_same_perimeter():
#     r8 = Rectangle(5, 1)
#     r9 = Rectangle(4, 3)
#     r10 = r8 - r9
#     assert r10.width == -3.0
#     assert r10.height == 2


if __name__ == '__main__':
    pytest.main(['-v'])
