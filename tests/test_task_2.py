import pytest

from src.task_2 import calculate_tax

def test_calculate_tax():
    assert calculate_tax(60, 10) == 66.00
    # assert calculate_tax(65.5, 5.5) == 69.10

    with pytest.raises(ValueError):
        # assert calculate_tax( -20, 5)
        # assert calculate_tax( 0, 5)
        assert calculate_tax( 20, -5)
        # assert calculate_tax( 20, -5)
        # assert calculate_tax(-45.45,-55.76)
        # assert calculate_tax(0, 0)


def test_calculate_discount():
    assert calculate_tax(45, 25, 0.15) == 49.5
    assert calculate_tax(45, 25, 0) == 56.25