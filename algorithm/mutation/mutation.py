from abc import ABC, abstractmethod
from algorithm.population import Population


class Mutation(ABC):
    @staticmethod
    @abstractmethod
    def evaluate(population: Population) -> Population:
        pass
