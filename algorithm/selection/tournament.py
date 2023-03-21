from algorithm.selection.selection import Selection
from algorithm.population_repository import PopulationRepository


class Tournament(Selection):
    def __init__(self, chromosome_amount: int):
        self.chromosome_amount = chromosome_amount

    @staticmethod
    def evaluate(population: PopulationRepository) -> PopulationRepository:
        pass  # PERFORM MAGIC
