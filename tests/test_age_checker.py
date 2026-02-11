import pytest
from lib.age_checker import age_checker
from datetime import date, datetime, timedelta

def test_access_granted_if_age_greater_than_15():
    result = age_checker("1960-10-21")
    assert result == "Access granted!"

def test_access_is_denied_if_user_is_under_sixtee():
    result = age_checker("2010-07-10")
    assert result == "Access is denied: your current age is 15 and you must be 16"
####################################new

""" def test_access_granted_if_age_is_16():
    today = date.today()
    birth_date = date(today.year - 16, today.month, today.day)
    result = age_checker(birth_date.isoformat())
    assert result == "Access granted!"

def test_access_not_granted_if_one_day_before_birthday():
    today = date.today()
    birth_date = date(today.year - 16, today.month, today.day) + timedelta(days=1)
    result = age_checker(birth_date.isoformat())
    assert result == "Access is denied: your current age is 15 and you must be 16" """