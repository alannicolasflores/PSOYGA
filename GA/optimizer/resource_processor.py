def extract_resources(unidad_aprendizaje):
    """Extrae los recursos educativos de la unidad de aprendizaje."""
    resources = []
    
    # Asegurar que estamos accediendo correctamente al JSON
    if not unidad_aprendizaje or "unidad_aprendizaje" not in unidad_aprendizaje:
        raise ValueError(" Error: `unidad_aprendizaje` está vacío o no tiene la clave 'unidad_aprendizaje'.")

    unidad_aprendizaje = unidad_aprendizaje["unidad_aprendizaje"]

    #print(" Verificando módulos en unidad de aprendizaje...")

    if "modulos" not in unidad_aprendizaje or not unidad_aprendizaje["modulos"]:
        raise ValueError(" Error: No se encontraron módulos en `unidad_aprendizaje`.")

    for modulo in unidad_aprendizaje["modulos"]:
        #print(f"   Módulo encontrado: {modulo.get('nombre', 'Sin nombre')}")
        for tema in modulo.get("temas", []):
            #print(f" Tema encontrado: {tema.get('nombre', 'Sin nombre')} - ID: {tema.get('id')}")
            
            recursos = tema.get("recursos", [])
            #print(f"  Recursos encontrados: {len(recursos)}")

            for recurso in recursos:
                resource_data = {
                    "topic_id": tema.get("id"),
                    "resource_id": recurso.get("id"),
                    "difficulty": recurso.get("dificultad", 0),
                    "learning_styles": recurso.get("tipos_aprendizaje", {}),
                    "type": recurso.get("tipo"),
                    "name": recurso.get("nombre", "Desconocido")
                }
                resources.append(resource_data)

    if not resources:
        raise ValueError(" Error: No se encontraron recursos educativos válidos.")

    #print(f" Total de recursos extraídos: {len(resources)}")
    return resources
