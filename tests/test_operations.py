import pytest
from cli_professional_calculator.operation import basic

@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (-1, 1, 0)])
def test_add(a, b, expected):
    assert basic.add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [(10, 2, 5)])
def test_divide(a, b, expected):
    assert basic.divide(a, b) == expected
