from bank import value

def test_pay_0():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hello, Newman") == 0

def test_pay_20():
    assert value("How you doing?") == 20
    assert value("Hii") == 20

def test_pay_100():
    assert value("What's happening?") == 100
    assert value("hello") == 0

