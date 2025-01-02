import random

def tournament_selection(population, fitness, k=3):
    selected = []
    for _ in range(2):
        participants = random.sample(list(zip(population, fitness)), k)
        selected.append(min(participants, key=lambda p: p[1])[0])
    return selected
