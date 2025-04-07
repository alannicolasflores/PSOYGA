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
            best_solution, best_score, asignacion = run_ga_optimization(
                alumno=alumno,
                unidad_aprendizaje=unidad_aprendizaje
            )
        elif algoritmo == "GA_V2":
            best_solution, best_score, asignacion = run_ga_v2_optimization(
                alumno=alumno,
                unidad_aprendizaje=unidad_aprendizaje
            )
        else:
            return func.HttpResponse(f"Algoritmo '{algoritmo}' no soportado.", status_code=400)

        resultado = {
            "mejor_solucion": best_solution,
            "puntaje": best_score,
            "asignacion": asignacion
        }

        return func.HttpResponse(json.dumps(resultado, indent=4), status_code=200, mimetype="application/json")

    except Exception as e:
        logging.error(f"Error general: {str(e)}")
        return func.HttpResponse(f"Error general: {str(e)}", status_code=500)