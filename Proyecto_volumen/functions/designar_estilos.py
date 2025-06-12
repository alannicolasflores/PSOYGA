def asignar_estilos(tipo_material):
    if tipo_material == "video":
        return {
            "visual": 30,
            "auditivo": 25,
            "lectura_escritura": 5,
            "kinestesico": 40
        }
    elif tipo_material == "presentacion":  # Presentaciones de PowerPoint
        return {
            "visual": 60,
            "auditivo": 5,
            "lectura_escritura": 30,
            "kinestesico": 5
        }
    elif tipo_material == "pdf":
        return {
            "visual": 30,
            "auditivo": 5,
            "lectura_escritura": 60,
            "kinestesico": 5
        }
    elif tipo_material == "audio":
        return {
            "visual": 10,
            "auditivo": 80,
            "lectura_escritura": 5,
            "kinestesico": 5
        }
    else:
        return {
            "visual": 25,
            "auditivo": 25,
            "lectura_escritura": 25,
            "kinestesico": 25
        }