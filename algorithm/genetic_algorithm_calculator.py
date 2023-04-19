import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import time
import csv

from algorithm.population_repository import PopulationRepository
from functions.eggholder_function_calculator import EggholderFunctionCalculator
from functions.function_handler import FunctionHandler

# from algorithm.cross_binary.cross_binary import CrossTypes
from algorithm.cross_real.cross_real import CrossTypes
from algorithm.selection.selection import SelectionTypes
from algorithm.mutation.mutation import MutationTypes
from algorithm.mutation_real.mutation_real import MutationTypes
from algorithm.inversion.inversion import Inversion


class GeneticAlgorithmCalculator:
    def __init__(self, range_a: int, range_b: int, population_size: int, number_of_bits:int, epoch_number: int,
                 best_and_tournament_chromosome_amount: int, elite_strategy_amount: int,
                 cross_probability: float, mutation_probability: float, inversion_probability: float,
                 selection_method: int, cross_method: int, mutation_method: int, is_max: int):
        self.function_handler = FunctionHandler(EggholderFunctionCalculator(), is_reversed=not is_max)
        self.population_repository = PopulationRepository(range_a, range_b, number_of_bits, population_size)
        self.selection_method = SelectionTypes.get_selection_by_type(selection_method, best_and_tournament_chromosome_amount)
        # self.mutation_method = MutationTypes.get_mutation_by_type(mutation_method, mutation_probability)
        self.mutation_method = MutationTypes.get_mutation_by_type(mutation_method, mutation_probability, range_a, range_b)
        self.inversion_method = Inversion(inversion_probability)
        # self.cross_method = CrossTypes.get_cross_by_type(cross_method, cross_probability)
        self.cross_method = CrossTypes.get_cross_by_type(cross_method, cross_probability, self.function_handler)
        self.EPOCH_NUMBER = epoch_number
        self.elite_strategy_amount = elite_strategy_amount
        self.best = []
        self.avg = []
        self.diff = []
        self.std_dev = []
        self.elapsed_time = 0

    def run(self):
        start_time = time.time()
        for epoch_number in range(self.EPOCH_NUMBER):
            decoded_population = self.population_repository.decode_population()
            function_values = np.array(list(map(self.function_handler.evaluate, decoded_population)))
            self.avg.append(sum(function_values)/len(function_values))
            self.std_dev.append(np.std(function_values))
            # self._draw_values(decoded_population, function_values)
            elite_squad = self._get_elite_squad(function_values)

            self.selection_method.evaluate(self.population_repository, function_values)
            self.cross_method.evaluate(self.population_repository)
            self.mutation_method.evaluate(self.population_repository)
            # self.inversion_method.evaluate(self.population_repository)

            self._swap_elite_squad(elite_squad)
        end_time = time.time()

        self.elapsed_time = end_time - start_time

        print("TIME NEEDED [s]: ",self.elapsed_time)
        print(f"VALUE TO FIND -> -959.6407 YOUR VALUE {self.best[-1]}")

        self._draw_best()
        self._draw_avg()
        self._draw_diff()
        self._draw_std_dev()

        self._save_to_file()

    def _get_elite_squad(self, function_values: np.array):
        best_individuals = np.argsort(function_values)[:self.elite_strategy_amount]
        if len(self.best) > 0 and self.best[-1] != np.sort(function_values)[0]:
            print(f"NEW BEST! {np.sort(function_values)[0]}")
        self.best.append(np.sort(function_values)[0])
        return deepcopy([self.population_repository.population[index] for index in best_individuals])

    def _swap_elite_squad(self, elite_squad: list):
        for index, individual in enumerate(elite_squad):
            self.population_repository.population[index] = individual

    # @staticmethod
    # def _draw_values(decoded_population, function_values):
    #     fig = plt.figure(figsize=(12, 12))
    #     ax = fig.add_subplot(projection='3d')
    #     for index, value in enumerate(decoded_population):
    #         ax.scatter(value[0], value[1], function_values[index])
    #     plt.show()

    def _draw_best(self):
        plt.scatter([i for i in range(0, len(self.best))], self.best)
        plt.title("Plot - best value per epoch")
        plt.xlabel("epoch")
        plt.ylabel("value")
        plt.show()

    def _draw_avg(self):
        plt.scatter([i for i in range(0, len(self.avg))], self.avg)
        plt.title("Plot - average value per epoch")
        plt.xlabel("epoch")
        plt.ylabel("value")
        plt.show()

    def _draw_diff(self):
        diff_t = [0]
        for i in range(len(self.best) - 1):
            difference = abs(self.best[i+1] - self.best[i])
            diff_t.append(difference)
        self.diff = diff_t
        plt.scatter([i for i in range(0, len(diff_t))], diff_t)
        plt.title("Plot - difference between bests in each epoch")
        plt.xlabel("epoch")
        plt.ylabel("value")
        plt.show()

    def _draw_std_dev(self):
        plt.scatter([i for i in range(0, len(self.std_dev))], self.std_dev)
        plt.title("Plot - standard devation value per epoch")
        plt.xlabel("epoch")
        plt.ylabel("value")
        plt.show()

    def _save_to_file(self):
        combined_data = list(zip(self.best , self.avg,  self.std_dev, self.diff))
        headers = ["best_per_epoch", "avg_value_per_epoch", "_std_per_epoch", "difference_between_bests_per_epoch"]

        with open('output.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the timestamp in the first row
            csv_writer.writerow(["Elapsed Time",self.elapsed_time])

            # Write the headers in the second row
            csv_writer.writerow(headers)

            # Write the data
            for row in combined_data:
                csv_writer.writerow(row)

    @property
    def get_time(self):
        return self.elapsed_time