import random



def one_point_crossover(parent1, parent2):
    """
    Cruce de un solo punto aplicado a cadenas binarias.
    
    Parámetros:
    - parent1 (str): Primera cadena binaria (padre).
    - parent2 (str): Segunda cadena binaria (madre).
    
    Retorna:
    - tuple: Dos nuevas cadenas binarias (hijos) generadas por el cruce.
    """
    if len(parent1) <= 1 or len(parent2) <= 1:
        return parent1, parent2  # Evita error si la longitud de los padres es 1 o menor

    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

# Ejemplo de ejecución:
# random.seed(1)  # Para reproducibilidad
# parent1 = "11001100"
# parent2 = "00110011"
# one_point_crossover(parent1, parent2)
# Posible salida: ('11000011', '00111100') (puede variar debido a aleatoriedad)
