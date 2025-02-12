SETTINGS = {
    "generations": 500,
    "population_size": 20,
    "mutation_rate": 0.05,
    "selection": {"k": 3},  # Parámetro del torneo
    "weights": {  # Asegúrate de que esta clave existe
        "w_a": 0.8,  # Peso de adecuación
        "w_d": 0.2  # Peso de penalización
    },
    "bounds": (0, 1)  # Límites para la mutación
}
