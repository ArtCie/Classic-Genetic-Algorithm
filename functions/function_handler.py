from functions.functon_calculator import FunctionCalculator


class FunctionHandler:
    def __init__(self, function_calculator: FunctionCalculator, is_reversed=False):
        self.__function_calculator = function_calculator
        self.is_reversed = is_reversed

    def evaluate(self, x1: float, x2: float) -> float:
        result = round(self.__function_calculator.evaluate(x1, x2), 4)
        return result if not self.is_reversed else - result
