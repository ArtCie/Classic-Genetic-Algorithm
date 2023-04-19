from abc import ABC, abstractmethod
from algorithm.population_repository import PopulationRepository
from enum import IntEnum


class CrossReal(ABC):
    def __init__(self, probability: float, range_a: float, range_b: float):
        self.PROBABILITY = probability
        self.range_a = range_a
        self.range_b = range_b

    @abstractmethod
    def evaluate(self, population_repository: PopulationRepository) -> None:
        pass


class CrossTypes(IntEnum):
    ARITHMETIC = 0
    BLEND = 1
    BLX_ALPHA = 2
    BLX_ALPHA_BETA = 3
    LINEAR = 4
    AVERAGE = 5

    @staticmethod
    def get_names():
        return [cross_type.name for cross_type in CrossTypes]

    @staticmethod
    def get_cross_by_type(type, probability, function_handler, range_a, range_b):
        if type == CrossTypes.ARITHMETIC:
            from algorithm.cross_real.arithmetic import Arithmetic
            return Arithmetic(probability, range_a, range_b)
        if type == CrossTypes.BLEND:
            from algorithm.cross_real.blend import Blend
            return Blend(probability, range_a, range_b)
        if type == CrossTypes.BLX_ALPHA:
            from algorithm.cross_real.blx_alpha import BlxAlpha
            return BlxAlpha(probability, range_a, range_b)
        if type == CrossTypes.BLX_ALPHA_BETA:
            from algorithm.cross_real.blx_alpha_beta import BlxAlphaBeta
            return BlxAlphaBeta(probability, range_a, range_b)
        if type == CrossTypes.AVERAGE:
            from algorithm.cross_real.average import Average
            return Average(probability, range_a, range_b)
        from algorithm.cross_real.linear import Linear
        return Linear(probability, function_handler, range_a, range_b)
