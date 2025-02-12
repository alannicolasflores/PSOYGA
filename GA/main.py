import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from optimizer import population, objective_function, selection, crossover, mutation, replacement
from config import SETTINGS

if not isinstance(alumno, dict):
    raise TypeError(f"Se esperaba un diccionario en 'alumno', pero se encontró: {type(alumno)}")

temas = alumno.get("test_inicial", {}).get("temas", [])

if isinstance(temas, set):
    temas = list(temas)  # Convertir a lista si es un conjunto
elif not isinstance(temas, list):
    raise TypeError(f"Se esperaba una lista en 'temas', pero se encontró: {type(temas)}")

student_knowledge = {tema["id_tema"]: tema["nivel"] for tema in temas}

student_styles = alumno.get("tipos_aprendizaje", {})

resources = []
for modulo in unidad_aprendizaje.get("modulos", []):
    for tema in modulo.get("temas", []):
        topic_id = tema.get("id")
        for recurso in tema.get("recursos", []):
            resource_data = {
                "topic_id": topic_id,
                "resource_id": recurso.get("id"),
                "difficulty": recurso.get("dificultad", 0),
                "learning_styles": recurso.get("tipos_aprendizaje", {}),
                "type": recurso.get("tipo"),
                "name": recurso.get("nombre", "Desconocido")
            }
            resources.append(resource_data)

def optimize_resources(student_knowledge, student_styles, resources):
    generations = SETTINGS["generations"]
    pop_size = SETTINGS["population_size"]
    w_a = SETTINGS["weights"]["w_a"]
    w_d = SETTINGS["weights"]["w_d"]
    bounds = SETTINGS["bounds"]

    population_data = population.initialize_population(pop_size, len(resources))
    best_historical_fitness = float('-inf')

    for generation in range(generations):
        decoded_population = [population.binary_to_decimal(ind, bounds) for ind in population_data]

        fitness = [
            sum(
                objective_function.educational_objective(
                    adequacy=objective_function.calculate_adequacy(
                        list(resources[i]["learning_styles"].values()), list(student_styles.values())
                    ),
                    difficulty=resources[i]["difficulty"],
                    knowledge=student_knowledge.get(resources[i]["topic_id"], 0),
                    w_a=w_a,
                    w_d=w_d
                ) * decoded_population[idx][i]
                for i in range(len(resources))
            )
            for idx in range(len(decoded_population))
        ]

        parents = selection.tournament_selection(population_data, fitness, k=SETTINGS["selection"]["k"])
        new_population = []
        while len(new_population) < pop_size:
            child1, child2 = crossover.one_point_crossover(parents[0], parents[1])
            new_population.append(mutation.mutate(child1, SETTINGS["mutation_rate"]))
            new_population.append(mutation.mutate(child2, SETTINGS["mutation_rate"]))

        population_data = replacement.replace_population(population_data, new_population, fitness, sum, bounds, bit_length=10, elitism=True)

        best_fitness = max(fitness)
        if best_fitness > best_historical_fitness:
            best_historical_fitness = best_fitness

        print(f"Generación {generation + 1}: Mejor aptitud = {best_historical_fitness}")

    best_index = fitness.index(best_historical_fitness)
    return population_data[best_index], best_historical_fitness

def main():
    alumno = { ... }  # Inserta el JSON del alumno aquí
    unidad_aprendizaje = { ... }  # Inserta el JSON de la unidad de aprendizaje aquí

    student_knowledge, student_styles, resources = preprocess_data(alumno, unidad_aprendizaje)
    best_solution, best_score = optimize_resources(student_knowledge, student_styles, resources)

    print(f"Mejor combinación de recursos: {best_solution}")
    print(f"Mejor puntaje obtenido: {best_score}")

if __name__ == "__main__":
    main()
