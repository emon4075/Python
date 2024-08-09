from plates import is_valid as V


def test_1():
    assert V("H") == False
    assert V("HELLOHYBYEBYE") == False
    assert V("HEYE") == True


def test_2():
    assert V("AA2A") == False
    assert V("AA2") == True
    assert V("1AA") == False
    assert V("AA0") == False


def test_3():
    assert V("Hello , World") == False
    assert V("Hello,World") == False
    assert V("  Hello,World") == False


def test_4():
    assert V("AA2@#") == False
