from Bank import value


def test_1():
    assert value("Hello, Newman") == 0
    assert value("Hello") == 0


def test_2():
    assert value("How") == 20


def test_3():
    assert value("WTF") == 100
