import random

def mutate(individual, mutation_rate):
    """
    Aplica mutación cambiando bits de la representación binaria con una probabilidad dada.
    
    Parámetros:
    - individual (str): Cadena binaria que representa un individuo.
    - mutation_rate (float): Probabilidad de mutación para cada bit (entre 0 y 1).
    
    Retorna:
    - str: Nueva cadena binaria después de aplicar la mutación.
    """
    individual = list(individual)  # Convertir la cadena en lista para modificar los bits
    
    # Para cromosomas de longitud 1, aplicar mutación con la probabilidad normal
    if len(individual) == 1:
        if random.random() < mutation_rate:
            individual[0] = '0' if individual[0] == '1' else '1'
        return "".join(individual)
    
    # Para cromosomas más largos, aplicar la mutación normal
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = '0' if individual[i] == '1' else '1'
    return "".join(individual)

# Ejemplo de ejecución:
# random.seed(1)  # Para reproducibilidad
# individual = "11001100"
# mutate(individual, 0.2)
# Posible salida: '11011100' (puede variar debido a aleatoriedad)