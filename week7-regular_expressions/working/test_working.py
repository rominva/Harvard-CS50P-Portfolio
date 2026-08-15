import pytest
from working import convert


def test_default():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"
    assert convert("5:00 AM to 9:00 AM") == "05:00 to 09:00"
    assert convert("3:00 PM to 10:00 PM") == "15:00 to 22:00"


def test_optional_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_12_oclock():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    assert convert("12:59 AM to 12:59 PM") == "00:59 to 12:59"


def test_edges():
    assert convert("1 AM to 11 AM") == "01:00 to 11:00"
    assert convert("1 PM to 11 PM") == "13:00 to 23:00"
    assert convert("1 AM to 11 PM") == "01:00 to 23:00"
    

def test_incorrect_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:70 PM")

    with pytest.raises(ValueError):
        convert("10:00 AM to 21:00 PM")


def test_incorrect_format():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

    with pytest.raises(ValueError):
        convert("06:00 AM to 08:00 PM")

    with pytest.raises(ValueError):
        convert("7:00 am to 3:00 pm")

    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")

    with pytest.raises(ValueError):
        convert("9:00  AM  to  5:00  PM")

    with pytest.raises(ValueError):
        convert("9:00 AM till 5:00 PM")

