from algorithm.chromosome import Chromosome

import numpy as np


class Individual:
    def __init__(self, x1: np.array, x2: np.array):
        self.chromosome_1 = Chromosome(x1)
        self.chromosome_2 = Chromosome(x2)
