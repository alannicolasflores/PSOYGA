import json
import os


def load_data(json_path):
    """
    Carga un archivo JSON desde una ruta especificada.
    
    Args:
        json_path (str): Ruta del archivo JSON.

    Returns:
        dict: Contenido del JSON como un diccionario.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        UnicodeDecodeError: Si hay un error de codificación al leer el archivo.
        json.JSONDecodeError: Si el archivo no tiene un formato JSON válido.
    """

    # Convertir a path absoluto si es relativo
    if not os.path.isabs(json_path):
        json_path = os.path.abspath(json_path)

    if not os.path.exists(json_path):
        raise FileNotFoundError(f" El archivo no existe: {json_path}")

    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not data:
            raise ValueError(f" El archivo '{json_path}' está vacío o mal estructurado.")

        return data

    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f" Error de codificación al leer {json_path}: {e}")

    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f" Error de JSON en {json_path}: {e}", doc=e.doc, pos=e.pos)


def preprocess_data(alumno, unidad_aprendizaje):
    """
    Preprocesa los datos recibidos para el algoritmo genético.
    
    Args:
        alumno (dict): Datos del alumno, incluyendo conocimientos y estilos de aprendizaje.
        unidad_aprendizaje (dict): Estructura de la unidad de aprendizaje con módulos, temas y recursos.

    Returns:
        tuple: student_knowledge (dict), student_styles (dict), resources (list)

    Raises:
        TypeError: Si los datos no son diccionarios.
        ValueError: Si no se encuentran recursos.
    """

    if not isinstance(alumno, dict):
        raise TypeError(" El parámetro 'alumno' debe ser un diccionario.")
    
    if not isinstance(unidad_aprendizaje, dict):
        raise TypeError(" El parámetro 'unidad_aprendizaje' debe ser un diccionario.")

    # Extraer conocimientos iniciales del alumno
    student_knowledge = {
        tema["id_tema"]: tema["nivel"]
        for tema in alumno.get("test_inicial", {}).get("temas", [])
    
    }

    # Estilos de aprendizaje del alumno
    student_styles = alumno.get("tipos_aprendizaje", {})

    # Extraer recursos de la unidad de aprendizaje
    resources = []
    for modulo in unidad_aprendizaje.get("modulos", []):
        for tema in modulo.get("temas", []):
            topic_id = tema.get("id")
            for recurso in tema.get("recursos", []):
                resource_data = {
                    "topic_id": topic_id,
                    "resource_id": recurso.get("id"),
                    "difficulty": recurso.get("dificultad"),
                    "learning_styles": recurso.get("tipos_aprendizaje", {}),
                    "type": recurso.get("tipo"),
                    "name": recurso.get("nombre"),
                    "url": recurso.get("url", "")
                }
                resources.append(resource_data)

    if not resources:
        raise ValueError(" No se encontraron recursos en la unidad de aprendizaje.")

    return student_knowledge, student_styles, resources
