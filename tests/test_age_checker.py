import pytest
from lib.age_checker import age_checker
from datetime import date, datetime, timedelta

def test_access_granted_if_age_greater_than_15():
    result = age_checker("1960-10-21")
    assert result == "Access granted!"

def test_access_is_denied_if_user_is_under_sixteen():
    result = age_checker("2010-07-10")
    assert result == "Access is denied: your current age is 15 and you must be 16"


def test_error_thrown_for_invalid_date_format():
    with pytest.raises(ValueError) as error:
        age_checker('01-02-2010')
    assert str(error.value) == 'Date must be in YYYY-MM-DD'

def test_error_thrown_when_not_passed_a_string():
    with pytest.raises(TypeError) as error:
        age_checker(15)
    assert str(error.value) == 'Date must be in string format: YYYY-MM-DD'


def test_access_granted_if_age_is_16():
    today = date.today()
    birth_date = date(today.year - 16, today.month, today.day)
    result = age_checker(birth_date.isoformat())
    assert result == "Access granted!"

def test_access_not_granted_if_one_day_before_birthday():
    today = date.today()
    birth_date = date(today.year - 16, today.month, today.day) + timedelta(days=1)
    print(birth_date)
    result = age_checker(birth_date.isoformat())
    assert result == "Access is denied: your current age is 15 and you must be 16" 