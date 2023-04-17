from algorithm.genetic_algorithm_calculator import GeneticAlgorithmCalculator


def run():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=200,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=4, cross_probability=0.6,
                                                              mutation_probability=0.5, inversion_probability=0.4,
                                                              selection_method=1, cross_method=5, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def run2():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=400,
                                                              best_and_tournament_chromosome_amount=3,
                                                              elite_strategy_amount=10, cross_probability=0.2,
                                                              mutation_probability=0.2, inversion_probability=0.2,
                                                              selection_method=2, cross_method=0, mutation_method=2,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def run3():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=200,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=10, cross_probability=0.7,
                                                              mutation_probability=0.7, inversion_probability=0.5,
                                                              selection_method=0, cross_method=3, mutation_method=2,
                                                              is_max=1)
    genetic_algorithm_calculator.run()



run()
