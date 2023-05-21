import pandas as pd
import multiprocessing

from sklearn import model_selection
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from deap import base
from deap import creator
from deap import tools
import time
from sklearn import metrics

import random


def SVCParameters(numberFeatures, icls):
    genome = list()

    # kernel
    listKernel = ["linear", "rbf", "poly", "sigmoid"]
    genome.append(listKernel[random.randint(0, 3)])
    # c
    k = random.uniform(0.1, 100)
    genome.append(k)
    # degree
    genome.append(random.randint(1, 5))
    # gamma
    gamma = random.uniform(0.001, 5)
    genome.append(gamma)
    # coeff
    coeff = random.uniform(0.01, 10)
    genome.append(coeff)

    return icls(genome)


def SVCParametersFitness(y, df, numberOfAtributtes, individual):
    split = 5
    cv = StratifiedKFold(n_splits=split)
    listColumnsToDrop=[] #lista cech do usuniecia

    dfSelectedFeatures=df.drop(df.columns[listColumnsToDrop], axis=1, inplace=False)
    mms = MinMaxScaler()
    df_norm = mms.fit_transform(dfSelectedFeatures)
    estimator = SVC(kernel=individual[0],C=individual[1],degree=individual[2],
                    gamma=individual[3],coef0=individual[4],random_state=101)

    resultSum = 0
    for train, test in cv.split(df_norm, y):
        estimator.fit(df_norm[train], y[train])
        predicted = estimator.predict(df_norm[test])
        expected = y[test]
        tn, fp, fn, tp = metrics.confusion_matrix(expected,
                                                  predicted).ravel()
        result = (tp + tn) / (tp + fp + tn + fn)  # w oparciu o macierze
        resultSum = resultSum + result  # zbieramy wyniki z poszczególnych etapów walidacji krzyżowej
    return resultSum / split,

def mutationSVC(individual):
    numberParamer = random.randint(0, len(individual) - 1)
    if numberParamer == 0:
        # kernel
        listKernel = ["linear", "rbf", "poly", "sigmoid"]
        individual[0] = listKernel[random.randint(0, 3)]
    elif numberParamer == 1:
        # C
        k = random.uniform(0.1, 100)
        individual[1] = k
    elif numberParamer == 2:
        # degree
        # individual[2] = random.uniform(0.01, 1)
        individual[2] = random.randint(1, 5)

    elif numberParamer == 3:
        # gamma
        gamma = random.uniform(0.01, 5)
        individual[3] = gamma
    elif numberParamer == 4:
        # coeff
        coeff = random.uniform(0.1, 20)
        individual[4] = coeff


pd.set_option('display.max_columns', None)

# ---------------- switch for test data
# df = pd.read_csv("data_example.csv")
#
# y = df['Status']
# df.drop('Status', axis=1, inplace=True)
#
# df.drop('ID', axis=1, inplace=True)
# df.drop('Recording', axis=1, inplace=True)
# -------

# ------------- main data - 1
df = pd.read_csv("data_main.csv")
df['class'] = df['class'].map({"Positive": 1, "Negative": 0})
df['Gender'] = df['Gender'].map({"Male": 1, "Female": 0})
y = df['class']

for column in df.columns[2:-1]:
    df[column] = df[column].map({"Yes": 1, "No": 0})

# -----------

# ---------- main data - 2
# df = pd.read_csv("data/heart_failure_clinical_records_dataset.csv")
# y = df['DEATH_EVENT']

numberOfAttributes = len(df.columns)
print(numberOfAttributes)

# ----- check standard score using SVC
mms = MinMaxScaler()
df_norm = mms.fit_transform(df)

clf = SVC()
scores = model_selection.cross_val_score(clf, df_norm, y, cv=5, scoring='accuracy', n_jobs=1)
print(scores.mean())


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
toolbox = base.Toolbox()

toolbox.register('individual', SVCParameters, numberOfAttributes, creator.Individual)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('evaluate', SVCParametersFitness, y, df, numberOfAttributes)
toolbox.register('select', tools.selWorst)
toolbox.register("mutate", mutationSVC)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=8)
    toolbox.register("map", pool.map)

    sizePopulation = 100
    probabilityMutation = 0.5
    probabilityCrossover = 0.5
    numberIteration = 100
    numberSelection = 30

    pop = toolbox.population(n=sizePopulation)
    fitnesses = list(toolbox.map(toolbox.evaluate, pop))
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
            # jesli maksymalizacja musi być selWorst, minimalizacja selBest
            listElitism.append(tools.selWorst(pop, 1)[0])
            # listElitism.append(tools.selWorst(pop, 1)[0])
        # for child1, child2 in zip(offspring[::2], offspring[1::2]):
        #     if random.random() < probabilityCrossover:
        #         toolbox.mate(child1, child2)
        #         del child1.fitness.values
        #         del child2.fitness.values

        for mutant in offspring:
            if random.random() < probabilityMutation:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
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
        best_ind = tools.selWorst(pop, 1)[0]
        print(f"Mean -> {mean}")
        print("Best individual is %s, %s" % (best_ind,
                                             best_ind.fitness.values))
    end_time = time.time()
    execution_time = end_time - start_time
    print("-- End of (successful) evolution --")
    print("Execution time:", execution_time, "seconds")
    print("MIN", sorted(results_min)[0])
    x_range = [i for i in range(numberIteration)]
