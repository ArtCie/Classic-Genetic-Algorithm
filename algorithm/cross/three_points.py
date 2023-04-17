from algorithm.cross.cross import Cross
from algorithm.population_repository import PopulationRepository
from algorithm.individual import Individual
from algorithm.chromosome import Chromosome

import numpy as np

class ThreePoints(Cross):
    def __init__(self, probability: float):
        super().__init__(probability)

    def evaluate(self, population_repository : PopulationRepository) -> None:

        population = population_repository.population
        np.random.shuffle(population)

        new_pop = []

        while len(new_pop) < population_repository.population_size:
            random_indexes =  np.random.randint(0, len(population_repository.population), size=2)
            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                cross_point = np.random.choice(range(1,population_repository.chromosome_length * 2 - 1),3)
                if cross_point[0] == cross_point[1] or cross_point[0]== cross_point[2] or cross_point[1] == cross_point[2]:
                    pass
                cross_point = sorted(cross_point)

                merged_individual_1 = self.get_string_individual(population[random_indexes[0]])
                merged_individual_2 = self.get_string_individual(population[random_indexes[1]])

                new_individual_1 = merged_individual_1[:cross_point[0]] + merged_individual_2[cross_point[0]:cross_point[1]] + merged_individual_1[cross_point[1]:cross_point[2]] + merged_individual_2[cross_point[2]:]
                new_individual_2 = merged_individual_2[:cross_point[0]] + merged_individual_1[cross_point[0]:cross_point[1]] + merged_individual_2[cross_point[1]:cross_point[2]]+ merged_individual_1[cross_point[2]:]


                chromosome_1 = np.array(list(new_individual_1[:population_repository.chromosome_length])).astype(int)
                chromosome_2 = np.array(list(new_individual_1[population_repository.chromosome_length:])).astype(int)
                new_1 = Individual(chromosome_1,chromosome_2)

                chromosome_1 = np.array(list(new_individual_2[:population_repository.chromosome_length])).astype(int)
                chromosome_2 = np.array(list(new_individual_2[population_repository.chromosome_length:])).astype(int)
                new_2 = Individual(chromosome_1,chromosome_2)

                new_pop.append(new_1)
                new_pop.append(new_2)
            else:
                new_pop.append(population[random_indexes[0]])
                new_pop.append(population[random_indexes[1]])
        population_repository.population = np.array(new_pop)

    @staticmethod
    def get_string_individual(individual):
        return np.array2string(individual.chromosome_1.value, separator="")[1:-1] + \
            np.array2string(individual.chromosome_2.value, separator="")[1:-1]
