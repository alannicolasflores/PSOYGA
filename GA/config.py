SETTINGS = {
    "generations": 10,
    "population_size": 20,
    "mutation_rate": 0.05,
    "crossover_rate": 0.8,
    "selection": {"k": 3},  # Parámetro del torneo
    "weights": {  # Asegúrate de que esta clave existe
        "w_a": 0.7,  # Peso de adecuación ajustado
        "w_d": 0.3   # Peso de penalización ajustado
    },
    "bounds": (0, 100)  # Límites para la mutación
}
