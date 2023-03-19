from functions.functon_calculator import FunctionCalculator

from math import sqrt, sin


class EggholderFunctionCalculator(FunctionCalculator):
    @staticmethod
    def evaluate(x1: float, x2: float) -> float:
        return -(x2 + 47) * sin(sqrt(abs(x2 + x1/2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))