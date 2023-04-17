from algorithm.cross_real.cross_real import CrossReal
from algorithm.population_repository import PopulationRepository
import numpy as np

class Arithmetic(CrossReal):
    def __init__(self, probability: float):
        super().__init__(probability)

    def evaluate(self, population_repository : PopulationRepository) -> None:

        population = population_repository.population
        np.random.shuffle(population)
        K = np.random.random()
        K_prim = 1 - K

        for index, value in enumerate(range(population_repository.population_size // 2)):
            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                x1, x2 = population[index * 2].chromosome_1.value, population[index * 2].chromosome_2.value
                y1, y2 = population[index * 2 + 1].chromosome_1.value, population[index * 2 + 1].chromosome_2.value

                population[index * 2].chromosome_1.value = K * x1 + K_prim * x2
                population[index * 2].chromosome_2.value = K * y1 + K_prim * y2

                population[index * 2 + 1].chromosome_1.value = K_prim * x1 + K * x2
                population[index * 2 + 1].chromosome_2.value = K_prim * y1 + K * y2
