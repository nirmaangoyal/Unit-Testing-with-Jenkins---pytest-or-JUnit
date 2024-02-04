import pytest
from MathUtils import MathUtils

@pytest.fixture
def math_utils():
    return MathUtils()

def test_add(math_utils):
    assert math_utils.add(2, 3) == 5
    # Add more test cases

def test_subtract(math_utils):
    assert math_utils.subtract(3, 2) == 1
    # Add more test cases

def test_multiply(math_utils):
    assert math_utils.multiply(2, 3) == 6
    # Add more test cases

def test_divide(math_utils):
    assert math_utils.divide(4, 2) == 2.0
    assert math_utils.divide(4, 0) == -1.0  # Test division by zero
    # Add more test cases
