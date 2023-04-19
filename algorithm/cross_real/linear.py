from algorithm.cross_real.cross_real import CrossReal
from algorithm.individual import Individual
from algorithm.population_repository import PopulationRepository
from functions.function_handler import FunctionHandler

import numpy as np


class Linear(CrossReal):
    def __init__(self, probability: float, function_handler: FunctionHandler, range_a: float, range_b: float):
        super().__init__(probability, range_a, range_b)
        self.function_handler = function_handler

    def evaluate(self, population_repository: PopulationRepository) -> None:
        population = population_repository.population
        np.random.shuffle(population)

        new_pop = []

        while len(new_pop) < population_repository.population_size:
            index_1, index_2 = np.random.randint(0, len(population_repository.population), size=2)
            x1, y1 = population[index_1].chromosome_1.value, population[index_1].chromosome_2.value
            x2, y2 = population[index_2].chromosome_1.value, population[index_2].chromosome_2.value

            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                temp_values = [
                    [0.5 * (x1 + x2), 0.5 * (y1 + y2)],
                    [1.5 * x1 - 0.5 * x2, 1.5 * y1 - 0.5 * y2],
                    [-0.5 * x1 + 1.5 * x2, -0.5 * y1 + 1.5 * y2]
                ]

                # OVERFLOW !!!

                evals = [self.function_handler.evaluate([temp_values[0][0], temp_values[0][1]]),
                         self.function_handler.evaluate([temp_values[1][0], temp_values[1][1]]),
                         self.function_handler.evaluate([temp_values[2][0], temp_values[2][1]])]

                sorted_temp_values = [x for _, x in sorted(zip(evals, temp_values), key=lambda pair: pair[0])]

                new_pop.append(Individual(sorted_temp_values[0][0], sorted_temp_values[0][1]))
                new_pop.append(Individual(sorted_temp_values[1][0], sorted_temp_values[1][1]))
            else:
                new_pop.append(Individual(x1, y1))
                new_pop.append(Individual(x2, y2))

        population_repository.population = np.array(new_pop)
