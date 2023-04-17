from algorithm.cross_real.cross_real import CrossReal
from algorithm.population_repository import PopulationRepository
from functions.function_handler import FunctionHandler

import numpy as np


class Linear(CrossReal):
    def __init__(self, probability: float, function_handler: FunctionHandler):
        super().__init__(probability)
        self.function_handler = function_handler

    def evaluate(self, population_repository: PopulationRepository) -> None:
        population = population_repository.population
        np.random.shuffle(population)

        for index, value in enumerate(range(population_repository.population_size // 2)):
            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                x1, x2 = population[index * 2].chromosome_1.value, population[index * 2].chromosome_2.value
                y1, y2 = population[index * 2 + 1].chromosome_1.value, population[index * 2 + 1].chromosome_2.value

                temp_values = [
                    [0.5 * (x1 + x2), 0.5 * (y1 + y2)],
                    [1.5 * x1 - 0.5 * x2, 1.5 * y1 - 0.5 * y2],
                    [-0.5 * x1 + 1.5 * x2, -0.5 * y1 + 1.5 * y2]
                ]

                evals = [self.function_handler.evaluate([temp_values[0][0], temp_values[0][1]]),
                         self.function_handler.evaluate([temp_values[1][0], temp_values[1][1]]),
                         self.function_handler.evaluate([temp_values[2][0], temp_values[2][1]])]

                sorted_temp_values = [x for _, x in sorted(zip(evals, temp_values), key=lambda pair: pair[0])]

                population[index * 2].chromosome_1.value = sorted_temp_values[0][0]
                population[index * 2].chromosome_2.value = sorted_temp_values[0][1]

                population[index * 2 + 1].chromosome_1.value = sorted_temp_values[1][0]
                population[index * 2 + 1].chromosome_2.value = sorted_temp_values[1][1]
