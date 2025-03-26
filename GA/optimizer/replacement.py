from .population import binary_to_decimal

def replace_population(old_population, new_population, fitness, obj_func, bounds, bit_length=10, elitism=True):
    """
    Mantiene los mejores individuos para la siguiente generación con elitismo fuerte.
    
    Parámetros:
    - old_population (list): Población anterior.
    - new_population (list): Nueva población generada.
    - fitness (list): Lista de valores de aptitud (fitness) de la población anterior.
    - obj_func (func): Función objetivo para evaluar los individuos.
    - bounds (tuple): Límites inferior y superior para la conversión de valores decimales.
    - bit_length (int, opcional): Longitud en bits de la representación de cada variable. Por defecto, 10.
    - elitism (bool, opcional): Indica si se preserva el mejor individuo. Por defecto, True.
    
    Retorna:
    - list: Nueva población después del reemplazo.
    """
    # Convertir individuos binarios a decimales antes de calcular fitness
    decoded_new_population = [binary_to_decimal(ind, bounds, bit_length) for ind in new_population]
    
    # Calcular fitness de la nueva población
    new_fitness = [obj_func(ind) for ind in decoded_new_population]

    # Combinar las dos poblaciones
    combined = old_population + new_population
    combined_fitness = fitness + new_fitness

    # Ordenar de mayor a menor fitness
    sorted_population = sorted(zip(combined, combined_fitness), key=lambda x: x[1], reverse=True)

    if elitism:
        # Extraer el mejor individuo
        best_individual = sorted_population[0][0]  # Mejor individuo
        best_fitness = sorted_population[0][1]  # Su fitness

        # Reemplazar la peor solución con el mejor individuo
        new_population = [ind for ind, _ in sorted_population[:len(old_population) - 1]]
        new_population.append(best_individual)  # Asegurar que el mejor pase

        # Imprimir para verificar si realmente se mantiene el mejor
        print(f"Mejor individuo preservado con aptitud = {best_fitness}")
    else:
        # Tomar los mejores sin elitismo
        new_population = [ind for ind, _ in sorted_population[:len(old_population)]]

    return new_population

# Ejemplo de ejecución:
# old_pop = ['1100', '1010', '0111', '1001']
# new_pop = ['1111', '0000', '1011', '0110']
# fitness = [0.8, 0.6, 0.9, 0.7]
# obj_func = lambda x: sum(x)  # Función objetivo de ejemplo
# bounds = (0, 10)
# replace_population(old_pop, new_pop, fitness, obj_func, bounds, bit_length=4, elitism=True)
# Posible salida: Nueva población con elitismo aplicado
