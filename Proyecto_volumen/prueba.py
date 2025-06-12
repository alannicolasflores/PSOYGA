import os

base_path = "/Volumes/SSD_JOEL/Recoleccion_Materiales/materiales_descargados/IS/Modulo-1"

# Tipos de material que esperamos en cada tema
tipos_materiales = ["pdf", "video", "audio", "ppt"]

print(f"Accediendo al módulo: {base_path}")

# Listar carpetas temas dentro del módulo
temas = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
print(f"Temas encontrados: {temas}")

for tema in temas:
    print(f"\nTema: {tema}")
    tema_path = os.path.join(base_path, tema)

    for tipo in tipos_materiales:
        tipo_path = os.path.join(tema_path, tipo)
        if os.path.exists(tipo_path) and os.path.isdir(tipo_path):
            archivos = [f for f in os.listdir(tipo_path) if f != '.DS_Store' and not f.startswith('.')]

           
            if archivos:
                archivo = archivos[0]  # Tomamos el primer archivo que encuentre
                print(f"  Tipo: {tipo} -> Archivo: {archivo}")
            else:
                print(f"  Tipo: {tipo} -> No hay archivos")
        else:
            print(f"  Tipo: {tipo} -> Carpeta no encontrada")
