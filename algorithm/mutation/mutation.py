from abc import ABC, abstractmethod
from algorithm.population_repository import PopulationRepository
from enum import IntEnum


class Mutation(ABC):
    def __init__(self, probability: float):
        self.PROBABILITY = probability

    @abstractmethod
    def evaluate(self, population: PopulationRepository) -> PopulationRepository:
        pass

    @staticmethod
    def _negate_value(current_value: int) -> int:
        return int(current_value != 1)


class MutationTypes(IntEnum):
    ONE_POINT = 0
    TWO_POINTS = 1

    @staticmethod
    def get_names():
        return [mutation_type.name for mutation_type in MutationTypes]

    @staticmethod
    def get_mutation_by_type(type, probability):
        if type == MutationTypes.ONE_POINT:
            from algorithm.mutation.one_point import OnePoint
            return OnePoint(probability)
        from algorithm.mutation.two_points import TwoPoints
        return TwoPoints(probability)