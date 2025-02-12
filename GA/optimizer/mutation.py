import random

def mutate(individual, mutation_rate):
    """
    Aplica mutación cambiando bits de la representación binaria.
    """
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = '0' if individual[i] == '1' else '1'
    return "".join(individual)
