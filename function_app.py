import sys
import os
import azure.functions as func
import logging
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from GA.main import run as run_ga_optimization
from GA_V2.main import run as run_ga_v2_optimization

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="optimize_resources", methods=["POST"])
def optimize_resources_endpoint(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        alumno = req_body.get("alumno")
        unidad_aprendizaje = req_body.get("unidad_aprendizaje")
        algoritmo = req_body.get("algoritmo", "GA_V2")
        if not alumno or not unidad_aprendizaje:
            return func.HttpResponse("Faltan datos de alumno o unidad de aprendizaje.", status_code=400)

        if algoritmo == "GA_V1":
            resultado = run_ga_optimization(
                alumno=alumno,
                unidad_aprendizaje=unidad_aprendizaje
            )
        elif algoritmo == "GA_V2":
            resultado = run_ga_v2_optimization(
                alumno=alumno,
                unidad_aprendizaje=unidad_aprendizaje
            )
        else:
            return func.HttpResponse(f"Algoritmo '{algoritmo}' no soportado.", status_code=400)

        # Asegurarse de que todos los valores sean serializables
        resultado_serializable = {
            "mejor_solucion": [int(x) for x in resultado["mejor_solucion"]],
            "puntaje": float(resultado["puntaje"]),
            "asignacion": [
                {
                    "id_tema": int(tema["id_tema"]),
                    "nombre_tema": str(tema["nombre_tema"]),
                    "materiales": [
                        {
                            "id": int(mat["id"]),
                            "tipo": str(mat["tipo"]),
                            "nombre": str(mat["nombre"]),
                            "url": str(mat["url"]),
                            "tipos_aprendizaje": {
                                "visual": int(mat["tipos_aprendizaje"]["visual"]),
                                "auditivo": int(mat["tipos_aprendizaje"]["auditivo"]),
                                "lectura_escritura": int(mat["tipos_aprendizaje"]["lectura_escritura"]),
                                "kinestesico": int(mat["tipos_aprendizaje"]["kinestesico"])
                            },
                            "dificultad": int(mat["dificultad"])
                        }
                        for mat in tema["materiales"]
                    ]
                }
                for tema in resultado["asignacion"]
            ]
        }

        # Convertir a JSON con formato legible
        response_json = json.dumps(resultado_serializable, indent=4, ensure_ascii=False)
        
        # Agregar encabezados para mejor visualización en PowerShell
        headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type"
        }

        return func.HttpResponse(
            response_json,
            status_code=200,
            headers=headers
        )

    except Exception as e:
        logging.error(f"Error general: {str(e)}")
        return func.HttpResponse(f"Error general: {str(e)}", status_code=500)