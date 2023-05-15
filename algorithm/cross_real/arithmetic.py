from algorithm.cross_real.cross_real import CrossReal
from algorithm.individual import Individual
from algorithm.population_repository import PopulationRepository
import numpy as np
from copy import deepcopy

class Arithmetic(CrossReal):
    def __init__(self, probability: float, range_a: float, range_b: float):
        super().__init__(probability, range_a, range_b)

    def calculate_new_value_1(self,K,K_prim,x1,x2,y1,y2): 
        return K * x1 + K_prim * x2, K * y1 + K_prim * y2
    
    def calculate_new_value_2(self,K,K_prim,x1,x2,y1,y2):
        return K_prim * x1 + K * x2, K_prim * y1 + K * y2
    
    def evaluate(self, population_repository : PopulationRepository) -> None:

        population = population_repository.population
        np.random.shuffle(population)

        new_pop = []

        while len(new_pop) < population_repository.population_size:
            index_1, index_2 = np.random.randint(0, len(population_repository.population), size=2)
            x1, y1 = population[index_1].chromosome_1.value, population[index_1].chromosome_2.value
            x2, y2 = population[index_2].chromosome_1.value, population[index_2].chromosome_2.value

            if np.random.choice([0, 1], p=[1 - self.PROBABILITY, self.PROBABILITY]):
                K = np.random.random()
                K_prim = 1 - K

                new_value_1 = self.calculate_new_value_1(K,K_prim,x1,x2,y1,y2)
                new_value_2 = self.calculate_new_value_2(K,K_prim,x1,x2,y1,y2)

                while new_value_1[0] > self.range_b or new_value_1[0] < self.range_a  or new_value_1[1] > self.range_b or new_value_1[1] < self.range_a:
                    new_value_1 = (K,K_prim,x1,x2,y1,y2)

                while new_value_2[0] > self.range_b or new_value_2[0] < self.range_a or new_value_2[1] > self.range_b or new_value_2[1] < self.range_a:
                    new_value_2 = (K,K_prim,x1,x2,y1,y2)

                new_pop.append(Individual(new_value_1[0],new_value_1[1]))
                new_pop.append(Individual(new_value_2[0],new_value_2[1]))
            else:
                new_pop.append(Individual(x1, y1))
                new_pop.append(Individual(x2, y2))

        population_repository.population = np.array(new_pop)

