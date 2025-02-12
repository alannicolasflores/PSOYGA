import math

def calculate_adequacy(resource_styles, student_styles):
    """
    Calcula la adecuación entre los estilos de aprendizaje del recurso y del estudiante.
    Si el estudiante no tiene estilos de aprendizaje definidos, se devuelve 0.
    """
    if not student_styles or not resource_styles:  # Evita la división por cero
        return 0  

    common_styles = set(student_styles.keys()) & set(resource_styles.keys())  # Intersección de claves
    if not common_styles:  # Si no hay estilos en común, retornar 0
        return 0  

    return 100 - sum(abs(student_styles.get(style, 0) - resource_styles.get(style, 0)) 
                     for style in common_styles) / max(len(common_styles), 1)  # Asegurar que nunca divida por 0


def difficulty_penalty(difficulty, knowledge, tolerance=1):
    """
    Aplica una penalización adaptativa si la diferencia entre la dificultad del recurso
    y el conocimiento del estudiante es mayor a una tolerancia dada.
    """
    diff = abs(difficulty - knowledge)
    if diff <= tolerance:
        return 0  # Sin penalización si está dentro del rango tolerable
    return diff  # Penalización lineal en lugar de cuadrática

def preprocess_resource_data(resources, student_knowledge, student_styles):
    """
    Preprocesa los datos de los recursos, calculando la adecuación y ajustando los valores
    antes de ser evaluados en la función objetivo.
    """
    processed_resources = []
    for resource in resources:
        # Verificar que el recurso tenga un ID válido
        resource_id = resource.get("resource_id")  # Usar "resource_id" en lugar de "id"
        if resource_id is None:
            print(f" Advertencia: Se encontró un recurso sin 'resource_id'. Recurso omitido: {resource}")
            continue  # Saltar este recurso

        adequacy = calculate_adequacy(resource.get("learning_styles", {}), student_styles)
        print(f"Recurso {resource['resource_id']} - Adecuación calculada: {adequacy}")

        processed_resources.append({
            "topic_id": resource.get("topic_id", 0),
            "resource_id": resource_id,  # Corregido
            "difficulty": resource.get("difficulty", 0),
            "knowledge": student_knowledge.get(resource.get("topic_id"), 0),
            "adequacy": adequacy
        })

    return processed_resources

