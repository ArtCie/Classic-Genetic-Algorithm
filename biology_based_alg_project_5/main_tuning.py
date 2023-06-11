from mealpy.swarm_based import GWO
import numpy as np
from mealpy.tuner import Tuner



def evaluate(solution) -> list:
    return -(solution[1] + 47) * np.sin(np.sqrt(np.abs(solution[1] + solution[0] / 2 + 47))) - solution[0] * np.sin(np.sqrt(np.abs(solution[0] - (solution[1] + 47))))


problem = {
    "fit_func": evaluate,
    "lb": np.array([-512, -512]),
    "ub": np.array([512, 512])
}

problem_params = {
    "epoch": [5, 10, 100, 1000, 10000],
    "pop_size": [5, 10, 100, 1000, 10000]
}

term = {
  "max_fe": 10000
}

# TODO
"""
GWO has two parameters -> epochs and pop_size
This file set up tuner class which will find best parameters for our problem
Above you can see problem_params -> those epochs and pop_size will be checked (permutation!)
After this is done -> results are in history/tuning.csv file - attach results to our report :)
"""
if __name__ == "__main__":
    model = GWO.OriginalGWO(seed=42)

    tuner = Tuner(model, problem_params)
    tuner.execute(problem=problem, termination=term, n_trials=5, n_jobs=5, mode="thread", n_workers=5, verbose=True)

    tuner.export_results(save_path="history/", save_as="csv")

    best_position, best_fitness = tuner.resolve()

    print(best_position, best_fitness)
    print(tuner.problem.get_name())


