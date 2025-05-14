import json

import pytest
import requests

#Primero correr func start y posteriormente el comando pytest

#--- Comando para correr pruebas automatizadas ---
# pytest -s tests/test_optimizado.py

# ---- Entorno virtual ----
# env_tests

# ---- Scripts de ejecucion y terminacion ----

"""

NOTA: 
Los scripts están configurados para correr en una máquina MacOs, 
tendrían que adaptarse para correr en Windows.

"""
# ./terminate.sh
# ./terminate.sh



# URL del endpoint de Azure Function
url = "http://localhost:7071/api/optimize_resources" 

#Prueba con datos de entrada robusta
"""
datos_entrada_base = {
    "alumno": {
        "id": 1,
        "nombre": "Alan Joel",
        "tipos_aprendizaje": {
            "visual": 40,
            "auditivo": 30,
            "lectura_escritura": 20,
            "kinestesico": 10
        },
        "test_inicial": {
            "temas": [
                {
                    "id_tema": 1,
                    "nombre_tema": "Introducción",
                    "nivel": 2
                }
            ]
        }
    },
    
    "unidad_aprendizaje": {
      "id": 1,
      "nombre": "Unidad de Aprendizaje: Metodologías de Ingeniería de Software",
      "descripcion": "Exploración de las principales metodologías utilizadas en la ingeniería de software para el desarrollo eficiente de proyectos.",
      "modulos": [
        {
          "id": 1,
          "nombre": "Módulo 1: Fundamentos de Ingeniería de Software",
          "descripcion": "Bases y conceptos fundamentales en ingeniería de software.",
          "temas": [
            {
              "id": 1,
              "nombre": "Introducción a las metodologías de software",
              "descripcion": "Descripción general de metodologías de desarrollo como cascada, ágil, y espiral.",
              "recursos": [
                {
                  "id": 1,
                  "tipo": "video",
                  "nombre": "Historia de las metodologías",
                  "url": "https://example.com/historia_metodologias",
                  "descripcion": "Un video que cubre el origen y evolución de las metodologías de software.",
                  "tipos_aprendizaje": {
                    "visual": 50,
                    "auditivo": 30,
                    "lectura_escritura": 10,
                    "kinestesico": 10
                  },
                  "dificultad": 1
                },
                {
                  "id": 2,
                  "tipo": "documento",
                  "nombre": "Comparativa de metodologías",
                  "url": "https://example.com/comparativa_metodologias",
                  "descripcion": "Un documento PDF que compara las principales metodologías.",
                  "tipos_aprendizaje": {
                    "visual": 20,
                    "auditivo": 10,
                    "lectura_escritura": 60,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                },
                {
                  "id": 3,
                  "tipo": "artículo",
                  "nombre": "Tendencias actuales",
                  "url": "https://example.com/tendencias_metodologias",
                  "descripcion": "Artículo sobre tendencias modernas en el desarrollo ágil.",
                  "tipos_aprendizaje": {
                    "visual": 30,
                    "auditivo": 20,
                    "lectura_escritura": 40,
                    "kinestesico": 10
                  },
                  "dificultad": 1
                }
              ]
            },
            {
              "id": 2,
              "nombre": "Metodología Cascada",
              "descripcion": "Análisis detallado de la metodología en cascada y sus aplicaciones.",
              "recursos": [
                {
                  "id": 4,
                  "tipo": "video",
                  "nombre": "Proceso en cascada",
                  "url": "https://example.com/proceso_cascada",
                  "descripcion": "Video explicativo sobre cómo funciona la metodología en cascada.",
                  "tipos_aprendizaje": {
                    "visual": 60,
                    "auditivo": 20,
                    "lectura_escritura": 10,
                    "kinestesico": 10
                  },
                  "dificultad": 1
                },
                {
                  "id": 5,
                  "tipo": "documento",
                  "nombre": "Ventajas y desventajas",
                  "url": "https://example.com/ventajas_cascada",
                  "descripcion": "Documento que analiza los pros y contras de esta metodología.",
                  "tipos_aprendizaje": {
                    "visual": 30,
                    "auditivo": 10,
                    "lectura_escritura": 50,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                },
                {
                  "id": 6,
                  "tipo": "artículo",
                  "nombre": "Proyectos reales en cascada",
                  "url": "https://example.com/proyectos_cascada",
                  "descripcion": "Artículo que describe proyectos exitosos desarrollados en cascada.",
                  "tipos_aprendizaje": {
                    "visual": 40,
                    "auditivo": 10,
                    "lectura_escritura": 40,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                }
              ]
            },
            {
              "id": 3,
              "nombre": "Metodologías Ágiles",
              "descripcion": "Exploración de Scrum, Kanban y otras metodologías ágiles.",
              "recursos": [
                {
                  "id": 7,
                  "tipo": "video",
                  "nombre": "Introducción a Scrum",
                  "url": "https://example.com/scrum_basico",
                  "descripcion": "Video explicativo sobre los principios de Scrum.",
                  "tipos_aprendizaje": {
                    "visual": 50,
                    "auditivo": 30,
                    "lectura_escritura": 10,
                    "kinestesico": 10
                  },
                  "dificultad": 1
                },
                {
                  "id": 8,
                  "tipo": "documento",
                  "nombre": "Guía de Kanban",
                  "url": "https://example.com/guia_kanban",
                  "descripcion": "Documento que detalla los elementos clave de Kanban.",
                  "tipos_aprendizaje": {
                    "visual": 25,
                    "auditivo": 15,
                    "lectura_escritura": 50,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                },
                {
                  "id": 9,
                  "tipo": "artículo",
                  "nombre": "Casos de éxito con ágil",
                  "url": "https://example.com/casos_exito_agil",
                  "descripcion": "Artículo que detalla proyectos exitosos implementando metodologías ágiles.",
                  "tipos_aprendizaje": {
                    "visual": 40,
                    "auditivo": 20,
                    "lectura_escritura": 30,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                }
              ]
            },
            {
              "id": 4,
              "nombre": "Metodología Espiral",
              "descripcion": "Estudio de la metodología espiral y su enfoque iterativo.",
              "recursos": [
                {
                  "id": 10,
                  "tipo": "video",
                  "nombre": "Iteraciones en espiral",
                  "url": "https://example.com/iteraciones_espiral",
                  "descripcion": "Video explicativo sobre las iteraciones en la metodología espiral.",
                  "tipos_aprendizaje": {
                    "visual": 40,
                    "auditivo": 30,
                    "lectura_escritura": 20,
                    "kinestesico": 10
                  },
                  "dificultad": 1
                },
                {
                  "id": 11,
                  "tipo": "documento",
                  "nombre": "Guía de la metodología espiral",
                  "url": "https://example.com/guia_espiral",
                  "descripcion": "Documento que explica cada etapa de la metodología espiral.",
                  "tipos_aprendizaje": {
                    "visual": 30,
                    "auditivo": 20,
                    "lectura_escritura": 40,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                },
                {
                  "id": 12,
                  "tipo": "artículo",
                  "nombre": "Análisis de riesgos en espiral",
                  "url": "https://example.com/riesgos_espiral",
                  "descripcion": "Artículo que explica cómo manejar riesgos en la metodología espiral.",
                  "tipos_aprendizaje": {
                    "visual": 35,
                    "auditivo": 20,
                    "lectura_escritura": 35,
                    "kinestesico": 10
                  },
                  "dificultad": 3
                }
              ]
            },
            {
              "id": 5,
              "nombre": "Metodologías Híbridas",
              "descripcion": "Combinaciones de metodologías tradicionales y ágiles.",
              "recursos": [
                {
                  "id": 13,
                  "tipo": "video",
                  "nombre": "Híbridos exitosos",
                  "url": "https://example.com/hibridos_exitosos",
                  "descripcion": "Video sobre la implementación de metodologías híbridas.",
                  "tipos_aprendizaje": {
                    "visual": 40,
                    "auditivo": 30,
                    "lectura_escritura": 20,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                },
                {
                  "id": 14,
                  "tipo": "documento",
                  "nombre": "Guía para metodologías híbridas",
                  "url": "https://example.com/guia_hibridos",
                  "descripcion": "Documento detallado sobre la mezcla de metodologías tradicionales y ágiles.",
                  "tipos_aprendizaje": {
                    "visual": 30,
                    "auditivo": 20,
                    "lectura_escritura": 40,
                    "kinestesico": 10
                  },
                  "dificultad": 3
                },
                {
                  "id": 15,
                  "tipo": "artículo",
                  "nombre": "Estudios de caso híbridos",
                  "url": "https://example.com/caso_hibridos",
                  "descripcion": "Artículo que analiza proyectos que combinaron metodologías.",
                  "tipos_aprendizaje": {
                    "visual": 35,
                    "auditivo": 25,
                    "lectura_escritura": 30,
                    "kinestesico": 10
                  },
                  "dificultad": 3
                }
              ]
            },
            {
            "id": 6,
            "nombre": "DevOps y Entrega Continua",
            "descripcion": "Principios de integración y entrega continua en el desarrollo de software con enfoque DevOps.",
            "recursos": [
              {
                "id": 16,
                "tipo": "video",
                "nombre": "Introducción a DevOps",
                "url": "https://example.com/devops_intro",
                "descripcion": "Video introductorio sobre la cultura DevOps y sus principios.",
                "tipos_aprendizaje": {
                  "visual": 50,
                  "auditivo": 30,
                  "lectura_escritura": 10,
                  "kinestesico": 10
                },
                "dificultad": 1
              },
              {
                "id": 17,
                "tipo": "documento",
                "nombre": "Guía de Integración Continua",
                "url": "https://example.com/guia_integracion",
                "descripcion": "Documento detallado sobre la implementación de integración continua.",
                "tipos_aprendizaje": {
                  "visual": 25,
                  "auditivo": 15,
                  "lectura_escritura": 50,
                  "kinestesico": 10
                },
                "dificultad": 2
              },
              {
                "id": 18,
                "tipo": "artículo",
                "nombre": "Casos de éxito en DevOps",
                "url": "https://example.com/casos_devops",
                "descripcion": "Artículo con ejemplos de empresas que han implementado con éxito DevOps.",
                "tipos_aprendizaje": {
                  "visual": 40,
                  "auditivo": 20,
                  "lectura_escritura": 30,
                  "kinestesico": 10
                },
                "dificultad": 2
              }
            ]
          }
          ]
        },
        {
          "id": 2,
          "nombre": "Módulo 2: Diseño de Arquitecturas de Software",
          "descripcion": "Principios y patrones arquitectónicos en el desarrollo de software.",
          "temas": [
            {
              "id": 7,
              "nombre": "Patrones de Diseño",
              "descripcion": "Exploración de los patrones de diseño más utilizados en la ingeniería de software.",
              "recursos": [
                {
                  "id": 19,
                  "tipo": "video",
                  "nombre": "Patrones de diseño en la práctica",
                  "url": "https://example.com/patrones_diseno",
                  "descripcion": "Video que muestra ejemplos reales de patrones de diseño.",
                  "tipos_aprendizaje": {
                    "visual": 60,
                    "auditivo": 20,
                    "lectura_escritura": 10,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                },
                {
                  "id": 20,
                  "tipo": "documento",
                  "nombre": "Guía de patrones de diseño",
                  "url": "https://example.com/guia_patrones",
                  "descripcion": "Documento con una guía completa de patrones de diseño.",
                  "tipos_aprendizaje": {
                    "visual": 30,
                    "auditivo": 10,
                    "lectura_escritura": 50,
                    "kinestesico": 10
                  },
                  "dificultad": 3
                },
                {
                  "id": 21,
                  "tipo": "artículo",
                  "nombre": "Casos de estudio sobre patrones",
                  "url": "https://example.com/casos_patrones",
                  "descripcion": "Artículo con ejemplos de uso de patrones en la industria.",
                  "tipos_aprendizaje": {
                    "visual": 40,
                    "auditivo": 15,
                    "lectura_escritura": 35,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                }
              ]
            }
          ]
        },
        {
          "id": 3,
          "nombre": "Módulo 3: Pruebas y Mantenimiento de Software",
          "descripcion": "Metodologías y herramientas para pruebas y mantenimiento del software.",
          "temas": [
            {
              "id": 8,
              "nombre": "Pruebas Automatizadas",
              "descripcion": "Técnicas y herramientas para la automatización de pruebas en software.",
              "recursos": [
                {
                  "id": 22,
                  "tipo": "video",
                  "nombre": "Fundamentos de pruebas automatizadas",
                  "url": "https://example.com/pruebas_automatizadas",
                  "descripcion": "Video explicativo sobre la importancia de las pruebas automatizadas.",
                  "tipos_aprendizaje": {
                    "visual": 50,
                    "auditivo": 30,
                    "lectura_escritura": 10,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                },
                {
                  "id": 23,
                  "tipo": "documento",
                  "nombre": "Guía de herramientas de testing",
                  "url": "https://example.com/herramientas_testing",
                  "descripcion": "Documento sobre herramientas para pruebas automatizadas.",
                  "tipos_aprendizaje": {
                    "visual": 25,
                    "auditivo": 15,
                    "lectura_escritura": 50,
                    "kinestesico": 10
                  },
                  "dificultad": 2
                },
                {
                  "id": 24,
                  "tipo": "artículo",
                  "nombre": "Pruebas en la industria",
                  "url": "https://example.com/casos_testing",
                  "descripcion": "Artículo sobre cómo empresas aplican pruebas automatizadas.",
                  "tipos_aprendizaje": {
                    "visual": 35,
                    "auditivo": 25,
                    "lectura_escritura": 30,
                    "kinestesico": 10
                  },
                  "dificultad": 3
                }
              ]
            }
          ]
        }
      ]
    }
} 
"""


