from abc import ABC, abstractmethod
from algorithm.population_repository import PopulationRepository
from enum import IntEnum


class Mutation(ABC):
    def __init__(self, probability: float, start_point: float, end_point: float):
        self.PROBABILITY = probability
        self.start_point = start_point
        self.end_point = end_point

    @abstractmethod
    def evaluate(self, population: PopulationRepository) -> PopulationRepository:
        pass


class MutationTypes(IntEnum):
    BALANCED = 0
    GAUSS = 1

    @staticmethod
    def get_names():
        return [mutation_type.name for mutation_type in MutationTypes]

    @staticmethod
    def get_mutation_by_type(type, probability, start_point, end_point):
        if type == MutationTypes.BALANCED:
            from algorithm.mutation_real.balanced import Balanced
            return Balanced(probability, start_point, end_point)
        elif type == MutationTypes.GAUSS:
            from algorithm.mutation_real.gauss import Gauss
            return Gauss(probability, start_point, end_point)