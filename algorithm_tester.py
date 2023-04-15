from algorithm.genetic_algorithm_calculator import GeneticAlgorithmCalculator


def run():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=10, epoch_number=200,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=10, cross_probability=0.6,
                                                              mutation_probability=0.7, inversion_probability=0.5,
                                                              selection_method=1, cross_method=1, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()
run()
