from algorithm.cross_real.cross_real import CrossReal
from algorithm.individual import Individual
from algorithm.population_repository import PopulationRepository

import numpy as np
from copy import deepcopy


class Average(CrossReal):
    def __init__(self, probability: float, range_a: float, range_b: float):
        super().__init__(probability, range_a, range_b)

    def evaluate(self, population_repository : PopulationRepository) -> None:

        population = population_repository.population
        np.random.shuffle(population)
        new_pop = []

        while len(new_pop) < population_repository.population_size:
            index_1, index_2 = np.random.randint(0, len(population_repository.population), size=2)
            x1, y1 = population[index_1].chromosome_1.value, population[index_1].chromosome_2.value
            x2, y2 = population[index_2].chromosome_1.value, population[index_2].chromosome_2.value

            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                new_pop.append(Individual((x1 + x2) / 2, (y1 + y2) / 2))
            else:
                new_pop.append(Individual(x1, x2))

        population_repository.population = np.array(new_pop)