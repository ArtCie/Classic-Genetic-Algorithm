from algorithm.cross_real.cross_real import CrossReal
from algorithm.individual import Individual
from algorithm.population_repository import PopulationRepository

import numpy as np

class BlxAlpha(CrossReal):
    def __init__(self, probability: float, range_a: float, range_b: float):
        super().__init__(probability, range_a, range_b)

    def calculate_low(self,elem1,elem2,alpha,di):
        return min(elem1, elem2) - alpha * di
    
    def calculate_high(self,elem1,elem2,alpha,di):
        return max(elem1, elem2) + alpha * di

    def evaluate(self, population_repository : PopulationRepository) -> None:
        population = population_repository.population
        np.random.shuffle(population)
        new_pop = []

        while len(new_pop) < population_repository.population_size:
            index_1, index_2 = np.random.randint(0, len(population_repository.population), size=2)
            x1, y1 = population[index_1].chromosome_1.value, population[index_1].chromosome_2.value
            x2, y2 = population[index_2].chromosome_1.value, population[index_2].chromosome_2.value

            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                alpha = 0.00001
                di_x = abs(x1 - x2)
                di_y = abs(y1 - y2)

                low_x = self.calculate_low(x1,x2,alpha,di_x)
                high_x =  self.calculate_high(x1,x2,alpha,di_x)
                low_y = self.calculate_low(y1,y2,alpha,di_y)
                high_y = self.calculate_high(y1,y2,alpha,di_y)

                while low_x > self.range_b or low_x < self.range_a:
                    low_x = self.calculate_low(x1,x2,alpha,di_x)
                while high_x > self.range_b or high_x < self.range_a:
                    high_x =  self.calculate_high(x1,x2,alpha,di_x)
                while low_y > self.range_b or low_y < self.range_a:
                    low_y = self.calculate_low(y1,y2,alpha,di_y)
                while high_y > self.range_b or high_y < self.range_a:
                     high_y = self.calculate_high(y1,y2,alpha,di_y)

                new_pop.append(Individual(np.random.uniform(low=low_x, high=high_x), np.random.uniform(low=low_y, high=high_y)))
                new_pop.append(Individual(np.random.uniform(low=low_x, high=high_x), np.random.uniform(low=low_y, high=high_y)))

            else:
                new_pop.append(Individual(x1, y1))
                new_pop.append(Individual(x2, y2))

        population_repository.population = np.array(new_pop)
