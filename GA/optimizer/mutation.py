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
    for i in range(len(individual)):
        if random.random() < mutation_rate:  # Aplicar mutación con la probabilidad dada
            individual[i] = '0' if individual[i] == '1' else '1'  # Invertir el bit
    return "".join(individual)

# Ejemplo de ejecución:
# random.seed(1)  # Para reproducibilidad
# individual = "11001100"
# mutate(individual, 0.2)
# Posible salida: '11011100' (puede variar debido a aleatoriedad)