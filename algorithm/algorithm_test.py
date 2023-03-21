from algorithm.genetic_algorithm_calculator import GeneticAlgorithmCalculator


def run():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-10, range_b=10, population_size=2,
                                                              number_of_bits=6, epoch_number=1,
                                                              best_and_tournament_chromosome_amount=10,
                                                              elite_strategy_amount=2, cross_probability=0.8,
                                                              mutation_probability=1, inversion_probability=1,
                                                              selection_method=0, cross_method=0, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()


run()
