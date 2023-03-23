from algorithm.cross.cross import Cross
from algorithm.population_repository import PopulationRepository
from algorithm.individual import Individual
from algorithm.chromosome import Chromosome

import numpy as np


class OnePoint(Cross):
    def __init__(self, probability: float):
        super().__init__(probability)

    def evaluate(self, population_repository: PopulationRepository) -> None:
        population = population_repository.population
        np.random.shuffle(population)
        for index, value in enumerate(range(population_repository.population_size // 2)):
            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                cross_point = np.random.randint(population_repository.chromosome_length * 2)
                merged_individual_1 = self.get_string_individual(population[index * 2])
                merged_individual_2 = self.get_string_individual(population[index * 2 + 1])

                new_individual_1 = merged_individual_1[:cross_point] + merged_individual_2[cross_point:]
                new_individual_2 = merged_individual_2[:cross_point] + merged_individual_1[cross_point:]

                population[index * 2].chromosome_1.value = np.array(list(new_individual_1[:population_repository.chromosome_length])).astype(int)
                population[index * 2].chromosome_2.value = np.array(list(new_individual_1[population_repository.chromosome_length:])).astype(int)

                population[index * 2 + 1].chromosome_1.value = np.array(list(new_individual_2[:population_repository.chromosome_length])).astype(int)
                population[index * 2 + 1].chromosome_2.value = np.array(list(new_individual_2[population_repository.chromosome_length:])).astype(int)

    @staticmethod
    def get_string_individual(individual):
        return np.array2string(individual.chromosome_1.value, separator="")[1:-1] + \
            np.array2string(individual.chromosome_2.value, separator="")[1:-1]