#https://machinelearningmastery.com/simulated-annealing-from-scratch-in-python/
from numpy import asarray
from numpy import exp
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
from matplotlib import pyplot

from math import sqrt, sin


def objective(x1,x2):
     return -(x2 + 47) * sin(sqrt(abs(x2 + x1/2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))

# simulated annealing algorithm
def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
    # generate an initial point
    best1 = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    best2 = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    best_eval = objective(best1,best2)
    # current working solution
    curr1,curr2, curr_eval = best1,best2, best_eval
    scores = list()
    # run the algorithm
    for i in range(n_iterations):
        # take a step
        candidate1 = curr1 + randn(len(bounds)) * step_size
        candidate2 = curr2 + randn(len(bounds)) * step_size
        # evaluate candidate point
        candidate_eval = objective(candidate1,candidate2)
        # check for new best solution
        if candidate_eval < best_eval:
            # store new best point
            best1,best2, best_eval = candidate1,candidate2, candidate_eval
            # keep track of scores
            scores.append(best_eval)
            # report progress
            print('>%d f(%s,%s) = %.5f' % (i, best1,best2, best_eval))
        # difference between candidate and current point evaluation
        diff = candidate_eval - curr_eval
        # calculate temperature for current epoch
        t = temp / float(i + 1)
        # calculate metropolis acceptance criterion
        metropolis = exp(-diff / t)
        # check if we should keep the new point
        if diff < 0 or rand() < metropolis:
            # store the new current point
            curr1,curr2, curr_eval = candidate1,candidate2, candidate_eval
    return [best1,best2, best_eval, scores]


# seed the pseudorandom number generator
# define range for input
bounds = asarray([[-512, 512]])
# define the total iterations
n_iterations = 10000
# define the maximum step size
step_size = 0.1
# initial temperature
temp = 10
# perform the simulated annealing search
best1,best2, score, scores = simulated_annealing(objective, bounds, n_iterations, step_size, temp)
print('Done!')
print('f(%s,%s) = %f' % (best1,best2, score))
# line plot of best scores
pyplot.plot(scores, '.-')
pyplot.xlabel('Improvement Number')
pyplot.ylabel('Evaluation f(x)')
pyplot.show()