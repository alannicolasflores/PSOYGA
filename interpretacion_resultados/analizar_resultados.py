import pandas as pd

TIPO_MATERIAL = {
    "video": "kinestesico",
    "pdf": "lectura_escritura",
    "audio": "auditivo",
    "presentacion": "visual"

}


def analizar_resultados(archivos):
    xls = pd.ExcelFile(archivos)
    resumen = {}
    
    for hoja in xls.sheet_names:
        df = pd.read_excel(xls, hoja)
        
        df["tipos_aprendizaje"] = df["Tipos de Aprendizaje"].apply(eval)
        df["asignacion"] = df["Asignación"].apply(eval)
        df["mejor_solucion"] = df["Mejor Solución"].apply(eval)
        
        
        promedios = []
        
        porcentajes_material = {k: 0 for k in TIPO_MATERIAL.keys()}
        niveles_material = []
        
        for _, row in df.iterrows():
            tipos_aprendizaje = row["tipos_aprendizaje"]
            estilo_predominante = max(tipos_aprendizaje, key=tipos_aprendizaje.get)
            promedios.append((row["Alumno"], estilo_predominante))
            
            for tema in row["asignacion"]:
                materiales = tema.get("materiales", [])
            
                for mat in materiales:
                    
                    tipo = mat.get("tipo")
                    nivel = mat.get("dificultad")
                    if tipo in porcentajes_material:
                        porcentajes_material[tipo] += 1
                    if nivel is not None:
                        niveles_material.append(nivel)
                        
                        
                        
        total_materiales = sum(porcentajes_material.values())
        porcentaje_tipo = {k: v / total_materiales * 100 if total_materiales > 0 else 0 for k, v in porcentajes_material.items()}
        promedio_nivel = sum(niveles_material) / len(niveles_material) if niveles_material else 0
        
        resumen[hoja] = {
            "promedios_estilo": promedios,
            "porcentaje_tipo_material": porcentaje_tipo,
            "promedio_nivel_material": promedio_nivel
        }
        
    return resumen