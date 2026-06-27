import pytest
from fuel import convert, gauge


def test_convert_valid_fraction():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("0/4") == 0
    assert convert("4/4") == 100


def test_convert_invalid_fraction():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("-3/4")
    with pytest.raises(ValueError):
        convert("5/4")


def test_gauge_boundaries():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(98) == "98%"

    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"

    assert gauge(75) == "75%"
    assert gauge(25) == "25%"