# Prueba con datos de entrada básicos
datos_entrada_base = {
    "alumno": {
        "id": 1,
        "nombre": "Alan Joel",
        "tipos_aprendizaje": {
            "visual": 40,
            "auditivo": 30,
            "lectura_escritura": 20,
            "kinestesico": 10
        },
        "test_inicial": {
            "temas": [
                {
                    "id_tema": 1,
                    "nombre_tema": "Introducción",
                    "nivel": 2
                }
            ]
        }
    },
    "unidad_aprendizaje": {
        "id": 1,
        "nombre": "UA Metodologías",
        "modulos": [
            {
                "id": 1,
                "temas": [
                    {
                        "id": 1,
                        "recursos": [
                            {
                                "id": 1,
                                "tipo": "video",
                                "nombre": "Video test",
                                "url": "https://example.com",
                                "tipos_aprendizaje": {
                                    "visual": 50,
                                    "auditivo": 30,
                                    "lectura_escritura": 10,
                                    "kinestesico": 10
                                },
                                "dificultad": 1
                            }
                        ]
                    }
                ]
            }
        ]
    }
} 

# Prueba de optimización
@pytest.mark.parametrize("algoritmo", ["GA_V1", "GA_V2"])
def test_optimizacion(algoritmo):
    
    
    print(f"\nIniciando prueba de optimización del algoritmo {algoritmo}")
    datos_entrada = dict(datos_entrada_base)
    datos_entrada["algoritmo"] = algoritmo
    
    response = requests.post(url, json=datos_entrada)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    print("Status code esperado: 200")
    print(f"Status code obtenido: {response.status_code}")
    
    
    assert response.headers['Content-Type'] == 'application/json', "Response is not in JSON format"
    resultado = response.json()
    
    print("\nResultados de la optimización:")
    print(f"Mejor solución: {resultado.get('mejor_solucion', 'No disponible')}")
    print(f"Puntaje de la mejor solución: {resultado.get('puntaje', 'No disponible')}")
    print("\nAsignación de materiales a los temas:")
    
    if 'asignacion' in resultado:
        for tema in resultado['asignacion']:
            print(f" Tema: {tema}")
    else:
        print("No se encontró asignación en la respuesta.")
    
    
    required_fields = ['mejor_solucion', 'puntaje', 'asignacion']
    for field in required_fields:
        assert field in resultado, f"El campo '{field}' no está presente en la respuesta."
    
    
    assert isinstance(resultado.get("mejor_solucion", []), list), "El campo 'mejor_solucion' no es una lista válida."
    assert isinstance(resultado.get("puntaje", -1), float), "El puntaje no es un número flotante válido."
    assert isinstance(resultado.get("asignacion", []), list), "El campo 'asignacion' no es una lista válida."
    
    print(f"\nPrueba de optimización para {algoritmo} completada con éxito" )
    print(f"\n--------------------------------------------------------------------------- " )
