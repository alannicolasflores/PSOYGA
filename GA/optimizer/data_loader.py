import json

def load_json(file_path):
    """Carga un archivo JSON y valida su contenido."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not data:
            raise ValueError(f"Error: El archivo '{file_path}' está vacío o mal estructurado.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: El archivo '{file_path}' no se encontró. Verifica la ruta.")
    except json.JSONDecodeError:
        raise ValueError(f"Error: '{file_path}' no tiene un formato JSON válido.")

def load_data():
    """Carga los archivos JSON de alumno y unidad de aprendizaje."""
    alumno = load_json('alumno.json')
    unidad_aprendizaje = load_json('Grafo.json')

    if not isinstance(alumno, dict) or not isinstance(unidad_aprendizaje, dict):
        raise TypeError("Error: Los datos cargados deben ser diccionarios válidos.")

    return alumno, unidad_aprendizaje
