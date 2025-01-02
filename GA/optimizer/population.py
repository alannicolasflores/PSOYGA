import numpy as np

def initialize_population(size, dimensions, bounds):
    return [np.random.uniform(bounds[0], bounds[1], dimensions).tolist() for _ in range(size)]
