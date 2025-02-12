import random
from optimizer.population import initialize_population, binary_to_decimal
from optimizer import objective_function, selection, crossover, mutation, replacement
from config import SETTINGS
from optimizer.utils import preprocess_resource_data

def optimize_resources(student_knowledge, student_styles, resources):
    """
    Ejecuta la optimización de selección de recursos educativos con mensajes de depuración.
    """

    generations = SETTINGS["generations"]
    pop_size = SETTINGS["population_size"]
    w_a = SETTINGS["weights"]["w_a"]
    w_d = SETTINGS["weights"]["w_d"]
    bounds = SETTINGS["bounds"]

    # Preprocesar los datos de los recursos
    processed_resources = preprocess_resource_data(resources, student_knowledge, student_styles)
    print("Recursos procesados:")
    for idx, res in enumerate(processed_resources):
        print(f"Recurso {idx + 1}: Adecuacion = {res.get('adequacy')}, Dificultad = {res.get('difficulty')}, Conocimiento = {res.get('knowledge')}")

    # Inicializar la población (cada individuo es una cadena binaria)
    population_data = initialize_population(pop_size, len(resources))
    print("\nPoblacion inicial (en formato binario):")
    for idx, ind in enumerate(population_data):
        print(f"Individuo {idx + 1}: {ind}")

    best_historical_fitness = float('-inf')

    for generation in range(generations):
        print(f"\n--- Generacion {generation + 1} ---")

        # Convertir la población binaria a valores decimales según los bounds
        decoded_population = [binary_to_decimal(ind, bounds) for ind in population_data]
        print("Poblacion decodificada:")
        for idx, dec in enumerate(decoded_population):
            print(f"Individuo {idx + 1}: {dec}")

        # Calcular la aptitud de cada individuo
        fitness = []
        for idx, individuo in enumerate(decoded_population):
            fit_ind = 0
            print(f"\nCalculando fitness para el Individuo {idx + 1}:")
            for i, resource in enumerate(processed_resources):
                # Calcular el valor del objetivo para el recurso i
                score = objective_function.educational_objective(
                    adequacy=resource["adequacy"],
                    difficulty=resource["difficulty"],
                    knowledge=resource["knowledge"],
                    w_a=w_a,
                    w_d=w_d
                )
                contrib = score * individuo[i]
                fit_ind += contrib
                print(f"  Recurso {i + 1}: score = {score}, factor = {individuo[i]}, contribucion = {contrib}")
            fitness.append(fit_ind)
            print(f"Fitness total del Individuo {idx + 1}: {fit_ind}")

        # Mostrar estadísticas de la generación
        max_fit = max(fitness)
        avg_fit = sum(fitness) / len(fitness)
        min_fit = min(fitness)
        print(f"\nEstadisticas Generacion {generation + 1}: Max = {max_fit}, Promedio = {avg_fit}, Min = {min_fit}")

        # Selección de padres usando torneo
        parents = selection.tournament_selection(population_data, fitness, k=SETTINGS["selection"]["k"])
        print("\nPadres seleccionados (en formato binario):")
        for idx, parent in enumerate(parents):
            print(f"Padre {idx + 1}: {parent}")

        new_population = []
        crossover_rate = SETTINGS["crossover_rate"]

        # Generar la nueva población aplicando cruce y mutación
        while len(new_population) < pop_size:
            if random.random() < crossover_rate:
                child1, child2 = crossover.one_point_crossover(parents[0], parents[1])
                print("\nSe aplico cruce entre los padres:")
                print(f"  Padre 1: {parents[0]}")
                print(f"  Padre 2: {parents[1]}")
                print(f"  Hijo 1: {child1}")
                print(f"  Hijo 2: {child2}")
            else:
                child1, child2 = parents[0], parents[1]
                print("\nSin cruce (se seleccionan los mismos padres):")
                print(f"  Hijo 1: {child1}")
                print(f"  Hijo 2: {child2}")

            # Aplicar mutación a cada hijo
            mutated_child1 = mutation.mutate(child1, SETTINGS["mutation_rate"])
            mutated_child2 = mutation.mutate(child2, SETTINGS["mutation_rate"])
            print("  Tras mutacion:")
            print(f"    Hijo 1: {mutated_child1}")
            print(f"    Hijo 2: {mutated_child2}")

            new_population.append(mutated_child1)
            new_population.append(mutated_child2)

        # Reemplazar la población actual con la nueva, usando elitismo
        population_data = replacement.replace_population(
            population_data,
            new_population,
            fitness,
            sum,
            bounds,
            bit_length=10,
            elitism=True
        )
        print("\nPoblacion actualizada (en formato binario):")
        for idx, ind in enumerate(population_data):
            print(f"Individuo {idx + 1}: {ind}")

        # Actualizar y mostrar la mejor aptitud histórica
        best_fitness = max(fitness)
        if best_fitness > best_historical_fitness:
            best_historical_fitness = best_fitness

        print(f"Generacion {generation + 1}: Mejor aptitud historica = {best_historical_fitness}")

    return population_data, best_historical_fitness
