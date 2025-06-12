import json
import os
import random
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from functions.designar_estilos import asignar_estilos

base_path = "/Volumes/SSD_JOEL/Recoleccion_Materiales/materiales_descargados/IS"

unidad_aprendizaje_base = {
    "id": 1,
    "nombre": "Unidad de Aprendizaje: Metodologías de Ingeniería de Software",
    "descripcion": "Exploración de las principales metodologías utilizadas en la ingeniería de software para el desarrollo eficiente de proyectos.",
    "modulos": []
}
nivel_por_modulo = {
    
     1: 1,
    2: 2,
    3: 3,
    4: 3
}

modulos = {
    "Fundamentos": [
    "Fundamentos de ingeniería de software",
    "Plan de proyecto software",
    "Modelos de procesos",
    "Principios y metodologías ágiles"
    ],
    "Diseño y Construcción": [
        "Ingeniería de requerimientos",
        "Diseño del sistema software",
        "Herramientas de modelado"
    ],
    "Pruebas de Software": [
        "Tipos de pruebas",
        "Herramientas para pruebas",
        "Evaluación de las pruebas"
    ],
    "Calidad y Modelos de Madurez": [
        "Calidad del proceso software",
        "Calidad del producto software",
        "Modelos y normas de calidad",
        "Modelos de madurez"
    ]
}



def normalizar_nombre(nombre):
    return nombre.replace(" ", "_")


def cargar_materiales_por_tema(tema, nivel_dificultad, modulo_id, tema_id):
    global material_id_global
    materiales = []
    tipos_materiales = ["pdf", "video", "audio", "presentacion"]
    tema_normalizado = normalizar_nombre(tema)
    modulo_carpeta = f"Modulo-{modulo_id}"

    for tipo_material in tipos_materiales:
        ruta_material = os.path.join(base_path, modulo_carpeta, tema_normalizado, tipo_material)
        
        if os.path.exists(ruta_material) and os.path.isdir(ruta_material):
            archivos = [f for f in os.listdir(ruta_material) if not f.startswith('.')]
            
            if archivos:
                archivo = archivos[0]
                archivos_normalizados = os.path.splitext(archivo)[0]
                normalizar_archivos = normalizar_nombre(archivos_normalizados)
           
                material = {
                    "id": material_id_global,
                    "tipo": tipo_material,
                    "nombre": archivos_normalizados,
                    "url": f"https://{tema_normalizado}/{normalizar_archivos}.com",
                    "descripcion": f"Material sobre {tema} en formato {tipo_material}.",
                    "tipos_aprendizaje": asignar_estilos(tipo_material),
                    "dificultad": nivel_dificultad
                }
                materiales.append(material)
                material_id_global += 1  # Incrementar el ID del tema para cada material encontrado
    return materiales

unidad_numero = 1
tema_id = 1
material_id_global = 1

for idx, (nombre_modulo, temas) in enumerate(modulos.items(), start=1):
    modulo_dict = {
        "id": idx,
        "nombre": nombre_modulo,
        "temas": []
    }
    nivel = nivel_por_modulo.get(idx, 3)
    for tema in temas:
        recursos = cargar_materiales_por_tema(tema, nivel, idx, tema_id)
        modulo_dict["temas"].append({
            "id": tema_id,
            "nombre": tema,
            "descripcion": f"Descripción general de {tema}.",
            "recursos": recursos
        })
        tema_id += 1  # Incrementar el ID del tema para cada tema procesado 
    unidad_aprendizaje_base["modulos"].append(modulo_dict)

output_dir = "../../final_data/unidad_IS"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, f"unidad_aprendizaje_IS_{unidad_numero}.json")

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(unidad_aprendizaje_base, f, indent=4, ensure_ascii=False)

print(f"Archivo JSON generado en: {output_path}")
