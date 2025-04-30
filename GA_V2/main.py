import json
import os

from .genetic_algorithm import (AlgoritmoGenetico, funcion_aptitud, load_data,
                                mutacion_binaria,
                                representacionBinaria_dosPuntos,
                                seleccion_torneo)


def run(alumno=None, unidad_aprendizaje=None):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "data")

    datos_estudiante = alumno or load_data(os.path.join(DATA_DIR, 'alumno.json'))
    datos_materiales = unidad_aprendizaje or load_data(os.path.join(DATA_DIR, 'unidad_aprendizaje.json'))

    # 🛠️ Homologar estructura si vienen directo desde la API
    if 'modulos' in datos_materiales:
        datos_materiales = {
            'unidad_aprendizaje': datos_materiales
        }

    if 'tipos_aprendizaje' in datos_estudiante:
        datos_estudiante = {
            'alumno': datos_estudiante
        }

    print("Estructura de datos_materiales:")
    print(json.dumps(datos_materiales, indent=2))

    longitud_individuo = sum(
        len(tema['recursos'])
        for modulo in datos_materiales['unidad_aprendizaje']['modulos']
        for tema in modulo['temas']
    )

    if longitud_individuo == 0:
        raise ValueError("No hay recursos disponibles para optimizar")

    algoritmo_genetico = AlgoritmoGenetico(
        funcion_mutacion=mutacion_binaria,
        funcion_cruza=representacionBinaria_dosPuntos,
        funcion_seleccion=seleccion_torneo,
        funcion_aptitud=funcion_aptitud,
        tasa_mutacion=0.01,
        tasa_de_cruza=0.8,
        tamano_poblacion=50,
        longitud_individuo=longitud_individuo,
        datos_estudiante=datos_estudiante,
        datos_materiales=datos_materiales,
        alpha=0.6,
        beta=0.4,
        sigma=2,
        generaciones_detencion_temprana=10
    )

    mejor_solucion, mejor_aptitud, generacion_detencion = algoritmo_genetico.ejecutar(100)

    asignacion = []
    tema_index = 0
    for modulo in datos_materiales['unidad_aprendizaje']['modulos']:
        for tema in modulo['temas']:
            materiales_tema = []
            for recurso in tema['recursos']:
                if tema_index < len(mejor_solucion) and mejor_solucion[tema_index] == 1:
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
                for tema_test in datos_estudiante.get("alumno", {}).get("test_inicial", {}).get("temas", []):
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
        "mejor_solucion": [int(x) for x in mejor_solucion],
        "puntaje": float(mejor_aptitud),
        "asignacion": asignacion
    }

    return resultado
