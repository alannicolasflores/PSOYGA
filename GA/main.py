from optimizer import population, objective_function, selection, crossover, mutation, replacement
from config import SETTINGS

def main():
    # Configuración
    obj_func = objective_function.OBJECTIVE_FUNCTIONS[SETTINGS["objective_function"]]
    pop_size = SETTINGS["population_size"]
    generations = SETTINGS["generations"]
    dimensions = SETTINGS["dimensions"]
    bounds = SETTINGS["bounds"]

    # Inicializar población
    pop = population.initialize_population(pop_size, dimensions, bounds)

    # Iterar a través de generaciones
    for generation in range(generations):
        # Evaluar la aptitud de la población
        fitness = [obj_func(ind) for ind in pop]

        # Seleccionar padres
        parents = selection.tournament_selection(pop, fitness, k=3)

        # Cruce
        child1, child2 = crossover.one_point_crossover(parents[0], parents[1])

        # Mutación
        child1 = mutation.mutate(child1, SETTINGS["mutation_rate"], bounds)
        child2 = mutation.mutate(child2, SETTINGS["mutation_rate"], bounds)

        pop = replacement.replace_population(pop, [child1, child2], fitness, obj_func)


        # Mostrar el mejor resultado de la generación
        best_fitness = min(fitness)
        print(f"Generación {generation + 1}: Mejor aptitud = {best_fitness}")

if __name__ == "__main__":
    main()
