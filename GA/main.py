import sys
import os
from optimizer.data_loader import load_data
from optimizer.resource_processor import extract_resources
from optimizer.optimizer import optimize_resources
import json
# Agregar el directorio raíz del proyecto al path para importar módulos personalizados
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    """
    Función principal que carga los datos, extrae los recursos y ejecuta la optimización.
    """
    # Cargar datos del alumno y unidad de aprendizaje
    alumno, unidad_aprendizaje = load_data()

    # Extraer información de los recursos disponibles
    student_knowledge = {tema["id_tema"]: tema["nivel"] for tema in alumno.get("test_inicial", {}).get("temas", [])}
    student_styles = alumno.get("tipos_aprendizaje", {})
#  print("🔍 Verificando estructura de `unidad_aprendizaje` antes de procesarlo...")
 #   print(json.dumps(unidad_aprendizaje, indent=2))  # Esto imprimirá el JSON cargado con formato legible

    resources = extract_resources(unidad_aprendizaje)  # Extrae los recursos

    # Optimizar la selección de recursos educativos
    best_solution, best_score = optimize_resources(student_knowledge, student_styles, resources)

    # Mostrar los resultados
    #print(f"Mejor combinación de recursos: {best_solution}")
    print(f"Mejor puntaje obtenido: {best_score}")

if __name__ == "__main__":
    main()
