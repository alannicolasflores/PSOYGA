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
                        "titulo": recurso.get("nombre"),
                        "tipo": recurso.get("tipo")
                    })
                tema_index += 1
            if materiales_tema:
                asignacion.append({
                    "tema": tema.get("nombre"),
                    "materiales": materiales_tema
                })

    return best_solution, best_score, asignacion