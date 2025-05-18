import math

def calculate_adequacy(resource_styles, student_styles):
    """
    Calcula la adecuación entre los estilos de aprendizaje del recurso y del estudiante.
    Si el estudiante no tiene estilos de aprendizaje definidos o hay valores None, se devuelve 0.
    """
    if not student_styles or not resource_styles:  # Evita la división por cero
        return 0
        
    # Verificar que no haya valores None en los estilos
    if (any(v is None for v in student_styles.values()) or 
        any(v is None for v in resource_styles.values())):
        return 0

    common_styles = set(student_styles.keys()) & set(resource_styles.keys())  # Intersección de claves
    if not common_styles:  # Si no hay estilos en común, retornar 0
        return 0  

    # Asegurarse de que los valores sean numéricos
    diff_sum = 0
    for style in common_styles:
        student_val = student_styles.get(style, 0) or 0  # Convierte None a 0
        resource_val = resource_styles.get(style, 0) or 0  # Convierte None a 0
        diff_sum += abs(student_val - resource_val)
    
    return 100 - (diff_sum / max(len(common_styles), 1))  # Asegurar que nunca divida por 0


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
    Preprocesa los datos de los recursos para el optimizador.
    Maneja valores faltantes o nulos en los recursos.
    """
    processed_resources = []
    
    for resource in resources:
        # Asegurarse de que los estilos de aprendizaje tengan valores por defecto
        learning_styles = resource.get('learning_styles', {})
        if learning_styles is None:
            learning_styles = {}
            
        # Asegurar que todos los estilos tengan valores numéricos
        default_styles = {
            'visual': 0,
            'auditivo': 0,
            'lectura_escritura': 0,
            'kinestesico': 0
        }
        
        # Combinar con valores por defecto y asegurar que los valores sean numéricos
        safe_learning_styles = {}
        for style, default_val in default_styles.items():
            val = learning_styles.get(style)
            safe_learning_styles[style] = int(val) if val is not None and str(val).isdigit() else default_val
        
        # Asegurar que la dificultad sea un valor numérico
        difficulty = resource.get('difficulty')
        if difficulty is None or not str(difficulty).isdigit():
            difficulty = 1  # Valor por defecto
        else:
            difficulty = int(difficulty)
        
        # Obtener el ID del tema, usando un valor por defecto si no está presente
        topic_id = resource.get('topic_id', 0)
        
        processed_resource = {
            'learning_styles': safe_learning_styles,
            'difficulty': difficulty,
            'knowledge': int(student_knowledge.get(topic_id, 0) or 0),
            'topic_id': topic_id
        }
        processed_resources.append(processed_resource)
    
    return processed_resources

