from hello import hello as h


def test_default():
    assert h() == "Hello ,world"


def test_rest():
    assert h("Emon") == "Hello ,Emon"
