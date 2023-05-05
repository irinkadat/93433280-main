from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("1/3") == 33

    with pytest.raises(ValueError):
        convert("one/five")

    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(80) =="80%"
