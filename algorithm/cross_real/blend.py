from algorithm.cross_real.cross_real import CrossReal
from algorithm.population_repository import PopulationRepository

import numpy as np


class Blend(CrossReal):
    def __init__(self, probability: float):
        super().__init__(probability)

    def evaluate(self, population_repository: PopulationRepository) -> None:
        population = population_repository.population
        np.random.shuffle(population)
        K, R = np.random.random(), np.random.random()
        p = (1 + 2 * K) * R - K
        p_prim = 1 - p

        for index, value in enumerate(range(population_repository.population_size // 2)):
            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                x1, x2 = population[index * 2].chromosome_1.value, population[index * 2].chromosome_2.value
                y1, y2 = population[index * 2 + 1].chromosome_1.value, population[index * 2 + 1].chromosome_2.value

                population[index * 2].chromosome_1.value = p_prim * x1 + p * x2
                population[index * 2].chromosome_2.value = p_prim * y1 + p * y2

                population[index * 2 + 1].chromosome_1.value = p_prim * x2 + p * x1
                population[index * 2 + 1].chromosome_2.value = p_prim * y2 + K * y1
