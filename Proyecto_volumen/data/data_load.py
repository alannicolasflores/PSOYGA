import json
import os

BASE_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data"))

def cargar_archivo(nombre_archivo):
    
    ruta = os.path.join(BASE_DATA_PATH, nombre_archivo)
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def cargar_temas(nombre_archivo):
    return cargar_archivo(nombre_archivo)

def cargar_nombres(nombre_archivo):
    return cargar_archivo(nombre_archivo)

def cargar_primer_apellido(nombre_archivo):
    return cargar_archivo(nombre_archivo)

def cargar_segundo_apellido(nombre_archivo):
    return cargar_archivo(nombre_archivo)