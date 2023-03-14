from algorithm.population import Population
from algorithm.cross.cross import Cross
from algorithm.selection.selection import Selection
from algorithm.inversion.inversion import Inversion
from algorithm.mutation.mutation import Mutation

class GeneticAlgorithmCalculator:
    def __init__(self, epoch_number: int, population: Population, cross_method: Cross, inversion_method: Inversion, mutation_method: Mutation, selection_method: Selection):
        self.EPOCH_NUMBER = epoch_number
        self.population = population
        self.cross_method = cross_method
        self.inversion_method = inversion_method
        self.mutation_method = mutation_method
        self.selection_method = selection_method

    def run(self):
        for epoch_number in range(self.EPOCH_NUMBER):
            self.selection_method.evaluate(self.population)
            self.cross_method.evaluate(self.population)
            self.mutation_method.evaluate(self.population)
            self.inversion_method.evaluate(self.population)
        # TODO
        # after each epoch -> evaluate results
        # print best value
        # add class for graph
        # implement mutation/inversion/cross/selection -> each class should have probability field