from abc import ABC, abstractmethod
from algorithm.population_repository import PopulationRepository
from enum import IntEnum


class Selection(ABC):
    @staticmethod
    @abstractmethod
    def evaluate(population: PopulationRepository) -> PopulationRepository:
        pass


class SelectionTypes(IntEnum):
    BEST = 0
    ROULETTE = 1
    TOURNAMENT = 2

    @staticmethod
    def get_names():
        return [selection_type.name for selection_type in SelectionTypes]

    @staticmethod
    def get_selection_by_type(type, best_and_tournament_chromosome_amount):
        if type == SelectionTypes.BEST:
            from algorithm.selection.best import Best
            return Best(best_and_tournament_chromosome_amount)
        if type == SelectionTypes.ROULETTE:
            from algorithm.selection.roulette import Roulette
            return Roulette()
        from algorithm.selection.tournament import Tournament
        return Tournament(best_and_tournament_chromosome_amount)
