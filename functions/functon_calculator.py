from abc import ABC, abstractmethod


class FunctionCalculator(ABC):
    @staticmethod
    @abstractmethod
    def evaluate(x1: float, x2: float) -> float:
        pass
