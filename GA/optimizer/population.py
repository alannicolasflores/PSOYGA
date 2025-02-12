import random

def population(size, dimensions, bit_length=10):
    """
    Inicializa la población con individuos representados en binario.
    """
    return ["".join(random.choice("01") for _ in range(dimensions * bit_length)) for _ in range(size)]

def binary_to_decimal(binary_str, bounds, bit_length=10):
    """
    Convierte una cadena binaria en una lista de valores decimales dentro de los límites dados.
    """
    step = (bounds[1] - bounds[0]) / (2**bit_length - 1)
    return [bounds[0] + int(binary_str[i:i+bit_length], 2) * step for i in range(0, len(binary_str), bit_length)]

def decimal_to_binary(decimal_values, bounds, bit_length=10):
    """
    Convierte una lista de valores decimales en una cadena binaria.
    """
    step = (bounds[1] - bounds[0]) / (2**bit_length - 1)
    return "".join(format(int((val - bounds[0]) / step), f'0{bit_length}b') for val in decimal_values)
