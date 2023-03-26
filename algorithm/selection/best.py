from algorithm.selection.selection import Selection
from algorithm.population_repository import PopulationRepository


class Best(Selection):
    def __init__(self, chromosome_amount: int):
        self.chromosome_amount = chromosome_amount

    def evaluate(self, population: PopulationRepository, function_values: list) -> None:
        pass  # PERFORM MAGIC
