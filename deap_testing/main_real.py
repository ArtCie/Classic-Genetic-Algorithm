import matplotlib.pyplot as plt
import random
from math import sqrt, sin
from deap import base
from deap import creator
from deap import tools
import time


def plot(x_data, y_data, title=""):
    plt.plot(x_data, y_data)
    plt.xlabel("Iteration number")
    plt.ylabel("Value")
    plt.title(title)
    plt.show()


def individual(icls):
    genome = list()
    genome.append(random.uniform(-512,512))
    genome.append(random.uniform(-512,512))
    return icls(genome)


#jeśli chcemy odbić funkcje * -1 _ normlanie * 1
def evaluate(x1: float, x2: float) -> float:
    return (-(x2 + 47) * sin(sqrt(abs(x2 + x1 / 2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))) * (1)

def fitnessFunction(individual):
    return evaluate(individual[0], individual[1]),

#maksymalizacja +1.0, minimalizacja -1.0
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()

toolbox.register('individual', individual, creator.Individual)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('evaluate', fitnessFunction)
toolbox.register('select', tools.selTournament, tournsize=3)
toolbox.register('mate', tools.cxBlend, alpha=0.01)
toolbox.register("mutate", tools.mutGaussian, mu = 5, sigma= 10)

sizePopulation = 100
probabilityMutation = 0.5
probabilityCrossover = 0.5
numberIteration = 100
numberSelection = 30

pop = toolbox.population(n=sizePopulation)
fitnesses = list(map(toolbox.evaluate, pop))
for ind, fit in zip(pop, fitnesses):
    ind.fitness.values = fit

g = 0

results_min = []
results_mean = []
results_std = []

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
        listElitism.append(tools.selBest(pop, 1)[0])
        #listElitism.append(tools.selWorst(pop, 1)[0])
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
    print("Best individual is %s, %s" % (best_ind,
                                         best_ind.fitness.values))
end_time = time.time()
execution_time = end_time - start_time
print("-- End of (successful) evolution --")
print("Execution time:", execution_time, "seconds")

x_range = [i for i in range(numberIteration)]
plot(x_range, results_min, title="Minimum plot")
plot(x_range, results_std, title="Std plot")
plot(x_range, results_mean, title="Mean plot")
