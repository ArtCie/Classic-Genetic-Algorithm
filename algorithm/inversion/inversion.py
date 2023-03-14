from abc import ABC, abstractmethod
from algorithm.population import Population


class Inversion(ABC):
    @staticmethod
    @abstractmethod
    def evaluate(population: Population) -> Population:
        pass
