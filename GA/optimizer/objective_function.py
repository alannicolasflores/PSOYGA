import numpy as np

def rastrigin(x):
    return 10 * len(x) + sum([(xi**2 - 10 * np.cos(2 * np.pi * xi)) for xi in x])

def sphere(x):
    return sum([xi**2 for xi in x])

OBJECTIVE_FUNCTIONS = {
    "rastrigin": rastrigin,
    "sphere": sphere
}
