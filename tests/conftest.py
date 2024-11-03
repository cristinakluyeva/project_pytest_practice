import pytest

@pytest.fixture
def list_normal():
    return [67.0, 68.5, 100.0]

@pytest.fixture
def list_zero_price():
    return [0, 65.5, 28.8]

@pytest.fixture
def list_zero_tax():
    return [56.8, 65.5, 28.8]

@pytest.fixture
def list_empty_price():
    return []