import random

def mutate(individual, mutation_rate, bounds):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] += random.uniform(-1, 1)
            individual[i] = max(min(individual[i], bounds[1]), bounds[0])
    return individual
