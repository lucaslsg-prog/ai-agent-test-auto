import pytest
from discount import calculate_discount

def test_standard_discount():
    assert calculate_discount(12500, 8) == 11500.00


def test_zero_discount():
    assert calculate_discount(999, 0) == 999.00


def test_full_discount():
    assert calculate_discount(999, 100) == 0.00


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_discount(-100, 10)


def test_discount_above_limit():
    with pytest.raises(ValueError):
        calculate_discount(1000, 101)