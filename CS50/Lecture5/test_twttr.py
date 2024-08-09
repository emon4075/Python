from twttr import shorten as S


def test1():
    assert S("Emon") == "mn"
    assert S("py") == "py"
    assert S("pet") == "pt"


def test2():
    assert S("Emon123") == "mn123"


def test3():
    assert S("emon?,") == "mn?,"
