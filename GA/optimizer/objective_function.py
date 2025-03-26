import math

def calculate_adequacy(resource_styles, student_styles):
    """
    Calcula la adecuación entre los estilos de aprendizaje del recurso y del estudiante.
    
    Parámetros:
    - resource_styles (dict): Estilos de aprendizaje del recurso (porcentajes)
    - student_styles (dict): Estilos de aprendizaje del estudiante (porcentajes)
    
    Retorna:
    - float: Valor de adecuación entre 0 y 1
    """
    total_match = 0
    total_weight = sum(student_styles.values())
    
    for style, student_value in student_styles.items():
        if style in resource_styles:
            # Normalizar los valores a porcentajes (0-1)
            student_percentage = student_value / 100
            resource_percentage = resource_styles[style] / 100
            # Calcular coincidencia ponderada
            total_match += min(student_percentage, resource_percentage) * student_value
    
    return total_match / total_weight if total_weight > 0 else 0

def educational_objective(adequacy, difficulty, knowledge, w_a, w_d):
    """
    Calcula la puntuación de un recurso educativo basada en la adecuación y el ajuste de dificultad.
    
    Parámetros:
    - adequacy (float): Nivel de adecuación entre el recurso y el estudiante (0-1).
    - difficulty (float): Dificultad del recurso educativo (1-3).
    - knowledge (float): Nivel de conocimiento del estudiante (1-3).
    - w_a (float): Peso asignado a la adecuación.
    - w_d (float): Peso asignado a la diferencia entre dificultad y conocimiento.
    
    Retorna:
    - float: Puntuación del recurso educativo.
    """
    difficulty_match = 1 - (abs(difficulty - knowledge) / 2)  # Normalize to 0-1
    return (w_a * adequacy + w_d * difficulty_match) / (w_a + w_d)  # Normalized score
    return w_a * adequacy - w_d * abs(difficulty - knowledge)

def calculate_topic_score(resources_scores):
    """
    Calcula la puntuación total de un tema.
    
    Parámetros:
    - resources_scores (list): Lista de puntuaciones de los recursos del tema
    
    Retorna:
    - float: Puntuación total del tema
    """
    return sum(score for score in resources_scores if score > 0)

def calculate_module_score(topic_scores, prerequisites_met=True):
    """
    Calcula la puntuación total del módulo.
    
    Parámetros:
    - topic_scores (list): Lista de puntuaciones de los temas
    - prerequisites_met (bool): Indica si se cumplen los prerequisitos
    
    Retorna:
    - float: Puntuación total del módulo
    """
    if not prerequisites_met:
        return 0
    return sum(topic_scores)
# Ejemplo de ejecución:
# adequacy = 0.8
# difficulty = 5
# knowledge = 4
# w_a = 1.5
# w_d = 1.0
# educational_objective(adequacy, difficulty, knowledge, w_a, w_d)
# Posible salida: 0.8
