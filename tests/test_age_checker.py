import pytest
from lib.age_checker import age_checker

def test_access_granted_if_age_greater_than_15():
    result = age_checker("1960-10-21")
    assert result == "Access granted!"