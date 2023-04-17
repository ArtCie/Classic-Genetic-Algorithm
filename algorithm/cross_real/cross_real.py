from abc import ABC, abstractmethod
from algorithm.population_repository import PopulationRepository
from enum import IntEnum


class CrossReal(ABC):
    def __init__(self, probability: float):
        self.PROBABILITY = probability

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
    def get_cross_by_type(type, probability, function_handler):
        if type == CrossTypes.ARITHMETIC:
            from algorithm.cross_real.arithmetic import Arithmetic
            return Arithmetic(probability)
        if type == CrossTypes.BLEND:
            from algorithm.cross_real.blend import Blend
            return Blend(probability)
        if type == CrossTypes.BLX_ALPHA:
            from algorithm.cross_real.blx_alpha import BlxAlpha
            return BlxAlpha(probability)
        if type == CrossTypes.BLX_ALPHA_BETA:
            from algorithm.cross_real.blx_alpha_beta import BlxAlphaBeta
            return BlxAlphaBeta(probability)
        if type == CrossTypes.AVERAGE:
            from algorithm.cross_real.average import Average
            return Average(probability)
        from algorithm.cross_real.linear import Linear
        return Linear(probability, function_handler)
