from algorithm.individual import Individual
from algorithm.chromosome import Chromosome

import numpy as np


class PopulationRepository:
    def __init__(self, start_point: float, finish_point: float, precision: int, population_size: int):
        self.start_point = start_point
        self.finish_point = finish_point
        self.precision = precision
        self.population_size = population_size
        self.chromosome_length = self._get_chromosome_length()
        self.decode_const_value = (self.finish_point - self.start_point) / (2 ** self.chromosome_length - 1)
        self._population = self._populate()

    def _get_chromosome_length(self):
        return int(np.ceil(np.log2((self.finish_point - self.start_point) * 10**self.precision + 1)))

    def _populate(self):
        return [
            Individual(x1, x2) for x1, x2 in np.random.randint(2, size=(self.population_size, 2, self.chromosome_length))
        ]

    @property
    def population(self) -> list:
        return self._population

    def decode_population(self):
        return np.array([self._decode_individual(individual) for individual in self.population])

    def _decode_individual(self, individual: Individual):
        return np.array([self._decode_chromosome(individual.chromosome_1), self._decode_chromosome(individual.chromosome_2)])

    def _decode_chromosome(self, chromosome: Chromosome):
        str_chromosome_list = np.array2string(chromosome.value, separator="")[1:-1]
        return self.start_point + int(str_chromosome_list, 2) * self.decode_const_value
