import random


def initialize_population(size, dimensions, bit_length=10):
    """
    Inicializa una población de individuos representados en binario.
    
    Parámetros:
    - size (int): Tamaño de la población (cantidad de individuos).
    - dimensions (int): Número de dimensiones o variables que representa cada individuo.
    - bit_length (int, opcional): Longitud en bits de la representación de cada variable. Por defecto, 10.
    
    Retorna:
    - list: Lista de cadenas binarias representando la población.
    """
    if dimensions <= 0:
        raise ValueError("Error: 'dimensions' debe ser mayor a 0. Verifica que 'resources' no esté vacío.")

    population = ["".join(random.choice("01") for _ in range(dimensions * bit_length)) for _ in range(size)]
    
    # Verificar que la población no esté vacía
    if not population or all(ind == "" for ind in population):
        raise ValueError("Error: La población generada está vacía.")


    return population

# Ejemplo de ejecución:
# random.seed(1)  # Para reproducibilidad
# population(2, 2, 4)
# Salida esperada (puede variar con otro seed): ['01101001', '10011011']

def binary_to_decimal(binary_str, bounds, bit_length=10):
    """
    Convierte una cadena binaria en una lista de valores decimales dentro de los límites dados.
    """
    step = (bounds[1] - bounds[0]) / (2**bit_length - 1)  # Determina el paso de conversión
    
    decimal_values = [bounds[0] + int(binary_str[i:i+bit_length], 2) * step 
                      for i in range(0, len(binary_str), bit_length)]

    return decimal_values


# Ejemplo de ejecución:
# binary_to_decimal('01101001', (0, 10), 4)
# Cálculo:
# step = (10 - 0) / (2⁴ - 1) = 10 / 15 ≈ 0.6667
# 0110 → 6 → 0 + 6 * 0.6667 = 4.0
# 1001 → 9 → 0 + 9 * 0.6667 = 6.0
# Salida esperada: [4.0, 6.0]

def decimal_to_binary(decimal_values, bounds, bit_length=10):
    """
    Convierte una lista de valores decimales en una cadena binaria respetando los límites.
    
    Parámetros:
    - decimal_values (list): Lista de valores decimales a convertir.
    - bounds (tuple): Límite inferior y superior para la conversión (min, max).
    - bit_length (int, opcional): Longitud en bits de cada variable codificada. Por defecto, 10.
    
    Retorna:
    - str: Cadena binaria resultante de la conversión.
    """
    step = (bounds[1] - bounds[0]) / (2**bit_length - 1)  # Determina el paso de conversión
    return "".join(format(int((val - bounds[0]) / step), f'0{bit_length}b') for val in decimal_values)

# Ejemplo de ejecución:
# decimal_to_binary([4.0, 6.0], (0, 10), 4)
# Cálculo:
# step = (10 - 0) / (2⁴ - 1) = 10 / 15 ≈ 0.6667
# 4.0 / 0.6667 ≈ 6 → 0110
# 6.0 / 0.6667 ≈ 9 → 1001
# Salida esperada: '01101001'