from abc import ABC, abstractmethod
from algorithm.population import Population


class Cross(ABC):
    @staticmethod
    @abstractmethod
    def evaluate(population: Population) -> Population:
        pass
