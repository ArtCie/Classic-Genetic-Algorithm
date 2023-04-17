from algorithm.selection.selection import Selection
from algorithm.population_repository import PopulationRepository

import numpy as np

class Best(Selection):
    def __init__(self, chromosome_amount: int):
        self.chromosome_amount = chromosome_amount

    def evaluate(self, population: PopulationRepository, function_values: list) -> None:
        decoded_pop = population.decode_population()
        #function_values = function_values * (-1)

        my_dict = dict()

        for i in range(len(decoded_pop)):
            my_dict[function_values[i]] = population.population[i]
        sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}

        #posortowany słownik po kluczach ktore są wartościami funkcji odcinamy te "najniższe wartości" słownika - w ktorych są składowane chromosomy
        lowest_values = list(sorted_dict.values())[:self.chromosome_amount]
        
        population.population = lowest_values