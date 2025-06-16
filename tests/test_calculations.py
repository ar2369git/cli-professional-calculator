import pytest
from cli_professional_calculator.calculation.factory import CalculationFactory

def test_valid_add():
    calc = CalculationFactory.create(2, '+', 3)
    assert calc.execute() == 5

def test_invalid_operator():
    with pytest.raises(ValueError):
        CalculationFactory.create(1, '%', 2)
