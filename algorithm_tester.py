from algorithm.genetic_algorithm_calculator import GeneticAlgorithmCalculator


def run():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=4, mutation_method=0,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def run2():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=400,
                                                              best_and_tournament_chromosome_amount=3,
                                                              elite_strategy_amount=10, cross_probability=0.2,
                                                              mutation_probability=0.0, inversion_probability=0.2,
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


def zad_00():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=0, mutation_method=0,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def zad_01():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=0, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def zad_20():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=2, mutation_method=0,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def zad_21():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=2, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def zad_30():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=3, mutation_method=0,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def zad_31():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=3, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def zad_40():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=4, mutation_method=0,
                                                              is_max=1)
    genetic_algorithm_calculator.run()


def zad_41():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=4, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def zad_50():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=5, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

def zad_51():
    genetic_algorithm_calculator = GeneticAlgorithmCalculator(range_a=-512, range_b=512, population_size=100,
                                                              number_of_bits=6, epoch_number=100,
                                                              best_and_tournament_chromosome_amount=30,
                                                              elite_strategy_amount=2, cross_probability=0.5,
                                                              mutation_probability=0.5, inversion_probability=0.0,
                                                              selection_method=1, cross_method=5, mutation_method=1,
                                                              is_max=1)
    genetic_algorithm_calculator.run()

zad_51()
