from algorithm.cross_real.cross_real import CrossReal
from algorithm.population_repository import PopulationRepository

import numpy as np


class BlxAlphaBeta(CrossReal):
    def __init__(self, probability: float):
        super().__init__(probability)

    def evaluate(self, population_repository: PopulationRepository) -> None:

        population = population_repository.population
        np.random.shuffle(population)
        alpha, beta = np.random.random(), np.random.random()

        for index, value in enumerate(range(population_repository.population_size // 2)):
            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                x1, x2 = population[index * 2].chromosome_1.value, population[index * 2].chromosome_2.value
                y1, y2 = population[index * 2 + 1].chromosome_1.value, population[index * 2 + 1].chromosome_2.value

                di_x = abs(x1 - x2)
                di_y = abs(y1 - y2)

                low_x, high_x = min(x1, x2) - alpha * di_x, max(x1, x2) + beta * di_x
                low_y, high_y = min(y1, y2) - alpha * di_y, max(y1, y2) + beta * di_y

                population[index * 2].chromosome_1.value = np.random.uniform(low=low_x, high=high_x)
                population[index * 2].chromosome_2.value = np.random.uniform(low=low_y, high=high_y)

                population[index * 2 + 1].chromosome_1.value = np.random.uniform(low=low_x, high=high_x)
                population[index * 2 + 1].chromosome_2.value = np.random.uniform(low=low_y, high=high_y)

    @staticmethod
    def get_string_individual(individual):
        return np.array2string(individual.chromosome_1.value, separator="")[1:-1] + \
            np.array2string(individual.chromosome_2.value, separator="")[1:-1]
