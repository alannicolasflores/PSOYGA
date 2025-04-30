import os
import json
from datetime import datetime
from .optimizer.data_loader import load_data, preprocess_data_from_json
from .optimizer.resource_processor import extract_resources
from .optimizer.optimizer import optimize_resources

def run(alumno=None, unidad_aprendizaje=None):
    if alumno and unidad_aprendizaje:
        student_knowledge, student_styles, resources = preprocess_data_from_json(alumno, unidad_aprendizaje)
    else:
        alumno, unidad_aprendizaje = load_data()
        student_knowledge = {tema["id_tema"]: tema["nivel"] for tema in alumno.get("test_inicial", {}).get("temas", [])}
        student_styles = alumno.get("tipos_aprendizaje", {})
        resources = extract_resources(unidad_aprendizaje)

    best_solution, best_score = optimize_resources(student_knowledge, student_styles, resources)

    asignacion = []
    tema_index = 0
    for modulo in unidad_aprendizaje.get("modulos", []):
        for tema in modulo.get("temas", []):
            materiales_tema = []
            for recurso in tema.get("recursos", []):
                if tema_index < len(best_solution) and best_solution[tema_index] == 1:
                    materiales_tema.append({
                        "id": int(recurso.get("id", 0)),
                        "tipo": str(recurso.get("tipo", "")),
                        "nombre": str(recurso.get("nombre", "")),
                        "url": str(recurso.get("url", "")),
                        "tipos_aprendizaje": {
                            "visual": int(recurso.get("tipos_aprendizaje", {}).get("visual", 0)),
                            "auditivo": int(recurso.get("tipos_aprendizaje", {}).get("auditivo", 0)),
                            "lectura_escritura": int(recurso.get("tipos_aprendizaje", {}).get("lectura_escritura", 0)),
                            "kinestesico": int(recurso.get("tipos_aprendizaje", {}).get("kinestesico", 0))
                        },
                        "dificultad": int(recurso.get("dificultad", 0))
                    })
                tema_index += 1
            if materiales_tema:
                # Obtener el nombre del tema del test inicial si está disponible
                nombre_tema = ""
                for tema_test in alumno.get("test_inicial", {}).get("temas", []):
                    if tema_test.get("id_tema") == tema.get("id"):
                        nombre_tema = tema_test.get("nombre_tema", "")
                        break
                
                # Si no se encontró en el test inicial, usar el nombre del tema de la unidad
                if not nombre_tema:
                    nombre_tema = tema.get("nombre", "")
                
                asignacion.append({
                    "id_tema": int(tema.get("id", 0)),
                    "nombre_tema": str(nombre_tema),
                    "materiales": materiales_tema
                })

    resultado = {
        "mejor_solucion": [int(x) for x in best_solution],
        "puntaje": float(best_score),
        "asignacion": asignacion
    }

    return resultado