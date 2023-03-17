from algorithm.cross.cross import Cross
from algorithm.population import Population


class Homo(Cross):
    def __init__(self, probability: float):
        super().__init__(probability)

    @staticmethod
    def evaluate(population: Population) -> Population:
        pass  # PERFORM MAGIC
