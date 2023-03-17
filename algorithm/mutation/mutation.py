from abc import ABC, abstractmethod
from algorithm.population import Population
from enum import IntEnum


class Mutation(ABC):
    def __init__(self, probability: float):
        self.PROBABILITY = probability

    @staticmethod
    @abstractmethod
    def evaluate(population: Population) -> Population:
        pass


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