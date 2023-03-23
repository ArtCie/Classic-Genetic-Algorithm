from abc import ABC, abstractmethod
from algorithm.population_repository import PopulationRepository
from enum import IntEnum


class Cross(ABC):
    def __init__(self, probability: float):
        self.PROBABILITY = probability

    @abstractmethod
    def evaluate(self, population_repository: PopulationRepository) -> None:
        pass


class CrossTypes(IntEnum):
    ONE_POINT = 0
    TWO_POINTS = 1
    THREE_POINTS = 2
    HOMO = 3

    @staticmethod
    def get_names():
        return [cross_type.name for cross_type in CrossTypes]

    @staticmethod
    def get_cross_by_type(type, probability):
        if type == CrossTypes.ONE_POINT:
            from algorithm.cross.one_point import OnePoint
            return OnePoint(probability)
        if type == CrossTypes.TWO_POINTS:
            from algorithm.cross.two_points import TwoPoints
            return TwoPoints(probability)
        if type == CrossTypes.THREE_POINTS:
            from algorithm.cross.three_points import ThreePoints
            return ThreePoints(probability)
        from algorithm.cross.homo import Homo
        return Homo(probability)
