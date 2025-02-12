import math

def calculate_adequacy(resource_vector, student_vector):
    """
    Calcula la adecuación entre el vector del recurso y el vector del estudiante usando similitud del coseno.
    """
    numerator = sum(p * q for p, q in zip(resource_vector, student_vector))
    denominator = math.sqrt(sum(p**2 for p in resource_vector)) * math.sqrt(sum(q**2 for q in student_vector))
    
    return numerator / denominator if denominator != 0 else 0

def educational_objective(adequacy, difficulty, knowledge, w_a, w_d):
    """
    Calcula la puntuación de un recurso educativo.
    """
    return w_a * adequacy - w_d * abs(difficulty - knowledge)
