import json
import os
import random
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from data.data_load import (cargar_nombres, cargar_primer_apellido,
                            cargar_segundo_apellido, cargar_temas)
from functions.generar_perfil import generar_perfil_vark

# Definir el número de alumnos y los niveles
num_alumnos = 36
niveles = [1, 2, 3]
estilo_map = {
    'visual': 'Visual', 
    'auditivo': 'Auditivo', 
    'lectura_escritura': 'Lectura/Escritura', 
    'kinestesico': 'Kinestésico'}

nombres = cargar_nombres("nombres.json")  # Cargar los nombres desde el archivo JSON
apellidos1 = cargar_primer_apellido("apellidos_1.json")  # Cargar el primer apellido desde el archivo JSON
apellidos2 = cargar_segundo_apellido("apellidos_2.json")  # Cargar el segundo apellido desde el archivo JSON
temas = cargar_temas("temas_BD.json")  # Cargar los temas desde el archivo JSON



# Ruta donde se encuentran los archivos de alumnos
alumnos_path = "../../final_data/alumnos_BD" 
# Ruta donde se encuentran los archivos de unidad
unidad_path = "../../final_data/unidad_BD"  
# Ruta donde se generarán los archivos combinados
ruta_salida = "../../final_data/entrada_final_BD"  

# Crear la carpeta de salida si no existe
os.makedirs(ruta_salida, exist_ok=True)

# Verificar si hay archivos JSON en la carpeta de unidad
archivos_unidad = [f for f in os.listdir(unidad_path) if f.endswith('.json')]

if not archivos_unidad:
    raise FileNotFoundError(f"No se encontraron archivos JSON en la ruta: {unidad_path}")
else:
    print(f"Se encontraron {len(archivos_unidad)} archivos de unidad en la ruta: {unidad_path}")

# Procesar cada archivo de unidad
for archivo_unidad in archivos_unidad:
    ruta_unidad = os.path.join(unidad_path, archivo_unidad)
    
    with open(ruta_unidad, "r", encoding="utf-8") as f:
        unidad_datos = json.load(f)
   
    if not unidad_datos:
        print(f"Error: La unidad de aprendizaje {archivo_unidad} está vacía.")
        continue  # Si la unidad está vacía, saltamos este archivo

    for estilo_corto, estilo_nombre in estilo_map.items():
        for nivel in niveles:
            
            nombre_salida = f"archivo_{nivel}_{estilo_corto}.json"
            ruta_salida_final = os.path.join(ruta_salida, nombre_salida)
            alumno_dict = {}
            # Generar 36 alumnos por cada combinación de nivel y estilo
            
            for alumno_id in range(1, num_alumnos + 1):
                perfil_vark = generar_perfil_vark(estilo_corto)  # Genera el perfil VARK
                temas_nivel = [{"id_tema": idx+1, "nombre_tema": tema, "nivel": nivel} for idx, tema in enumerate(temas)]
                nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos1)} {random.choice(apellidos2)}"
                    
                    
                alumno_dict[f"alumno_{alumno_id}"] = {
                            "id": alumno_id,  # ID único para cada alumno
                            "nombre": nombre_completo,
                            "tipos_aprendizaje": {
                                "visual": perfil_vark['visual'],
                                "auditivo": perfil_vark['auditivo'],
                                "lectura_escritura": perfil_vark['lectura_escritura'],
                                "kinestesico": perfil_vark['kinestesico']
                        },
                        "test_inicial": {
                            "temas": temas_nivel
                        }
                    }
                alumno_dict[f"unidad_aprendizaje_{alumno_id}"] = unidad_datos  # Agregar la unidad completa
            with open(ruta_salida_final, "w", encoding="utf-8") as f:
                json.dump(alumno_dict, f, indent=4, ensure_ascii=False)
            
            print(f"Archivo combinado generado: {ruta_salida_final}")

print(f"\nProceso completado. Archivos combinados generados en {ruta_salida}.")
