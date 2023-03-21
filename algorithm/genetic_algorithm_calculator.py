import numpy as np

from algorithm.population_repository import PopulationRepository
from functions.eggholder_function_calculator import EggholderFunctionCalculator
from functions.function_handler import FunctionHandler
from algorithm.cross.cross import CrossTypes
from algorithm.selection.selection import SelectionTypes
from algorithm.inversion.inversion import Inversion
from algorithm.mutation.mutation import MutationTypes

from algorithm.cross.cross import Cross
from algorithm.selection.selection import Selection
from algorithm.inversion.inversion import Inversion
from algorithm.mutation.mutation import Mutation


class GeneticAlgorithmCalculator:
    def __init__(self, range_a: int, range_b: int, population_size: int, number_of_bits:int, epoch_number: int,
                 best_and_tournament_chromosome_amount: int, elite_strategy_amount: int,
                 cross_probability: float, mutation_probability: float, inversion_probability: float,
                 selection_method: int, cross_method: int, mutation_method: int, is_max: int):
        self.population_repository = PopulationRepository(range_a, range_b, number_of_bits, population_size)
        self.selection_method = SelectionTypes.get_selection_by_type(selection_method, best_and_tournament_chromosome_amount)
        self.mutation_method = MutationTypes.get_mutation_by_type(mutation_method, mutation_probability)
        self.inversion_method = Inversion(inversion_probability)
        self.cross_method = CrossTypes.get_cross_by_type(cross_method, cross_probability)
        self.EPOCH_NUMBER = epoch_number
        self.elite_strategy_amount = elite_strategy_amount
        self.function_handler = FunctionHandler(EggholderFunctionCalculator(), is_reversed=not is_max)

    def run(self):
        for epoch_number in range(self.EPOCH_NUMBER):
            decoded_population = self.population_repository.decode_population()
            function_values = list(map(self.function_handler.evaluate, decoded_population))
            elite_squad = self._get_elite_squad(function_values)

            # self.selection_method.evaluate(self.population)
            # self.cross_method.evaluate(self.population)
            self.mutation_method.evaluate(self.population_repository)
            self.inversion_method.evaluate(self.population_repository)
        # TODO
        # after each epoch -> evaluate results
        # print best value
        # add class for graph
        # implement mutation/inversion/cross/selection -> each class should have probability field

    def _get_elite_squad(self, function_values: list):
        best_individuals = np.argsort(function_values)[:self.elite_strategy_amount]
        return [self.population_repository.population[index] for index in best_individuals]
