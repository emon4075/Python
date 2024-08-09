# More the function more the easier to find bugs
# E:\Python\CS50\Lecture5>pytest test_calculator.py
from calculator import Square as Sq


def test_positive():
    assert Sq(2) == 4
    assert Sq(3) == 9
    assert Sq(4) == 16
    assert Sq(5) == 25


def test_negative():
    assert Sq(-2) == 4
    assert Sq(-3) == 9
    assert Sq(-4) == 16


def zero_test():
    assert Sq(0) == 0
