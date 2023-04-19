import numpy as np

from algorithm.mutation_real.mutation_real import Mutation
from algorithm.population_repository import PopulationRepository
from algorithm.individual import Individual
from algorithm.chromosome import Chromosome


class Balanced(Mutation):
    def __init__(self, probability: float, start_point: float, end_point: float):
        super().__init__(probability, start_point, end_point)

    def evaluate(self, population_repository: PopulationRepository) -> None:
        population = population_repository.population
        np.vectorize(self.mutate_individual, otypes="?")(population)

    def mutate_individual(self, individual: Individual):
        if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
            if np.random.choice([0, 1]):
                self._mutate_chromosome(individual.chromosome_1)
            else:
                self._mutate_chromosome(individual.chromosome_2)

    def _mutate_chromosome(self, chromosome: Chromosome):
        if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
            chromosome.value = np.random.uniform(low=self.start_point, high=self.end_point)
