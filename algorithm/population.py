from algorithm.individual import Individual

import numpy as np


class Population:
    def __init__(self, start_point: float, finish_point: float, precision: int, population_size: int):
        self.start_point = start_point
        self.finish_point = finish_point
        self.precision = precision
        self.population_size = population_size
        self.chromosome_length = self._get_chromosome_length()
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