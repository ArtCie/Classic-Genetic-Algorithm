import matplotlib.pyplot as plt
from random import randint
import random
from math import sqrt, sin
import time
import numpy as np
from deap import base
from deap import creator
from deap import tools


def plot(x_data, y_data, title=""):
    plt.plot(x_data, y_data)
    plt.xlabel("Iteration number")
    plt.ylabel("Value")
    plt.title(title)
    plt.show()


def individual(icls):
    genome = list()
    for x in range(0, 40):
        genome.append(randint(0, 1))
    return icls(genome)

#jeśli chcemy odbić funkcje * -1 _ normlanie * 1
def evaluate(x1: float, x2: float) -> float:
    return (-(x2 + 47) * sin(sqrt(abs(x2 + x1 / 2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))) * (-1)


def _decode_individual(individual):
    x = individual[:20]
    y = individual[20:]
    return [_decode_chromosome(x), _decode_chromosome(y)]


def _decode_chromosome(value):
    start_point = -512
    finish_point = 512
    chromosome_length = 20
    const_value = (finish_point - start_point) / (2 ** chromosome_length - 1)
    str_chromosome_list = np.array2string(np.array(value), separator="")[1:-1]
    return start_point + int(str_chromosome_list, 2) * const_value


def fitnessFunction(individual):
    x, y = _decode_individual(individual)
    return evaluate(x, y),

#maksymalizacja +1.0, minimalizacja -1.0
creator.create("FitnessMin", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()

toolbox.register('individual', individual, creator.Individual)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('evaluate', fitnessFunction)

#toolbox.register('select', tools.selTournament, tournsize=3)
# switch selection method here
#toolbox.register('select', tools.selRoulette)
toolbox.register('select', tools.selBest)
#toolbox.register('select', tools.selNSGA2)

# switch crossover method here
#toolbox.register('mate', tools.cxOnePoint)
#toolbox.register('mate', tools.cxTwoPoint)
toolbox.register('mate', tools.cxOrdered)
#toolbox.register('mate', tools.cxPartialyMatched)

# switch mutation method here
toolbox.register('mutate', tools.mutShuffleIndexes)
#toolbox.register('mutate', tools.mutFlipBit)

sizePopulation = 100
probabilityMutation = 0.2
probabilityCrossover = 0.2
numberIteration = 400
numberSelection = 30

pop = toolbox.population(n=sizePopulation)
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

results_min = []
results_mean = []
results_std = []

g = 0
numberElitism = 1
start_time = time.time()
while g < numberIteration:
    g = g + 1
    print("-- Generation %i --" % g)
    offspring = toolbox.select(pop, numberSelection)
    offspring = list(map(toolbox.clone, offspring))
    offspring = random.choices(offspring, k=sizePopulation)
    listElitism = []
    for x in range(0, numberElitism):
        #jesli maksymalizacja musi być selWorst, minimalizacja selBest
        #listElitism.append(tools.selBest(pop, 1)[0])
        listElitism.append(tools.selWorst(pop, 1)[0])
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < probabilityCrossover:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values
    for mutant in offspring:
        if random.random() < probabilityMutation:
            toolbox.mutate(mutant, indpb=1)
            del mutant.fitness.values

    invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
    fitnesses = map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit
    print(" Evaluated %i individuals" % len(invalid_ind))
    pop[:] = offspring
    pop[:numberElitism] = listElitism
    fits = [ind.fitness.values[0] for ind in pop]
    length = len(pop)
    mean = sum(fits) / length
    sum2 = sum(x * x for x in fits)
    std = abs(sum2 / length - mean ** 2) ** 0.5

    results_min.append(min(fits))
    results_mean.append(mean)
    results_std.append(std)

    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (_decode_individual(best_ind),
                                         best_ind.fitness.values))
end_time = time.time()
execution_time = end_time - start_time
print("-- End of (successful) evolution --")
print("Execution time:", execution_time, "seconds")
print("MINNN",sorted(results_min)[0])
x_range = [i for i in range(numberIteration)]
plot(x_range, results_min, title="Minimum plot")
plot(x_range, results_std, title="Std plot")
plot(x_range, results_mean, title="Mean plot")