from algorithm.selection.selection import Selection
from algorithm.population_repository import PopulationRepository
import numpy as np


class Roulette(Selection):
    def evaluate(self, population: PopulationRepository, function_values: np.array) -> None:
        population_arr = population.population
        function_values = function_values * (-1)
        min_value = function_values.min()
        if min_value < 0:
            function_values += np.abs(min_value) + 1
        probabilities = np.array(function_values / np.sum(function_values))
        population.population = population_arr[np.random.choice(len(population_arr), len(population_arr),
                                                                replace=True, p=probabilities)]
