import math

def educational_objective(adequacy, difficulty, knowledge, w_a, w_d):
    """
    Calcula la puntuación de un recurso educativo basada en la adecuación y el ajuste de dificultad.
    
    Parámetros:
    - adequacy (float): Nivel de adecuación entre el recurso y el estudiante.
    - difficulty (float): Dificultad del recurso educativo.
    - knowledge (float): Nivel de conocimiento del estudiante.
    - w_a (float): Peso asignado a la adecuación.
    - w_d (float): Peso asignado a la diferencia entre dificultad y conocimiento.
    
    Retorna:
    - float: Puntuación del recurso educativo.
    """
    return w_a - w_d * abs(difficulty - knowledge)

# Ejemplo de ejecución:
# adequacy = 0.8
# difficulty = 5
# knowledge = 4
# w_a = 1.5
# w_d = 1.0
# educational_objective(adequacy, difficulty, knowledge, w_a, w_d)
# Posible salida: 0.8
