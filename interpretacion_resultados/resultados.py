import os
import re

import openpyxl
import pandas as pd
from analizar_resultados import analizar_resultados
from diccionario import TEMAS_NIVEL
from load_data import cargar_archivos

BASE_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Archivos_generados/GA_V1/Asignaciones"))
archivos = cargar_archivos(BASE_DATA_PATH)

TIPO_MATERIAL = {
    "video": "kinestesico",
    "pdf": "lectura_escritura",
    "audio": "auditivo",
    "presentacion": "visual"
}

# --- Calcular el total real de materiales disponibles por tipo y por nivel en la unidad ---
total_disponibles_tipo = {k: 0 for k in TIPO_MATERIAL.keys()}
total_disponibles_nivel = {1: 0, 2: 0, 3: 0}

# Solo necesitas calcularlo una vez, usando el primer archivo (asumiendo estructura idéntica)
if archivos:
    xls = pd.ExcelFile(archivos[0])
    for combinacion in xls.sheet_names:
        df = pd.read_excel(xls, combinacion)
        df["asignacion"] = df["Asignación"].apply(eval)
        for _, row in df.iterrows():
            for tema in row["asignacion"]:
                for mat in tema.get("materiales", []):
                    tipo = mat.get("tipo")
                    nivel = mat.get("dificultad")
                    if tipo in total_disponibles_tipo:
                        total_disponibles_tipo[tipo] += 1
                    if nivel in total_disponibles_nivel:
                        total_disponibles_nivel[nivel] += 1

def exportar_resumen_excel(resumen, archivo, algoritmo, total_disponibles_tipo, total_disponibles_nivel):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Elimina la hoja por defecto

    encabezados = [
        "Alumno", "Estilo Predominante (%)", "Promedio Nivel", "% Nivel 1", "% Nivel 2", "% Nivel 3",
        "% Video", "% PDF", "% Audio", "% Presentación"
    ]

    for combinacion, datos in resumen.items():
        # Extrae el nivel_combinacion del nombre de la hoja si aplica
        math = re.search(r"archivo[_ ]?(\d+)", combinacion, re.IGNORECASE)
        nivel_combinacion = int(math.group(1)) if math else 1

        ws = wb.create_sheet(title=str(combinacion)[:31])
        ws.append(encabezados)

        xls = pd.ExcelFile(archivo)
        df = pd.read_excel(xls, combinacion)
        df["tipos_aprendizaje"] = df["Tipos de Aprendizaje"].apply(eval)
        df["asignacion"] = df["Asignación"].apply(eval)

        for _, row in df.iterrows():
            tipos = row["tipos_aprendizaje"]
            estilo_predominante = max(tipos, key=tipos.get)
            valor_estilo = tipos[estilo_predominante]
            tipo_count = {k: 0 for k in TIPO_MATERIAL.keys()}
            nivel_count = {1: 0, 2: 0, 3: 0}
            total_mat = 0
            for tema in row["asignacion"]:
                for mat in tema.get("materiales", []):
                    tipo = mat.get("tipo")
                    nivel = mat.get("dificultad")
                    if tipo in tipo_count:
                        tipo_count[tipo] += 1
                    if nivel in nivel_count:
                        nivel_count[nivel] += 1
                    total_mat += 1
            porcentajes_nivel = {
                n: (nivel_count[n] / total_mat * 100) if total_mat else 0
                for n in nivel_count
            }
            porcentajes_tipo = {
                k: (tipo_count[k] / total_mat * 100) if total_mat else 0
                for k in TIPO_MATERIAL.keys()
            }
            fila = [
                row['Alumno'],
                f"{estilo_predominante} ({valor_estilo}%)",
                f"{porcentajes_nivel.get(nivel_combinacion, 0):.2f}",
                f"{porcentajes_nivel[1]:.1f}%",
                f"{porcentajes_nivel[2]:.1f}%",
                f"{porcentajes_nivel[3]:.1f}%",
                f"{porcentajes_tipo['video']:.1f}%",
                f"{porcentajes_tipo['pdf']:.1f}%",
                f"{porcentajes_tipo['audio']:.1f}%",
                f"{porcentajes_tipo['presentacion']:.1f}%"
            ]
            ws.append(fila)

    output_dir = os.path.join(os.path.dirname(__file__), "../Archivos_generados")
    os.makedirs(output_dir, exist_ok=True)
    nombre_base = os.path.splitext(os.path.basename(archivo))[0]
    nombre_archivo = os.path.join(output_dir, f"Resumen_{algoritmo}_{nombre_base}.xlsx")
    wb.save(nombre_archivo)
    print(f"Resumen exportado a {nombre_archivo}")

# --- Procesamiento principal ---
for archivo in archivos:
    print(f"\nResultados para archivo: {os.path.basename(archivo)}")
    resumen = analizar_resultados(archivo)
    for combinacion, datos in resumen.items():
        math = re.search(r"archivo[_ ]?(\d)", combinacion, re.IGNORECASE)
        nivel_combinacion = int(math.group(1)) if math else None

        print(f"\nCombinación (hoja): {combinacion}")
        print(f"Alumno | Estilo Predominante (%) | Promedio Nivel {nivel_combinacion} | % Nivel 1 | % Nivel 2 | % Nivel 3 | % Video | % PDF | % Audio | % Presentación")
        print("-" * 150)
        xls = pd.ExcelFile(archivo)
        df = pd.read_excel(xls, combinacion)
        df["tipos_aprendizaje"] = df["Tipos de Aprendizaje"].apply(eval)
        df["asignacion"] = df["Asignación"].apply(eval)
        for _, row in df.iterrows():
            tipos = row["tipos_aprendizaje"]
            estilo_predominante = max(tipos, key=tipos.get)
            valor_estilo = tipos[estilo_predominante]
            tipo_count = {k: 0 for k in TIPO_MATERIAL.keys()}
            nivel_count = {1: 0, 2: 0, 3: 0}
            total_mat = 0
            for tema in row["asignacion"]:
                for mat in tema.get("materiales", []):
                    tipo = mat.get("tipo")
                    nivel = mat.get("dificultad")
                    if tipo in tipo_count:
                        tipo_count[tipo] += 1
                    if nivel in nivel_count:
                        nivel_count[nivel] += 1
                    total_mat += 1
            porcentajes_nivel = {
            n: (nivel_count[n] / total_mat * 100) if total_mat else 0
            for n in nivel_count
            }
            porcentajes_tipo = {
            k: (tipo_count[k] / total_mat * 100) if total_mat else 0
            for k in TIPO_MATERIAL.keys()
            }
            print(f"{row['Alumno']} | ({valor_estilo}%) | {porcentajes_nivel[nivel_combinacion]:.2f} | "
                  f"{porcentajes_nivel[1]:.1f}% | {porcentajes_nivel[2]:.1f}% | {porcentajes_nivel[3]:.1f}% | "
                  f"{porcentajes_tipo['video']:.1f}% | {porcentajes_tipo['pdf']:.1f}% | "
                  f"{porcentajes_tipo['audio']:.1f}% | {porcentajes_tipo['presentacion']:.1f}%")

    exportar_resumen_excel(resumen, archivo, "GA_V1", total_disponibles_tipo, total_disponibles_nivel)