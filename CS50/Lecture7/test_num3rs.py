from num3rs import validate as V


def test_num():
    assert V("255.255.255.2") == True
    assert V("255.255.76") == False
    assert V("255.255.76.987") == False
    assert V("1.2.3.5") == True


def test_str():
    assert V("cat") == False
    assert V("mat") == False
    assert V("pet") == False
