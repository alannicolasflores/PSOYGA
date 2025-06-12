import random

from ..config import SETTINGS
from . import crossover, mutation, objective_function, replacement, selection
from .population import binary_to_decimal, initialize_population
from .utils import preprocess_resource_data


def optimize_resources(student_knowledge, student_styles, resources):
    """
    Ejecuta la optimización de selección de recursos educativos.
    
    Formato de salida:
    1. Recursos procesados:
       - Muestra la dificultad (1-3) y nivel de conocimiento requerido (1-3) de cada recurso
       - Dificultad: Nivel de complejidad del recurso
       - Conocimiento: Nivel de conocimiento actual del estudiante en el tema
    
    2. Rutas de aprendizaje:
       - Cada ruta representa una posible secuencia de recursos educativos
       - El porcentaje (0-100%) indica la intensidad recomendada de uso:
         * 100%: Uso completo del recurso
         * 75%: Uso mayoritario
         * 50%: Uso parcial
         * <50%: Uso opcional (no se muestra)
    
    3. Evaluación de recursos:
       - Porcentaje de uso: Intensidad recomendada de utilización del recurso
       - Adecuación: Qué tan bien se ajusta al estilo de aprendizaje (0=nada, 1=perfecto)
       - Puntuación: Calificación general del recurso para el estudiante
    
    4. Puntuaciones:
       - Total por ruta: Calidad general de la ruta de aprendizaje
       - Mejor aptitud: Puntuación de la mejor ruta encontrada hasta el momento
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
        print(f"Recurso {idx + 1}: Dificultad = {res.get('difficulty')}, Conocimiento = {res.get('knowledge')}")

    # Inicializar y decodificar la población
    population_data = initialize_population(pop_size, len(resources))
    decoded_population = [binary_to_decimal(ind, bounds) for ind in population_data]
    
    # Initialize best values
    best_historical_fitness = float('-inf')
    best_solution = None

    print("\n=== INICIO DE OPTIMIZACIÓN ===")
    print(f"Número de recursos: {len(resources)}")
    print(f"Tamaño de población: {pop_size}")
    print(f"Número de generaciones: {generations}")
    
    print("\n=== RECURSOS DISPONIBLES ===")
    for idx, res in enumerate(processed_resources):
        print(f"Recurso {idx + 1}:")
        print(f"  - Dificultad: {res.get('difficulty')}")
        print(f"  - Nivel de conocimiento requerido: {res.get('knowledge')}")
        print(f"  - Estilos de aprendizaje: {res.get('learning_styles')}")
    
    historial_generaciones = []
    for generation in range(generations):
        print(f"\n=== GENERACIÓN {generation + 1} ===")
        
        # Evaluate each learning path
        fitness = []
        for idx, individuo in enumerate(decoded_population):
            print(f"\nRuta de Aprendizaje {idx + 1}:")
            print("Recursos seleccionados:")
            fit_ind = 0
            
            for i, resource in enumerate(processed_resources):
                if individuo[i] > 50:  # Show only significantly used resources
                    adequacy = objective_function.calculate_adequacy(
                        resource["learning_styles"],
                        student_styles
                    )
                    score = objective_function.educational_objective(
                        adequacy=adequacy,
                        difficulty=resource["difficulty"],
                        knowledge=resource["knowledge"],
                        w_a=w_a,
                        w_d=w_d
                    )
                    contrib = score * (individuo[i] / 100)
                    fit_ind += contrib
                    print(f"  Recurso {i + 1}:")
                    print(f"    - Porcentaje de uso: {individuo[i]:.1f}%")
                    print(f"    - Adecuación: {adequacy:.2f}")
                    print(f"    - Puntuación: {score:.2f}")
            
            fitness.append(fit_ind)
            print(f"Puntuación total: {fit_ind:.2f}")

        # Show best path of current generation
        best_idx = fitness.index(max(fitness))
        best_fitness_gen = max(fitness)
        print(f"\n=== MEJOR RUTA DE LA GENERACIÓN {generation + 1} ===")
        print(f"Puntuación: {max(fitness):.2f}")
        print("Recursos recomendados:")
        for i, v in enumerate(decoded_population[best_idx]):
            if v > 50:
                print(f"  Recurso {i+1}: {v:.1f}% de uso")

        # Update historical best
        if max(fitness) > best_historical_fitness:
            best_historical_fitness = max(fitness)
            best_solution = decoded_population[best_idx].copy()
            print("\n=== ¡NUEVO MEJOR RESULTADO! ===")
            print(f"Puntuación: {best_historical_fitness:.2f}")

        # Genetic operations (hide binary output)
        parents = selection.tournament_selection(population_data, fitness, k=SETTINGS["selection"]["k"])
        new_population = []
        crossover_rate = SETTINGS["crossover_rate"]

        while len(new_population) < pop_size:
            if random.random() < crossover_rate:
                child1, child2 = crossover.one_point_crossover(parents[0], parents[1])
            else:
                child1, child2 = parents[0], parents[1]

            mutated_child1 = mutation.mutate(child1, SETTINGS["mutation_rate"])
            mutated_child2 = mutation.mutate(child2, SETTINGS["mutation_rate"])
            new_population.append(mutated_child1)
            new_population.append(mutated_child2)

        # Update population and decode
        population_data = replacement.replace_population(
            population_data,
            new_population,
            fitness,
            sum,
            bounds,
            bit_length=10,
            elitism=True
        )
        decoded_population = [binary_to_decimal(ind, bounds) for ind in population_data]

        print(f"\nGeneración {generation + 1} completada")
        print(f"Mejor aptitud actual: {max(fitness):.2f}")
        print(f"Mejor aptitud histórica: {best_historical_fitness:.2f}")
        historial_generaciones.append(best_fitness_gen)

    print("\n=== RESULTADO FINAL ===")
    print(f"Mejor puntuación alcanzada: {best_historical_fitness:.2f}")
    print("Ruta de aprendizaje óptima:")
    for i, v in enumerate(best_solution):
        if v > 50:
            print(f"  Recurso {i+1}: {v:.1f}% de uso")

    # Convertir la mejor solución a formato binario (0 o 1)
    binary_solution = [1 if x > 50 else 0 for x in best_solution]
    
    return binary_solution, best_historical_fitness, historial_generaciones
