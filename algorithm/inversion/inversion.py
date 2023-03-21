import numpy as np
from random import sample

from algorithm.population_repository import PopulationRepository
from algorithm.individual import Individual
from algorithm.chromosome import Chromosome


class Inversion:
    def __init__(self, probability: float):
        self.PROBABILITY = probability

    def evaluate(self, population_repository: PopulationRepository) -> None:
        population = population_repository.population
        np.vectorize(self._invert, otypes="?")(population)

    def _invert(self, individual: Individual):
        self._invert_chromosome(individual.chromosome_1)
        self._invert_chromosome(individual.chromosome_2)

    def _invert_chromosome(self, chromosome: Chromosome):
        if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
            current_value = chromosome.value
            start_index, end_index = sorted(sample(range(len(current_value)), 2))
            chromosome.value = np.array([*current_value[:start_index],
                                         *current_value[start_index: end_index + 1][::-1],
                                         *current_value[end_index + 1:]])
