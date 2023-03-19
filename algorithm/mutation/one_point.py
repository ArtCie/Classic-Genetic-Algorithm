from algorithm.mutation.mutation import Mutation
from algorithm.population import Population


class OnePoint(Mutation):
    def __init__(self, probability: float):
        super().__init__(probability)

    @staticmethod
    def evaluate(population: Population) -> Population:
        pass  # PERFORM MAGIC
