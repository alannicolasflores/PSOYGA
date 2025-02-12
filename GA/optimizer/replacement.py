from optimizer.population import binary_to_decimal

def replace_population(old_population, new_population, fitness, obj_func, bounds, bit_length=10, elitism=True):
    """
    Mantiene los mejores individuos para la siguiente generación con elitismo fuerte.
    """
    # Convertir individuos binarios a decimales antes de calcular fitness
    decoded_new_population = [binary_to_decimal(ind, bounds, bit_length) for ind in new_population]
    
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
