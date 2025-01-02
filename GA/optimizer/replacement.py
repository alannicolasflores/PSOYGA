def replace_population(old_population, new_population, fitness, obj_func):
    # Evaluar aptitud de los nuevos descendientes
    new_fitness = [obj_func(ind) for ind in new_population]

    # Combinar población actual con los nuevos descendientes
    combined = old_population + new_population
    combined_fitness = fitness + new_fitness

    # Ordenar por aptitud (menor es mejor) y seleccionar los mejores
    sorted_population = sorted(zip(combined, combined_fitness), key=lambda x: x[1])
    return [ind for ind, _ in sorted_population[:len(old_population)]]
