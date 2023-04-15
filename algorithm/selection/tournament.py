from algorithm.selection.selection import Selection
from algorithm.population_repository import PopulationRepository
import random

import numpy as np

class Tournament(Selection):
    def __init__(self, chromosome_amount: int):
        self.chromosome_amount = chromosome_amount

    def split_dict(self,input_dict, chunk_size):
        items = list(input_dict.items())
        chunks = [dict(items[i:i + chunk_size]) for i in range(0, len(items), chunk_size)]
        return chunks

    def evaluate(self, population: PopulationRepository, function_values: list) -> None:
        decoded_pop = population.decode_population()
        #function_values = function_values * (-1)

        next_gen = []

        my_dict = dict()

        for i in range(len(decoded_pop)):
            my_dict[function_values[i]] = population.population[i]

        #sortowanie losowe słownika
        random_keys = random.sample(my_dict.keys(), len(my_dict))
        mixed_dict = {k: my_dict[k] for k in random_keys}

        #tworzenie mniejszych slownikow po X wartosci 
        smaller_dicts = self.split_dict(mixed_dict, 3)

        for i in smaller_dicts:
            j = {k: my_dict[k] for k in sorted(i)}
            lowest_values = list(j.values())[:1]
            next_gen.append(lowest_values)

        flattened_list = [item for sublist in next_gen for item in sublist]
        population.population = flattened_list