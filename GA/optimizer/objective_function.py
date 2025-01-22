import numpy as np

def rastrigin(x):
    return 10 * len(x) + sum([(xi**2 - 10 * np.cos(2 * np.pi * xi)) for xi in x])

def sphere(x):
    return sum([xi**2 for xi in x])


def educational_objective(x):
    """
    x[0]: a_{i,j} (adecuación)
    x[1]: d_{i,j} (dificultad del recurso)
    x[2]: k_{i,j} (nivel de conocimiento del estudiante)
    x[3]: w_a (peso de la adecuación)
    x[4]: w_d (peso de la penalización por dificultad)
    """
    a_ij = x[0]  # Adecuación
    d_ij = x[1]  # Dificultad
    k_ij = x[2]  # Conocimiento
    w_a = x[3]   # Peso de adecuación
    w_d = x[4]   # Peso de penalización

    # Fórmula de la función objetivo
    return w_a * a_ij - w_d * abs(d_ij - k_ij)
OBJECTIVE_FUNCTIONS = {
    "rastrigin": rastrigin,
    "sphere": sphere,
    "educational": educational_objective  # Nueva función objetivo
}