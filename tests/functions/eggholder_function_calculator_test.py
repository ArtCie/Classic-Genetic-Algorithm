from functions.eggholder_function_calculator import EggholderFunctionCalculator
from functions.function_handler import FunctionHandler

import pytest


@pytest.fixture
def eggholder_function_calculator() -> EggholderFunctionCalculator:
    return EggholderFunctionCalculator()


class TestEggholderFunctionCalculator:
    def test_evaluate_minimum(self, eggholder_function_calculator: EggholderFunctionCalculator):
        function_handler = FunctionHandler(eggholder_function_calculator)
        x1 = 512
        x2 = 404.2319
        assert function_handler.evaluate(x1, x2) == -959.6407

    def test_evaluate_minimum_reversed(self, eggholder_function_calculator: EggholderFunctionCalculator):
        function_handler = FunctionHandler(eggholder_function_calculator, is_reversed=True)
        x1 = 512
        x2 = 404.2319
        assert function_handler.evaluate(x1, x2) == 959.6407

    def test_evaluate_value(self, eggholder_function_calculator: EggholderFunctionCalculator):
        function_handler = FunctionHandler(eggholder_function_calculator)
        x1 = 123
        x2 = 543
        assert function_handler.evaluate(x1, x2) == -271.003

    def test_evaluate_value_reversed(self, eggholder_function_calculator: EggholderFunctionCalculator):
        function_handler = FunctionHandler(eggholder_function_calculator, is_reversed=True)
        x1 = 123
        x2 = 543
        assert function_handler.evaluate(x1, x2) == 271.003
