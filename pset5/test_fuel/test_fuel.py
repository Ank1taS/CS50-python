from fuel import convert, gauge
import pytest

def test_convert_ValueError():
    with pytest.raises(ValueError):
        assert convert("5/7")
        assert convert("a/s")
        assert convert("0/10")
        assert convert("a/10")
        assert convert("10/s")


def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        assert convert("6/0")
        assert convert("y/0")

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"


