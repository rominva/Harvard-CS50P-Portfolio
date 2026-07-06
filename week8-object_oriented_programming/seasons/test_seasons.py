from seasons import extract_date, date_difference, calculate_total_minutes, sing
from datetime import date, datetime, timedelta
import pytest


# ✅ YYYY-MM-DD
def test_extract_date():
    with pytest.raises(ValueError):
        extract_date("January 1, 1999")

    with pytest.raises(ValueError):
        extract_date("24-12-2016")

    with pytest.raises(ValueError):
        extract_date("2020-02-30")

    with pytest.raises(ValueError):
        extract_date("26-01-01")

    with pytest.raises(ValueError):
        extract_date("2019/05/26")


def test_date_difference():
    assert date_difference(date(1970, 1, 1), date(1970, 1, 2)).days == 1
    assert date_difference(date(2025, 1, 1), date(2026, 1, 1)).days == 365
    assert date_difference(date(2000, 1, 1), date(2000, 2, 1)).days == 31
    assert date_difference(date(2000, 2, 28), date(2000, 3, 1)).days == 2


def test_calculate_total_minutes():
    assert calculate_total_minutes(timedelta(days=1)) == 1440
    assert calculate_total_minutes(timedelta(days=0)) == 0
    assert calculate_total_minutes(timedelta(days=365)) == 525600
    assert calculate_total_minutes(timedelta(days=730)) == 1051200


def test_sing():
    assert sing(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert sing(1051200) == "One million, fifty-one thousand, two hundred minutes"
    assert sing(1) == "One minute"
    assert sing(0) == "Zero minutes"
    assert " and " not in sing(1200)