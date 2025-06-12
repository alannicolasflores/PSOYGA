import json
import os

import openpyxl
import pytest
import requests

BASE_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Proyecto_volumen/final_data/entrada_final_BD"))

def cargar_archivos(directorio):
    
    return [os.path.join(directorio, f) 
            for f in os.listdir(directorio) 
            if f.endswith('.json')
            ]

#Primero correr func start y posteriormente el comando pytest

#--- Comando para correr pruebas automatizadas ---
# pytest -s tests/prueba_volumen.py

# ---- Entorno virtual ----
# env_tests

# ---- Scripts de ejecucion y terminacion ----

"""

NOTA: 
Los scripts están configurados para correr en una máquina MacOs, 
tendrían que adaptarse para correr en Windows.

"""
# ./test_volumen.sh
# ./terminate.sh


# URL del endpoint de Azure Function
url = "http://localhost:7071/api/optimize_resources" 

resultados_algoritmo = {}


# Prueba de optimización
@pytest.mark.parametrize("algoritmo", ["GA_V2"])
def test_optimizacion(algoritmo):
    
    
    print(f"\nIniciando prueba de optimización del algoritmo {algoritmo}")
    archivos_entrada = cargar_archivos(BASE_DATA_PATH)
    resultados = {}
    
    for archivo in archivos_entrada:
        
        with open(archivo, 'r', encoding='utf-8') as file:
            datos_entrada = json.load(file)
        datos_entrada["algoritmo"] = algoritmo

        alumnos = [k for k in datos_entrada.keys() if k.startswith("alumno_")]
        print(f"\n Archivo de entrada: {os.path.basename(archivo)}")
        print(f"Total de alumnos en archivo: {len(alumnos)}")

        combinacion = os.path.splitext(os.path.basename(archivo))[0]
        for idx, alumno_key in enumerate(alumnos, 1):
            alumno = datos_entrada[alumno_key]
            unidad_key = f"unidad_aprendizaje_{alumno_key.split('_')[1]}"
            unidad = datos_entrada.get(unidad_key, {})
            
            datos_entrada_individual = {
            
            "alumno": alumno,
            "unidad_aprendizaje": unidad,
            "algoritmo": algoritmo
            }
            
            print(f"\nJSON enviado para el alumno {idx}:")
            

            nombre_alumno = alumno.get("nombre", f"alumno_{idx}")

            print(f"\nAlumno {idx}: {nombre_alumno}")

            response = requests.post(url, json=datos_entrada_individual)
            assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
            print("Status code esperado: 200")
            print(f"Status code obtenido: {response.status_code}")

            assert response.headers['Content-Type'] == 'application/json', "Response is not in JSON format"
            resultado = response.json()
            
            if combinacion not in resultados:
                resultados[combinacion] = []
            resultados[combinacion].append({
                "alumno": nombre_alumno,
                "mejor_solucion": resultado.get('mejor_solucion', []),
                "generaciones": resultado.get('generaciones', []),
                "puntaje": resultado.get('puntaje', 'No disponible'),                    "asignacion": resultado.get('asignacion', [])
            })

            
            print("Resultados de la optimización:")
            print(f"Mejor solución: {resultado.get('mejor_solucion', 'No disponible')}")
            print(f"Puntaje de la mejor solución: {resultado.get('puntaje', 'No disponible')}")

            if 'generaciones' in resultado:
                for idx, gen in enumerate(resultado['generaciones']):
                    print(f" Generación {idx+1}: {gen}")
            elif 'evolucion' in resultado and 'generaciones' in resultado['evolucion']:
                for idx, gen in enumerate(resultado['evolucion']['generaciones']):
                    print(f" Generación {idx+1}: {gen}")
            else:
                print("\nNo se encontró información de generaciones en la respuesta.")
                

            

            assert isinstance(resultado.get("mejor_solucion", []), list), "El campo 'mejor_solucion' no es una lista válida."
            assert isinstance(resultado.get("puntaje", -1), float), "El puntaje no es un número flotante válido."
            assert isinstance(resultado.get("generaciones", []), list), "El campo 'generaciones' no es una lista válida."

    resultados_algoritmo[algoritmo] = resultados

    print(f"\nPrueba de optimización para {algoritmo} completada con éxito en archivo {os.path.basename(archivo)}")
    print(f"\n--------------------------------------------------------------------------- ")
    
    exportar_resultados_excel({algoritmo: resultados})


def exportar_resultados_excel(resultados_algoritmo):
    
    output_dir = os.path.join(os.path.dirname(__file__), "../Archivos_generados")
    os.makedirs(output_dir, exist_ok=True)  # Crea la carpeta si no existe
    
    
    for algoritmo, combinaciones in resultados_algoritmo.items():
        wb = openpyxl.Workbook()
        wb.remove(wb.active)  # Eliminar la hoja por defecto
        
        for combinacion, resultados in combinaciones.items():
            max_generaciones = max(len(res["generaciones"]) for res in resultados)
            ws = wb.create_sheet(title=combinacion[:31])
            encabezados = ["Alumno", "Mejor Solución"] + [f"Generación {i+1}" for i in range(max_generaciones)] + ["Puntaje"]
            ws.append(encabezados)
            for res in resultados:
                fila = [
                    res["alumno"],
                    str(res["mejor_solucion"]),
                    
                ]
                fila += [res["generaciones"][i] if i < len(res["generaciones"]) else "" for i in range(max_generaciones)]
                fila.append(res["puntaje"])
                ws.append(fila)
                
        wb.save(os.path.join(output_dir, f"resultados_{algoritmo}_convergencia.xlsx"))

def exportar_excel():
    exportar_resultados_excel(resultados_algoritmo)