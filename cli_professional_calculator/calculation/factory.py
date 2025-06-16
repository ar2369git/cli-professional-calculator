from cli_professional_calculator.calculation.calc import Calculation
from cli_professional_calculator.operation import basic

class CalculationFactory:
    @staticmethod
    def create(a, op, b):
        operations = {
            '+': basic.add,
            '-': basic.subtract,
            '*': basic.multiply,
            '/': basic.divide,
        }
        if op not in operations:
            raise ValueError("Unsupported operation")
        return Calculation(a, b, operations[op])
