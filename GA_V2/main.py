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
                        "nombre": recurso['nombre'],
                        "tipo": recurso['tipo'],
                    })
                tema_index += 1
            if materiales_tema:
                asignacion.append({
                    "materiales": materiales_tema
                })

    return mejor_solucion, mejor_aptitud, asignacion
