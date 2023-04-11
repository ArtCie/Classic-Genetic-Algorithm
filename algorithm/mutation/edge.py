import numpy as np

from algorithm.mutation.mutation import Mutation
from algorithm.population_repository import PopulationRepository
from algorithm.individual import Individual
from algorithm.chromosome import Chromosome


class Edge(Mutation):
    def __init__(self, probability: float):
        super().__init__(probability)

    def evaluate(self, population_repository: PopulationRepository) -> None:
        population = population_repository.population
        np.vectorize(self.mutate_individual, otypes="?")(population)

    def mutate_individual(self, individual: Individual):
        self._mutate_chromosome(individual.chromosome_1)
        self._mutate_chromosome(individual.chromosome_2)

    def _mutate_chromosome(self, chromosome: Chromosome):
        if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
            current_value = chromosome.value
            index_to_update = np.random.choice([0,len(current_value)])
            current_value[index_to_update] = self._negate_value(current_value[index_to_update])
