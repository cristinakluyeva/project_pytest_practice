import pytest

from src.task_2 import calculate_tax

def test_calculate_tax():
    assert calculate_tax(60, 10) == 66.00
    assert calculate_tax(65.5, 5.5) == 69.10

    with pytest.raises(ValueError):
        assert calculate_tax( -20, 5)
        assert calculate_tax( 0, 5)
        assert calculate_tax( 20, 0)
        assert calculate_tax( 20, -5)