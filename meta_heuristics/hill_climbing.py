#https://machinelearningmastery.com/stochastic-hill-climbing-in-python-from-scratch/
from numpy import asarray
from numpy.random import randn
from numpy.random import rand
from numpy.random import seed
from matplotlib import pyplot
from math import sqrt, sin


def objective(x1,x2):
     return -(x2 + 47) * sin(sqrt(abs(x2 + x1/2 + 47))) - x1 * sin(sqrt(abs(x1 - (x2 + 47))))

# hill climbing local search algorithm
def hillclimbing(objective, bounds, n_iterations, step_size):
    # generate an initial point
    solution1 = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    solution2 = bounds[:, 0] + rand(len(bounds)) * (bounds[:, 1] - bounds[:, 0])
    # evaluate the initial point
    solution_eval = objective(solution1,solution2)
    # run the hill climb
    scores = list()
    scores.append(solution_eval)
    for i in range(n_iterations):
        # take a step
        candidate1 = solution1 + randn(len(bounds)) * step_size
        candidate2 = solution2 + randn(len(bounds)) * step_size
        # evaluate candidate point
        candidte_eval = objective(candidate1,candidate2)
        # check if we should keep the new point
        if candidte_eval <= solution_eval:
            # store the new point
            solution1,solution2, solution_eval = candidate1,candidate2, candidte_eval
            # keep track of scores
            scores.append(solution_eval)
            # report progress
            print('>%d f(%s,%s) = %.5f' % (i, solution1,solution2, solution_eval))
    return [solution1,solution2, solution_eval, scores]


# define range for input
bounds = asarray([[-512, 512]])
# define the total iterations
n_iterations = 10000
# define the maximum step size
step_size = 0.1
# perform the hill climbing search
best1,best2, score, scores = hillclimbing(objective, bounds, n_iterations, step_size)
print('Done!')
print('f(%s,%s) = %f' % (best1,best2, score))
# line plot of best scores
pyplot.plot(scores, '.-')
pyplot.xlabel('Improvement Number')
pyplot.ylabel('Evaluation f(x)')
pyplot.show()