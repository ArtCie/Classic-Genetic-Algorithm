from algorithm.selection.selection import Selection
from algorithm.population import Population


class Tournament(Selection):
    def __init__(self, chromosome_amount: int):
        self.chromosome_amount = chromosome_amount

    @staticmethod
    def evaluate(population: Population) -> Population:
        pass  # PERFORM MAGIC
