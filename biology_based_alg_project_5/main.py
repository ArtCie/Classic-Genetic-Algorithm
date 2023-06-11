from mealpy.swarm_based import GWO
import numpy as np

from math import sqrt, sin


def evaluate(solution) -> list:
    return -(solution[1] + 47) * np.sin(np.sqrt(np.abs(solution[1] + solution[0] / 2 + 47))) - solution[0] * np.sin(np.sqrt(np.abs(solution[0] - (solution[1] + 47))))


problem = {
    "fit_func": evaluate,
    "lb": np.array([-512, -512]),
    "ub": np.array([512, 512])
}

model = GWO.OriginalGWO(epoch=100, pop_size=100, n_workers=10, seed=42)
best_position, best_fitness = model.solve(problem)
print(f"Best solution: {best_position}, Best fitness: {best_fitness}")

