import random

def one_point_crossover(parent1, parent2):
    """
    Cruce de un solo punto aplicado a cadenas binarias.
    """
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
