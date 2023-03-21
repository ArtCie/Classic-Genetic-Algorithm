from algorithm.cross.cross import Cross
from algorithm.population_repository import PopulationRepository


class ThreePoints(Cross):
    def __init__(self, probability: float):
        super().__init__(probability)

    @staticmethod
    def evaluate(population: PopulationRepository) -> PopulationRepository:
        pass  # PERFORM MAGIC
