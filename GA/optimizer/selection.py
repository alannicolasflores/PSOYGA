import random

def tournament_selection(population, fitness, k=3):
    """
    Realiza la selección por torneo para escoger individuos con mayor fitness.
    
    Parámetros:
    - population (list): Lista de individuos en la población.
    - fitness (list): Lista de valores de aptitud (fitness) correspondientes a cada individuo.
    - k (int, opcional): Cantidad de participantes en cada torneo. Por defecto, 3.
    
    Retorna:
    - list: Lista con dos individuos seleccionados.
    """
    selected = []
    for _ in range(2):  # Se seleccionan dos individuos
        participants = random.sample(list(zip(population, fitness)), k)  # Se escogen k participantes aleatoriamente
        selected.append(max(participants, key=lambda p: p[1])[0])  # Selecciona el individuo con mayor fitness
    return selected

# Ejemplo de ejecución:
# population = ['1100', '1010', '0111', '1001']
# fitness = [0.8, 0.6, 0.9, 0.7]
# tournament_selection(population, fitness, k=3)
# Posible salida esperada: ['0111', '1100'] (puede variar debido a aleatoriedad)