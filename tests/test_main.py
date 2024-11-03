import pytest
from src.main import calculate_taxes
from tests.conftest import list_normal, list_zero_price, list_zero_tax, list_empty_price

def test_calculate_taxes(list_normal):
    assert calculate_taxes(list_normal, 7.0) == [71.69, 73.295, 107.0]



def test_calculate_taxes_zero(list_zero_price):
    with pytest.raises(ValueError):
        assert calculate_taxes(list_zero_price, 7.0)


def test_calculate_taxes_zero_tax(list_zero_tax):
    assert calculate_taxes(list_zero_tax, 0)== list_zero_tax
    with pytest.raises(ValueError):
        assert calculate_taxes(list_zero_tax, -3)


def test_calculate_taxes_empty(list_empty_price):
    assert calculate_taxes(list_empty_price, 7.0) == []


def test_calculate_taxes_int():
    assert calculate_taxes([50, 80, 70], 13) == [56.5, 90.4, 79.1]


def test_calculate_taxes_minus():
    with pytest.raises(ValueError):
        assert calculate_taxes([-50, 80, 70], 13)
