import os
import json

def load_json(file_name):
    """
    Carga un archivo JSON desde el directorio del proyecto.
    """
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, '..', file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"  Error: El archivo '{file_path}' no se encontró. Verifica la ruta.")

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not data:
        raise ValueError(f"  Error: El archivo '{file_path}' está vacío o mal estructurado.")
    
    return data


def load_data():
    """
    Carga los datos del alumno y la unidad de aprendizaje desde archivos locales.
    """
    alumno = load_json('alumno.json')
    unidad_aprendizaje = load_json('Grafo.json')

    if not isinstance(alumno, dict) or not isinstance(unidad_aprendizaje, dict):
        raise TypeError("  Error: Los datos cargados deben ser diccionarios válidos.")

    return alumno, unidad_aprendizaje


def preprocess_data_from_json(alumno, unidad_aprendizaje):
    """
    Preprocesa datos pasados directamente como argumentos (generalmente desde un POST).
    Devuelve: student_knowledge, student_styles, resources
    """
    # Validaciones básicas
    if not isinstance(alumno, dict):
        raise TypeError("  El parámetro 'alumno' debe ser un diccionario.")
    if not isinstance(unidad_aprendizaje, dict):
        raise TypeError("  El parámetro 'unidad_aprendizaje' debe ser un diccionario.")

    # Extraer conocimientos iniciales del alumno
    student_knowledge = {
        tema["id_tema"]: tema["nivel"]
        for tema in alumno.get("test_inicial", {}).get("temas", [])
    }

    # Estilos de aprendizaje del alumno
    student_styles = alumno.get("tipos_aprendizaje", {})

    # Extraer los recursos desde la unidad de aprendizaje
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
        raise ValueError("  No se encontraron recursos en la unidad de aprendizaje.")

    return student_knowledge, student_styles, resources
