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
# ./run_tests.sh
# ./terminate.sh



# URL del endpoint de Azure Function
url = "http://localhost:7071/api/optimize_resources" 

#Prueba con datos de entrada robusta

datos_entrada_base =  {
    "alumno_1": {
        "id": 1,
        "nombre": "Mónica Díaz Cano",
        "tipos_aprendizaje": {
            "visual": 24,
            "auditivo": 51,
            "lectura_escritura": 21,
            "kinestesico": 4
        },
        "test_inicial": {
            "temas": [
                {
                    "id_tema": 1,
                    "nombre_tema": "Fundamentos de ingeniería de software",
                    "nivel": 1
                },
                {
                    "id_tema": 2,
                    "nombre_tema": "Plan de proyecto software",
                    "nivel": 1
                },
                {
                    "id_tema": 3,
                    "nombre_tema": "Modelos de procesos",
                    "nivel": 1
                },
                {
                    "id_tema": 4,
                    "nombre_tema": "Principios y metodologías ágiles",
                    "nivel": 1
                },
                {
                    "id_tema": 5,
                    "nombre_tema": "Ingeniería de requerimientos",
                    "nivel": 1
                },
                {
                    "id_tema": 6,
                    "nombre_tema": "Diseño del sistema software",
                    "nivel": 1
                },
                {
                    "id_tema": 7,
                    "nombre_tema": "Herramientas de modelado",
                    "nivel": 1
                },
                {
                    "id_tema": 8,
                    "nombre_tema": "Tipos de pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 9,
                    "nombre_tema": "Herramientas para pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 10,
                    "nombre_tema": "Evaluación de las pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 11,
                    "nombre_tema": "Calidad del proceso software",
                    "nivel": 1
                },
                {
                    "id_tema": 12,
                    "nombre_tema": "Calidad del producto software",
                    "nivel": 1
                },
                {
                    "id_tema": 13,
                    "nombre_tema": "Modelos y normas de calidad",
                    "nivel": 1
                },
                {
                    "id_tema": 14,
                    "nombre_tema": "Modelos de madurez",
                    "nivel": 1
                }
            ]
        }
    },
    "unidad_aprendizaje_1": {
        "id": 1,
        "nombre": "Unidad de Aprendizaje: Metodologías de Ingeniería de Software",
        "descripcion": "Exploración de las principales metodologías utilizadas en la ingeniería de software para el desarrollo eficiente de proyectos.",
        "modulos": [
            {
                "id": 1,
                "nombre": "Fundamentos",
                "temas": [
                    {
                        "id": 1,
                        "nombre": "Fundamentos de ingeniería de software",
                        "descripcion": "Descripción general de Fundamentos de ingeniería de software.",
                        "recursos": [
                            {
                                "id": 1,
                                "tipo": "pdf",
                                "nombre": "Fundamentos_de_ingeniería_de_software_5",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_5.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 2,
                                "tipo": "video",
                                "nombre": "Fundamentos_de_ingeniería_de_software_1",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_1.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 3,
                                "tipo": "audio",
                                "nombre": "Fundamentos_de_ingeniería_de_software_5",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_5.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 4,
                                "tipo": "presentacion",
                                "nombre": "Fundamentos_de_ingeniería_de_software_4",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_4.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "nombre": "Plan de proyecto software",
                        "descripcion": "Descripción general de Plan de proyecto software.",
                        "recursos": [
                            {
                                "id": 5,
                                "tipo": "pdf",
                                "nombre": "Plan_de_proyecto_software_1",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_1.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 6,
                                "tipo": "video",
                                "nombre": "Plan_de_proyecto_software_5",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_5.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 7,
                                "tipo": "audio",
                                "nombre": "Plan_de_proyecto_software_4",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_4.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 8,
                                "tipo": "presentacion",
                                "nombre": "Plan_de_proyecto_software_1",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_1.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 3,
                        "nombre": "Modelos de procesos",
                        "descripcion": "Descripción general de Modelos de procesos.",
                        "recursos": [
                            {
                                "id": 9,
                                "tipo": "pdf",
                                "nombre": "Modelos_de_procesos_4",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_4.com",
                                "descripcion": "Material sobre Modelos de procesos en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 10,
                                "tipo": "video",
                                "nombre": "Modelos_de_procesos_1",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_1.com",
                                "descripcion": "Material sobre Modelos de procesos en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 11,
                                "tipo": "audio",
                                "nombre": "Modelos_de_procesos_2",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_2.com",
                                "descripcion": "Material sobre Modelos de procesos en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 12,
                                "tipo": "presentacion",
                                "nombre": "Modelos_de_procesos_3",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_3.com",
                                "descripcion": "Material sobre Modelos de procesos en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 4,
                        "nombre": "Principios y metodologías ágiles",
                        "descripcion": "Descripción general de Principios y metodologías ágiles.",
                        "recursos": [
                            {
                                "id": 13,
                                "tipo": "pdf",
                                "nombre": "Principios_y_metodologías_ágiles_4",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_4.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 14,
                                "tipo": "video",
                                "nombre": "Principios_y_metodologías_ágiles_5",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_5.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 15,
                                "tipo": "audio",
                                "nombre": "Principios_y_metodologías_ágiles_4",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_4.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 16,
                                "tipo": "presentacion",
                                "nombre": "Principios_y_metodologías_ágiles_3",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_3.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": 2,
                "nombre": "Diseño y Construcción",
                "temas": [
                    {
                        "id": 5,
                        "nombre": "Ingeniería de requerimientos",
                        "descripcion": "Descripción general de Ingeniería de requerimientos.",
                        "recursos": [
                            {
                                "id": 17,
                                "tipo": "pdf",
                                "nombre": "Ingeniería_de_requerimientos_4",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_4.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 18,
                                "tipo": "video",
                                "nombre": "Ingeniería_de_requerimientos_2",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_2.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 19,
                                "tipo": "audio",
                                "nombre": "Ingeniería_de_requerimientos_1",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_1.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 20,
                                "tipo": "presentacion",
                                "nombre": "Ingeniería_de_requerimientos_4",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_4.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    },
                    {
                        "id": 6,
                        "nombre": "Diseño del sistema software",
                        "descripcion": "Descripción general de Diseño del sistema software.",
                        "recursos": [
                            {
                                "id": 21,
                                "tipo": "pdf",
                                "nombre": "Diseño_del_sistema_software_2",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_2.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 22,
                                "tipo": "video",
                                "nombre": "Diseño_del_sistema_software_1",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_1.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 23,
                                "tipo": "audio",
                                "nombre": "Diseño_del_sistema_software_5",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_5.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 24,
                                "tipo": "presentacion",
                                "nombre": "Diseño_del_sistema_software_5",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_5.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    },
                    {
                        "id": 7,
                        "nombre": "Herramientas de modelado",
                        "descripcion": "Descripción general de Herramientas de modelado.",
                        "recursos": [
                            {
                                "id": 25,
                                "tipo": "pdf",
                                "nombre": "Herramientas_de_modelado_1",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_1.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 26,
                                "tipo": "video",
                                "nombre": "Herramientas_de_modelado_2",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_2.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 27,
                                "tipo": "audio",
                                "nombre": "Herramientas_de_modelado_5",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_5.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 28,
                                "tipo": "presentacion",
                                "nombre": "Herramientas_de_modelado_1",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_1.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    }
                ]
            },
            {
                "id": 3,
                "nombre": "Pruebas de Software",
                "temas": [
                    {
                        "id": 8,
                        "nombre": "Tipos de pruebas",
                        "descripcion": "Descripción general de Tipos de pruebas.",
                        "recursos": [
                            {
                                "id": 29,
                                "tipo": "pdf",
                                "nombre": "Tipos_de_pruebas_software_1",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_1.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 30,
                                "tipo": "video",
                                "nombre": "Tipos_de_pruebas_software_4",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_4.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 31,
                                "tipo": "audio",
                                "nombre": "Tipos_de_pruebas_software_3",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_3.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 32,
                                "tipo": "presentacion",
                                "nombre": "Tipos_de_pruebas_software_2",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_2.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 9,
                        "nombre": "Herramientas para pruebas",
                        "descripcion": "Descripción general de Herramientas para pruebas.",
                        "recursos": [
                            {
                                "id": 33,
                                "tipo": "pdf",
                                "nombre": "Herramientas_para_pruebas_3",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_3.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 34,
                                "tipo": "video",
                                "nombre": "Herramientas_para_pruebas_5",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_5.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 35,
                                "tipo": "audio",
                                "nombre": "Herramientas_para_pruebas_2",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_2.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 36,
                                "tipo": "presentacion",
                                "nombre": "Herramientas_para_pruebas_4",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_4.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 10,
                        "nombre": "Evaluación de las pruebas",
                        "descripcion": "Descripción general de Evaluación de las pruebas.",
                        "recursos": [
                            {
                                "id": 37,
                                "tipo": "pdf",
                                "nombre": "Evaluación_de_las_pruebas_5",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_5.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 38,
                                "tipo": "video",
                                "nombre": "Evaluación_de_las_pruebas_5",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_5.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 39,
                                "tipo": "audio",
                                "nombre": "Evaluación_de_las_pruebas_2",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_2.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 40,
                                "tipo": "presentacion",
                                "nombre": "Evaluación_de_las_pruebas_4",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_4.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    }
                ]
            },
            {
                "id": 4,
                "nombre": "Calidad y Modelos de Madurez",
                "temas": [
                    {
                        "id": 11,
                        "nombre": "Calidad del proceso software",
                        "descripcion": "Descripción general de Calidad del proceso software.",
                        "recursos": [
                            {
                                "id": 41,
                                "tipo": "pdf",
                                "nombre": "Calidad_del_proceso_software_1",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_1.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 42,
                                "tipo": "video",
                                "nombre": "Calidad_del_proceso_software_5",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_5.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 43,
                                "tipo": "audio",
                                "nombre": "Calidad_del_proceso_software_5",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_5.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 44,
                                "tipo": "presentacion",
                                "nombre": "Calidad_del_proceso_software_2",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_2.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 12,
                        "nombre": "Calidad del producto software",
                        "descripcion": "Descripción general de Calidad del producto software.",
                        "recursos": [
                            {
                                "id": 45,
                                "tipo": "pdf",
                                "nombre": "Calidad_del_producto_software_1",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_1.com",
                                "descripcion": "Material sobre Calidad del producto software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 46,
                                "tipo": "video",
                                "nombre": "Calidad_del_producto_software_2",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_2.com",
                                "descripcion": "Material sobre Calidad del producto software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 47,
                                "tipo": "audio",
                                "nombre": "Calidad_del_producto_software_3",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_3.com",
                                "descripcion": "Material sobre Calidad del producto software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 48,
                                "tipo": "presentacion",
                                "nombre": "Calidad_del_producto_software_5",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_5.com",
                                "descripcion": "Material sobre Calidad del producto software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 13,
                        "nombre": "Modelos y normas de calidad",
                        "descripcion": "Descripción general de Modelos y normas de calidad.",
                        "recursos": [
                            {
                                "id": 49,
                                "tipo": "pdf",
                                "nombre": "Modelos_y_normas_de_calidad_4",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_4.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 50,
                                "tipo": "video",
                                "nombre": "Modelos_y_normas_de_calidad_4",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_4.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 51,
                                "tipo": "audio",
                                "nombre": "Modelos_y_normas_de_calidad_3",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_3.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 52,
                                "tipo": "presentacion",
                                "nombre": "Modelos_y_normas_de_calidad_5",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_5.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 14,
                        "nombre": "Modelos de madurez",
                        "descripcion": "Descripción general de Modelos de madurez.",
                        "recursos": [
                            {
                                "id": 53,
                                "tipo": "pdf",
                                "nombre": "Modelos_de_madurez_en_software_4",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_4.com",
                                "descripcion": "Material sobre Modelos de madurez en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 54,
                                "tipo": "video",
                                "nombre": "Modelos_de_madurez_en_software_1",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_1.com",
                                "descripcion": "Material sobre Modelos de madurez en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 55,
                                "tipo": "audio",
                                "nombre": "Modelos_de_madurez_en_software_4",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_4.com",
                                "descripcion": "Material sobre Modelos de madurez en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 56,
                                "tipo": "presentacion",
                                "nombre": "Modelos_de_madurez_en_software_3",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_3.com",
                                "descripcion": "Material sobre Modelos de madurez en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "alumno_2": {
        "id": 2,
        "nombre": "Raquel Moreno Poveda",
        "tipos_aprendizaje": {
            "visual": 25,
            "auditivo": 53,
            "lectura_escritura": 9,
            "kinestesico": 13
        },
        "test_inicial": {
            "temas": [
                {
                    "id_tema": 1,
                    "nombre_tema": "Fundamentos de ingeniería de software",
                    "nivel": 1
                },
                {
                    "id_tema": 2,
                    "nombre_tema": "Plan de proyecto software",
                    "nivel": 1
                },
                {
                    "id_tema": 3,
                    "nombre_tema": "Modelos de procesos",
                    "nivel": 1
                },
                {
                    "id_tema": 4,
                    "nombre_tema": "Principios y metodologías ágiles",
                    "nivel": 1
                },
                {
                    "id_tema": 5,
                    "nombre_tema": "Ingeniería de requerimientos",
                    "nivel": 1
                },
                {
                    "id_tema": 6,
                    "nombre_tema": "Diseño del sistema software",
                    "nivel": 1
                },
                {
                    "id_tema": 7,
                    "nombre_tema": "Herramientas de modelado",
                    "nivel": 1
                },
                {
                    "id_tema": 8,
                    "nombre_tema": "Tipos de pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 9,
                    "nombre_tema": "Herramientas para pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 10,
                    "nombre_tema": "Evaluación de las pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 11,
                    "nombre_tema": "Calidad del proceso software",
                    "nivel": 1
                },
                {
                    "id_tema": 12,
                    "nombre_tema": "Calidad del producto software",
                    "nivel": 1
                },
                {
                    "id_tema": 13,
                    "nombre_tema": "Modelos y normas de calidad",
                    "nivel": 1
                },
                {
                    "id_tema": 14,
                    "nombre_tema": "Modelos de madurez",
                    "nivel": 1
                }
            ]
        }
    },
    "unidad_aprendizaje_2": {
        "id": 1,
        "nombre": "Unidad de Aprendizaje: Metodologías de Ingeniería de Software",
        "descripcion": "Exploración de las principales metodologías utilizadas en la ingeniería de software para el desarrollo eficiente de proyectos.",
        "modulos": [
            {
                "id": 1,
                "nombre": "Fundamentos",
                "temas": [
                    {
                        "id": 1,
                        "nombre": "Fundamentos de ingeniería de software",
                        "descripcion": "Descripción general de Fundamentos de ingeniería de software.",
                        "recursos": [
                            {
                                "id": 1,
                                "tipo": "pdf",
                                "nombre": "Fundamentos_de_ingeniería_de_software_5",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_5.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 2,
                                "tipo": "video",
                                "nombre": "Fundamentos_de_ingeniería_de_software_1",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_1.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 3,
                                "tipo": "audio",
                                "nombre": "Fundamentos_de_ingeniería_de_software_5",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_5.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 4,
                                "tipo": "presentacion",
                                "nombre": "Fundamentos_de_ingeniería_de_software_4",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_4.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "nombre": "Plan de proyecto software",
                        "descripcion": "Descripción general de Plan de proyecto software.",
                        "recursos": [
                            {
                                "id": 5,
                                "tipo": "pdf",
                                "nombre": "Plan_de_proyecto_software_1",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_1.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 6,
                                "tipo": "video",
                                "nombre": "Plan_de_proyecto_software_5",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_5.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 7,
                                "tipo": "audio",
                                "nombre": "Plan_de_proyecto_software_4",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_4.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 8,
                                "tipo": "presentacion",
                                "nombre": "Plan_de_proyecto_software_1",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_1.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 3,
                        "nombre": "Modelos de procesos",
                        "descripcion": "Descripción general de Modelos de procesos.",
                        "recursos": [
                            {
                                "id": 9,
                                "tipo": "pdf",
                                "nombre": "Modelos_de_procesos_4",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_4.com",
                                "descripcion": "Material sobre Modelos de procesos en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 10,
                                "tipo": "video",
                                "nombre": "Modelos_de_procesos_1",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_1.com",
                                "descripcion": "Material sobre Modelos de procesos en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 11,
                                "tipo": "audio",
                                "nombre": "Modelos_de_procesos_2",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_2.com",
                                "descripcion": "Material sobre Modelos de procesos en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 12,
                                "tipo": "presentacion",
                                "nombre": "Modelos_de_procesos_3",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_3.com",
                                "descripcion": "Material sobre Modelos de procesos en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 4,
                        "nombre": "Principios y metodologías ágiles",
                        "descripcion": "Descripción general de Principios y metodologías ágiles.",
                        "recursos": [
                            {
                                "id": 13,
                                "tipo": "pdf",
                                "nombre": "Principios_y_metodologías_ágiles_4",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_4.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 14,
                                "tipo": "video",
                                "nombre": "Principios_y_metodologías_ágiles_5",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_5.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 15,
                                "tipo": "audio",
                                "nombre": "Principios_y_metodologías_ágiles_4",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_4.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 16,
                                "tipo": "presentacion",
                                "nombre": "Principios_y_metodologías_ágiles_3",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_3.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": 2,
                "nombre": "Diseño y Construcción",
                "temas": [
                    {
                        "id": 5,
                        "nombre": "Ingeniería de requerimientos",
                        "descripcion": "Descripción general de Ingeniería de requerimientos.",
                        "recursos": [
                            {
                                "id": 17,
                                "tipo": "pdf",
                                "nombre": "Ingeniería_de_requerimientos_4",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_4.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 18,
                                "tipo": "video",
                                "nombre": "Ingeniería_de_requerimientos_2",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_2.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 19,
                                "tipo": "audio",
                                "nombre": "Ingeniería_de_requerimientos_1",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_1.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 20,
                                "tipo": "presentacion",
                                "nombre": "Ingeniería_de_requerimientos_4",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_4.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    },
                    {
                        "id": 6,
                        "nombre": "Diseño del sistema software",
                        "descripcion": "Descripción general de Diseño del sistema software.",
                        "recursos": [
                            {
                                "id": 21,
                                "tipo": "pdf",
                                "nombre": "Diseño_del_sistema_software_2",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_2.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 22,
                                "tipo": "video",
                                "nombre": "Diseño_del_sistema_software_1",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_1.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 23,
                                "tipo": "audio",
                                "nombre": "Diseño_del_sistema_software_5",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_5.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 24,
                                "tipo": "presentacion",
                                "nombre": "Diseño_del_sistema_software_5",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_5.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    },
                    {
                        "id": 7,
                        "nombre": "Herramientas de modelado",
                        "descripcion": "Descripción general de Herramientas de modelado.",
                        "recursos": [
                            {
                                "id": 25,
                                "tipo": "pdf",
                                "nombre": "Herramientas_de_modelado_1",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_1.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 26,
                                "tipo": "video",
                                "nombre": "Herramientas_de_modelado_2",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_2.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 27,
                                "tipo": "audio",
                                "nombre": "Herramientas_de_modelado_5",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_5.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 28,
                                "tipo": "presentacion",
                                "nombre": "Herramientas_de_modelado_1",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_1.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    }
                ]
            },
            {
                "id": 3,
                "nombre": "Pruebas de Software",
                "temas": [
                    {
                        "id": 8,
                        "nombre": "Tipos de pruebas",
                        "descripcion": "Descripción general de Tipos de pruebas.",
                        "recursos": [
                            {
                                "id": 29,
                                "tipo": "pdf",
                                "nombre": "Tipos_de_pruebas_software_1",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_1.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 30,
                                "tipo": "video",
                                "nombre": "Tipos_de_pruebas_software_4",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_4.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 31,
                                "tipo": "audio",
                                "nombre": "Tipos_de_pruebas_software_3",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_3.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 32,
                                "tipo": "presentacion",
                                "nombre": "Tipos_de_pruebas_software_2",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_2.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 9,
                        "nombre": "Herramientas para pruebas",
                        "descripcion": "Descripción general de Herramientas para pruebas.",
                        "recursos": [
                            {
                                "id": 33,
                                "tipo": "pdf",
                                "nombre": "Herramientas_para_pruebas_3",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_3.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 34,
                                "tipo": "video",
                                "nombre": "Herramientas_para_pruebas_5",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_5.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 35,
                                "tipo": "audio",
                                "nombre": "Herramientas_para_pruebas_2",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_2.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 36,
                                "tipo": "presentacion",
                                "nombre": "Herramientas_para_pruebas_4",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_4.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 10,
                        "nombre": "Evaluación de las pruebas",
                        "descripcion": "Descripción general de Evaluación de las pruebas.",
                        "recursos": [
                            {
                                "id": 37,
                                "tipo": "pdf",
                                "nombre": "Evaluación_de_las_pruebas_5",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_5.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 38,
                                "tipo": "video",
                                "nombre": "Evaluación_de_las_pruebas_5",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_5.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 39,
                                "tipo": "audio",
                                "nombre": "Evaluación_de_las_pruebas_2",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_2.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 40,
                                "tipo": "presentacion",
                                "nombre": "Evaluación_de_las_pruebas_4",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_4.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    }
                ]
            },
            {
                "id": 4,
                "nombre": "Calidad y Modelos de Madurez",
                "temas": [
                    {
                        "id": 11,
                        "nombre": "Calidad del proceso software",
                        "descripcion": "Descripción general de Calidad del proceso software.",
                        "recursos": [
                            {
                                "id": 41,
                                "tipo": "pdf",
                                "nombre": "Calidad_del_proceso_software_1",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_1.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 42,
                                "tipo": "video",
                                "nombre": "Calidad_del_proceso_software_5",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_5.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 43,
                                "tipo": "audio",
                                "nombre": "Calidad_del_proceso_software_5",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_5.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 44,
                                "tipo": "presentacion",
                                "nombre": "Calidad_del_proceso_software_2",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_2.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 12,
                        "nombre": "Calidad del producto software",
                        "descripcion": "Descripción general de Calidad del producto software.",
                        "recursos": [
                            {
                                "id": 45,
                                "tipo": "pdf",
                                "nombre": "Calidad_del_producto_software_1",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_1.com",
                                "descripcion": "Material sobre Calidad del producto software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 46,
                                "tipo": "video",
                                "nombre": "Calidad_del_producto_software_2",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_2.com",
                                "descripcion": "Material sobre Calidad del producto software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 47,
                                "tipo": "audio",
                                "nombre": "Calidad_del_producto_software_3",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_3.com",
                                "descripcion": "Material sobre Calidad del producto software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 48,
                                "tipo": "presentacion",
                                "nombre": "Calidad_del_producto_software_5",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_5.com",
                                "descripcion": "Material sobre Calidad del producto software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 13,
                        "nombre": "Modelos y normas de calidad",
                        "descripcion": "Descripción general de Modelos y normas de calidad.",
                        "recursos": [
                            {
                                "id": 49,
                                "tipo": "pdf",
                                "nombre": "Modelos_y_normas_de_calidad_4",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_4.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 50,
                                "tipo": "video",
                                "nombre": "Modelos_y_normas_de_calidad_4",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_4.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 51,
                                "tipo": "audio",
                                "nombre": "Modelos_y_normas_de_calidad_3",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_3.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 52,
                                "tipo": "presentacion",
                                "nombre": "Modelos_y_normas_de_calidad_5",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_5.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 14,
                        "nombre": "Modelos de madurez",
                        "descripcion": "Descripción general de Modelos de madurez.",
                        "recursos": [
                            {
                                "id": 53,
                                "tipo": "pdf",
                                "nombre": "Modelos_de_madurez_en_software_4",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_4.com",
                                "descripcion": "Material sobre Modelos de madurez en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 54,
                                "tipo": "video",
                                "nombre": "Modelos_de_madurez_en_software_1",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_1.com",
                                "descripcion": "Material sobre Modelos de madurez en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 55,
                                "tipo": "audio",
                                "nombre": "Modelos_de_madurez_en_software_4",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_4.com",
                                "descripcion": "Material sobre Modelos de madurez en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 56,
                                "tipo": "presentacion",
                                "nombre": "Modelos_de_madurez_en_software_3",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_3.com",
                                "descripcion": "Material sobre Modelos de madurez en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "alumno_3": {
        "id": 3,
        "nombre": "Mario Moreno Cano",
        "tipos_aprendizaje": {
            "visual": 19,
            "auditivo": 60,
            "lectura_escritura": 12,
            "kinestesico": 9
        },
        "test_inicial": {
            "temas": [
                {
                    "id_tema": 1,
                    "nombre_tema": "Fundamentos de ingeniería de software",
                    "nivel": 1
                },
                {
                    "id_tema": 2,
                    "nombre_tema": "Plan de proyecto software",
                    "nivel": 1
                },
                {
                    "id_tema": 3,
                    "nombre_tema": "Modelos de procesos",
                    "nivel": 1
                },
                {
                    "id_tema": 4,
                    "nombre_tema": "Principios y metodologías ágiles",
                    "nivel": 1
                },
                {
                    "id_tema": 5,
                    "nombre_tema": "Ingeniería de requerimientos",
                    "nivel": 1
                },
                {
                    "id_tema": 6,
                    "nombre_tema": "Diseño del sistema software",
                    "nivel": 1
                },
                {
                    "id_tema": 7,
                    "nombre_tema": "Herramientas de modelado",
                    "nivel": 1
                },
                {
                    "id_tema": 8,
                    "nombre_tema": "Tipos de pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 9,
                    "nombre_tema": "Herramientas para pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 10,
                    "nombre_tema": "Evaluación de las pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 11,
                    "nombre_tema": "Calidad del proceso software",
                    "nivel": 1
                },
                {
                    "id_tema": 12,
                    "nombre_tema": "Calidad del producto software",
                    "nivel": 1
                },
                {
                    "id_tema": 13,
                    "nombre_tema": "Modelos y normas de calidad",
                    "nivel": 1
                },
                {
                    "id_tema": 14,
                    "nombre_tema": "Modelos de madurez",
                    "nivel": 1
                }
            ]
        }
    },
    "unidad_aprendizaje_3": {
        "id": 1,
        "nombre": "Unidad de Aprendizaje: Metodologías de Ingeniería de Software",
        "descripcion": "Exploración de las principales metodologías utilizadas en la ingeniería de software para el desarrollo eficiente de proyectos.",
        "modulos": [
            {
                "id": 1,
                "nombre": "Fundamentos",
                "temas": [
                    {
                        "id": 1,
                        "nombre": "Fundamentos de ingeniería de software",
                        "descripcion": "Descripción general de Fundamentos de ingeniería de software.",
                        "recursos": [
                            {
                                "id": 1,
                                "tipo": "pdf",
                                "nombre": "Fundamentos_de_ingeniería_de_software_5",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_5.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 2,
                                "tipo": "video",
                                "nombre": "Fundamentos_de_ingeniería_de_software_1",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_1.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 3,
                                "tipo": "audio",
                                "nombre": "Fundamentos_de_ingeniería_de_software_5",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_5.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 4,
                                "tipo": "presentacion",
                                "nombre": "Fundamentos_de_ingeniería_de_software_4",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_4.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "nombre": "Plan de proyecto software",
                        "descripcion": "Descripción general de Plan de proyecto software.",
                        "recursos": [
                            {
                                "id": 5,
                                "tipo": "pdf",
                                "nombre": "Plan_de_proyecto_software_1",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_1.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 6,
                                "tipo": "video",
                                "nombre": "Plan_de_proyecto_software_5",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_5.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 7,
                                "tipo": "audio",
                                "nombre": "Plan_de_proyecto_software_4",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_4.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 8,
                                "tipo": "presentacion",
                                "nombre": "Plan_de_proyecto_software_1",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_1.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 3,
                        "nombre": "Modelos de procesos",
                        "descripcion": "Descripción general de Modelos de procesos.",
                        "recursos": [
                            {
                                "id": 9,
                                "tipo": "pdf",
                                "nombre": "Modelos_de_procesos_4",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_4.com",
                                "descripcion": "Material sobre Modelos de procesos en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 10,
                                "tipo": "video",
                                "nombre": "Modelos_de_procesos_1",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_1.com",
                                "descripcion": "Material sobre Modelos de procesos en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 11,
                                "tipo": "audio",
                                "nombre": "Modelos_de_procesos_2",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_2.com",
                                "descripcion": "Material sobre Modelos de procesos en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 12,
                                "tipo": "presentacion",
                                "nombre": "Modelos_de_procesos_3",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_3.com",
                                "descripcion": "Material sobre Modelos de procesos en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 4,
                        "nombre": "Principios y metodologías ágiles",
                        "descripcion": "Descripción general de Principios y metodologías ágiles.",
                        "recursos": [
                            {
                                "id": 13,
                                "tipo": "pdf",
                                "nombre": "Principios_y_metodologías_ágiles_4",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_4.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 14,
                                "tipo": "video",
                                "nombre": "Principios_y_metodologías_ágiles_5",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_5.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 15,
                                "tipo": "audio",
                                "nombre": "Principios_y_metodologías_ágiles_4",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_4.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 16,
                                "tipo": "presentacion",
                                "nombre": "Principios_y_metodologías_ágiles_3",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_3.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": 2,
                "nombre": "Diseño y Construcción",
                "temas": [
                    {
                        "id": 5,
                        "nombre": "Ingeniería de requerimientos",
                        "descripcion": "Descripción general de Ingeniería de requerimientos.",
                        "recursos": [
                            {
                                "id": 17,
                                "tipo": "pdf",
                                "nombre": "Ingeniería_de_requerimientos_4",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_4.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 18,
                                "tipo": "video",
                                "nombre": "Ingeniería_de_requerimientos_2",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_2.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 19,
                                "tipo": "audio",
                                "nombre": "Ingeniería_de_requerimientos_1",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_1.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 20,
                                "tipo": "presentacion",
                                "nombre": "Ingeniería_de_requerimientos_4",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_4.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    },
                    {
                        "id": 6,
                        "nombre": "Diseño del sistema software",
                        "descripcion": "Descripción general de Diseño del sistema software.",
                        "recursos": [
                            {
                                "id": 21,
                                "tipo": "pdf",
                                "nombre": "Diseño_del_sistema_software_2",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_2.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 22,
                                "tipo": "video",
                                "nombre": "Diseño_del_sistema_software_1",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_1.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 23,
                                "tipo": "audio",
                                "nombre": "Diseño_del_sistema_software_5",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_5.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 24,
                                "tipo": "presentacion",
                                "nombre": "Diseño_del_sistema_software_5",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_5.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    },
                    {
                        "id": 7,
                        "nombre": "Herramientas de modelado",
                        "descripcion": "Descripción general de Herramientas de modelado.",
                        "recursos": [
                            {
                                "id": 25,
                                "tipo": "pdf",
                                "nombre": "Herramientas_de_modelado_1",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_1.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 26,
                                "tipo": "video",
                                "nombre": "Herramientas_de_modelado_2",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_2.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 27,
                                "tipo": "audio",
                                "nombre": "Herramientas_de_modelado_5",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_5.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 28,
                                "tipo": "presentacion",
                                "nombre": "Herramientas_de_modelado_1",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_1.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    }
                ]
            },
            {
                "id": 3,
                "nombre": "Pruebas de Software",
                "temas": [
                    {
                        "id": 8,
                        "nombre": "Tipos de pruebas",
                        "descripcion": "Descripción general de Tipos de pruebas.",
                        "recursos": [
                            {
                                "id": 29,
                                "tipo": "pdf",
                                "nombre": "Tipos_de_pruebas_software_1",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_1.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 30,
                                "tipo": "video",
                                "nombre": "Tipos_de_pruebas_software_4",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_4.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 31,
                                "tipo": "audio",
                                "nombre": "Tipos_de_pruebas_software_3",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_3.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 32,
                                "tipo": "presentacion",
                                "nombre": "Tipos_de_pruebas_software_2",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_2.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 9,
                        "nombre": "Herramientas para pruebas",
                        "descripcion": "Descripción general de Herramientas para pruebas.",
                        "recursos": [
                            {
                                "id": 33,
                                "tipo": "pdf",
                                "nombre": "Herramientas_para_pruebas_3",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_3.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 34,
                                "tipo": "video",
                                "nombre": "Herramientas_para_pruebas_5",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_5.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 35,
                                "tipo": "audio",
                                "nombre": "Herramientas_para_pruebas_2",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_2.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 36,
                                "tipo": "presentacion",
                                "nombre": "Herramientas_para_pruebas_4",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_4.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 10,
                        "nombre": "Evaluación de las pruebas",
                        "descripcion": "Descripción general de Evaluación de las pruebas.",
                        "recursos": [
                            {
                                "id": 37,
                                "tipo": "pdf",
                                "nombre": "Evaluación_de_las_pruebas_5",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_5.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 38,
                                "tipo": "video",
                                "nombre": "Evaluación_de_las_pruebas_5",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_5.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 39,
                                "tipo": "audio",
                                "nombre": "Evaluación_de_las_pruebas_2",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_2.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 40,
                                "tipo": "presentacion",
                                "nombre": "Evaluación_de_las_pruebas_4",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_4.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    }
                ]
            },
            {
                "id": 4,
                "nombre": "Calidad y Modelos de Madurez",
                "temas": [
                    {
                        "id": 11,
                        "nombre": "Calidad del proceso software",
                        "descripcion": "Descripción general de Calidad del proceso software.",
                        "recursos": [
                            {
                                "id": 41,
                                "tipo": "pdf",
                                "nombre": "Calidad_del_proceso_software_1",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_1.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 42,
                                "tipo": "video",
                                "nombre": "Calidad_del_proceso_software_5",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_5.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 43,
                                "tipo": "audio",
                                "nombre": "Calidad_del_proceso_software_5",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_5.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 44,
                                "tipo": "presentacion",
                                "nombre": "Calidad_del_proceso_software_2",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_2.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 12,
                        "nombre": "Calidad del producto software",
                        "descripcion": "Descripción general de Calidad del producto software.",
                        "recursos": [
                            {
                                "id": 45,
                                "tipo": "pdf",
                                "nombre": "Calidad_del_producto_software_1",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_1.com",
                                "descripcion": "Material sobre Calidad del producto software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 46,
                                "tipo": "video",
                                "nombre": "Calidad_del_producto_software_2",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_2.com",
                                "descripcion": "Material sobre Calidad del producto software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 47,
                                "tipo": "audio",
                                "nombre": "Calidad_del_producto_software_3",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_3.com",
                                "descripcion": "Material sobre Calidad del producto software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 48,
                                "tipo": "presentacion",
                                "nombre": "Calidad_del_producto_software_5",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_5.com",
                                "descripcion": "Material sobre Calidad del producto software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 13,
                        "nombre": "Modelos y normas de calidad",
                        "descripcion": "Descripción general de Modelos y normas de calidad.",
                        "recursos": [
                            {
                                "id": 49,
                                "tipo": "pdf",
                                "nombre": "Modelos_y_normas_de_calidad_4",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_4.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 50,
                                "tipo": "video",
                                "nombre": "Modelos_y_normas_de_calidad_4",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_4.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 51,
                                "tipo": "audio",
                                "nombre": "Modelos_y_normas_de_calidad_3",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_3.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 52,
                                "tipo": "presentacion",
                                "nombre": "Modelos_y_normas_de_calidad_5",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_5.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 14,
                        "nombre": "Modelos de madurez",
                        "descripcion": "Descripción general de Modelos de madurez.",
                        "recursos": [
                            {
                                "id": 53,
                                "tipo": "pdf",
                                "nombre": "Modelos_de_madurez_en_software_4",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_4.com",
                                "descripcion": "Material sobre Modelos de madurez en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 54,
                                "tipo": "video",
                                "nombre": "Modelos_de_madurez_en_software_1",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_1.com",
                                "descripcion": "Material sobre Modelos de madurez en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 55,
                                "tipo": "audio",
                                "nombre": "Modelos_de_madurez_en_software_4",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_4.com",
                                "descripcion": "Material sobre Modelos de madurez en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 56,
                                "tipo": "presentacion",
                                "nombre": "Modelos_de_madurez_en_software_3",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_3.com",
                                "descripcion": "Material sobre Modelos de madurez en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "alumno_4": {
        "id": 4,
        "nombre": "Antonio Serrano Vázquez",
        "tipos_aprendizaje": {
            "visual": 17,
            "auditivo": 53,
            "lectura_escritura": 7,
            "kinestesico": 23
        },
        "test_inicial": {
            "temas": [
                {
                    "id_tema": 1,
                    "nombre_tema": "Fundamentos de ingeniería de software",
                    "nivel": 1
                },
                {
                    "id_tema": 2,
                    "nombre_tema": "Plan de proyecto software",
                    "nivel": 1
                },
                {
                    "id_tema": 3,
                    "nombre_tema": "Modelos de procesos",
                    "nivel": 1
                },
                {
                    "id_tema": 4,
                    "nombre_tema": "Principios y metodologías ágiles",
                    "nivel": 1
                },
                {
                    "id_tema": 5,
                    "nombre_tema": "Ingeniería de requerimientos",
                    "nivel": 1
                },
                {
                    "id_tema": 6,
                    "nombre_tema": "Diseño del sistema software",
                    "nivel": 1
                },
                {
                    "id_tema": 7,
                    "nombre_tema": "Herramientas de modelado",
                    "nivel": 1
                },
                {
                    "id_tema": 8,
                    "nombre_tema": "Tipos de pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 9,
                    "nombre_tema": "Herramientas para pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 10,
                    "nombre_tema": "Evaluación de las pruebas",
                    "nivel": 1
                },
                {
                    "id_tema": 11,
                    "nombre_tema": "Calidad del proceso software",
                    "nivel": 1
                },
                {
                    "id_tema": 12,
                    "nombre_tema": "Calidad del producto software",
                    "nivel": 1
                },
                {
                    "id_tema": 13,
                    "nombre_tema": "Modelos y normas de calidad",
                    "nivel": 1
                },
                {
                    "id_tema": 14,
                    "nombre_tema": "Modelos de madurez",
                    "nivel": 1
                }
            ]
        }
    },
    "unidad_aprendizaje_4": {
        "id": 1,
        "nombre": "Unidad de Aprendizaje: Metodologías de Ingeniería de Software",
        "descripcion": "Exploración de las principales metodologías utilizadas en la ingeniería de software para el desarrollo eficiente de proyectos.",
        "modulos": [
            {
                "id": 1,
                "nombre": "Fundamentos",
                "temas": [
                    {
                        "id": 1,
                        "nombre": "Fundamentos de ingeniería de software",
                        "descripcion": "Descripción general de Fundamentos de ingeniería de software.",
                        "recursos": [
                            {
                                "id": 1,
                                "tipo": "pdf",
                                "nombre": "Fundamentos_de_ingeniería_de_software_5",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_5.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 2,
                                "tipo": "video",
                                "nombre": "Fundamentos_de_ingeniería_de_software_1",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_1.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 3,
                                "tipo": "audio",
                                "nombre": "Fundamentos_de_ingeniería_de_software_5",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_5.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 4,
                                "tipo": "presentacion",
                                "nombre": "Fundamentos_de_ingeniería_de_software_4",
                                "url": "https://Fundamentos_de_ingeniería_de_software/Fundamentos_de_ingeniería_de_software_4.com",
                                "descripcion": "Material sobre Fundamentos de ingeniería de software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 2,
                        "nombre": "Plan de proyecto software",
                        "descripcion": "Descripción general de Plan de proyecto software.",
                        "recursos": [
                            {
                                "id": 5,
                                "tipo": "pdf",
                                "nombre": "Plan_de_proyecto_software_1",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_1.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 6,
                                "tipo": "video",
                                "nombre": "Plan_de_proyecto_software_5",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_5.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 7,
                                "tipo": "audio",
                                "nombre": "Plan_de_proyecto_software_4",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_4.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 8,
                                "tipo": "presentacion",
                                "nombre": "Plan_de_proyecto_software_1",
                                "url": "https://Plan_de_proyecto_software/Plan_de_proyecto_software_1.com",
                                "descripcion": "Material sobre Plan de proyecto software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 3,
                        "nombre": "Modelos de procesos",
                        "descripcion": "Descripción general de Modelos de procesos.",
                        "recursos": [
                            {
                                "id": 9,
                                "tipo": "pdf",
                                "nombre": "Modelos_de_procesos_4",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_4.com",
                                "descripcion": "Material sobre Modelos de procesos en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 10,
                                "tipo": "video",
                                "nombre": "Modelos_de_procesos_1",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_1.com",
                                "descripcion": "Material sobre Modelos de procesos en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 11,
                                "tipo": "audio",
                                "nombre": "Modelos_de_procesos_2",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_2.com",
                                "descripcion": "Material sobre Modelos de procesos en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 12,
                                "tipo": "presentacion",
                                "nombre": "Modelos_de_procesos_3",
                                "url": "https://Modelos_de_procesos/Modelos_de_procesos_3.com",
                                "descripcion": "Material sobre Modelos de procesos en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    },
                    {
                        "id": 4,
                        "nombre": "Principios y metodologías ágiles",
                        "descripcion": "Descripción general de Principios y metodologías ágiles.",
                        "recursos": [
                            {
                                "id": 13,
                                "tipo": "pdf",
                                "nombre": "Principios_y_metodologías_ágiles_4",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_4.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 14,
                                "tipo": "video",
                                "nombre": "Principios_y_metodologías_ágiles_5",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_5.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 15,
                                "tipo": "audio",
                                "nombre": "Principios_y_metodologías_ágiles_4",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_4.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            },
                            {
                                "id": 16,
                                "tipo": "presentacion",
                                "nombre": "Principios_y_metodologías_ágiles_3",
                                "url": "https://Principios_y_metodologías_ágiles/Principios_y_metodologías_ágiles_3.com",
                                "descripcion": "Material sobre Principios y metodologías ágiles en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 1
                            }
                        ]
                    }
                ]
            },
            {
                "id": 2,
                "nombre": "Diseño y Construcción",
                "temas": [
                    {
                        "id": 5,
                        "nombre": "Ingeniería de requerimientos",
                        "descripcion": "Descripción general de Ingeniería de requerimientos.",
                        "recursos": [
                            {
                                "id": 17,
                                "tipo": "pdf",
                                "nombre": "Ingeniería_de_requerimientos_4",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_4.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 18,
                                "tipo": "video",
                                "nombre": "Ingeniería_de_requerimientos_2",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_2.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 19,
                                "tipo": "audio",
                                "nombre": "Ingeniería_de_requerimientos_1",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_1.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 20,
                                "tipo": "presentacion",
                                "nombre": "Ingeniería_de_requerimientos_4",
                                "url": "https://Ingeniería_de_requerimientos/Ingeniería_de_requerimientos_4.com",
                                "descripcion": "Material sobre Ingeniería de requerimientos en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    },
                    {
                        "id": 6,
                        "nombre": "Diseño del sistema software",
                        "descripcion": "Descripción general de Diseño del sistema software.",
                        "recursos": [
                            {
                                "id": 21,
                                "tipo": "pdf",
                                "nombre": "Diseño_del_sistema_software_2",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_2.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 22,
                                "tipo": "video",
                                "nombre": "Diseño_del_sistema_software_1",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_1.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 23,
                                "tipo": "audio",
                                "nombre": "Diseño_del_sistema_software_5",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_5.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 24,
                                "tipo": "presentacion",
                                "nombre": "Diseño_del_sistema_software_5",
                                "url": "https://Diseño_del_sistema_software/Diseño_del_sistema_software_5.com",
                                "descripcion": "Material sobre Diseño del sistema software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    },
                    {
                        "id": 7,
                        "nombre": "Herramientas de modelado",
                        "descripcion": "Descripción general de Herramientas de modelado.",
                        "recursos": [
                            {
                                "id": 25,
                                "tipo": "pdf",
                                "nombre": "Herramientas_de_modelado_1",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_1.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 26,
                                "tipo": "video",
                                "nombre": "Herramientas_de_modelado_2",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_2.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 27,
                                "tipo": "audio",
                                "nombre": "Herramientas_de_modelado_5",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_5.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            },
                            {
                                "id": 28,
                                "tipo": "presentacion",
                                "nombre": "Herramientas_de_modelado_1",
                                "url": "https://Herramientas_de_modelado/Herramientas_de_modelado_1.com",
                                "descripcion": "Material sobre Herramientas de modelado en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 2
                            }
                        ]
                    }
                ]
            },
            {
                "id": 3,
                "nombre": "Pruebas de Software",
                "temas": [
                    {
                        "id": 8,
                        "nombre": "Tipos de pruebas",
                        "descripcion": "Descripción general de Tipos de pruebas.",
                        "recursos": [
                            {
                                "id": 29,
                                "tipo": "pdf",
                                "nombre": "Tipos_de_pruebas_software_1",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_1.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 30,
                                "tipo": "video",
                                "nombre": "Tipos_de_pruebas_software_4",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_4.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 31,
                                "tipo": "audio",
                                "nombre": "Tipos_de_pruebas_software_3",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_3.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 32,
                                "tipo": "presentacion",
                                "nombre": "Tipos_de_pruebas_software_2",
                                "url": "https://Tipos_de_pruebas/Tipos_de_pruebas_software_2.com",
                                "descripcion": "Material sobre Tipos de pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 9,
                        "nombre": "Herramientas para pruebas",
                        "descripcion": "Descripción general de Herramientas para pruebas.",
                        "recursos": [
                            {
                                "id": 33,
                                "tipo": "pdf",
                                "nombre": "Herramientas_para_pruebas_3",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_3.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 34,
                                "tipo": "video",
                                "nombre": "Herramientas_para_pruebas_5",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_5.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 35,
                                "tipo": "audio",
                                "nombre": "Herramientas_para_pruebas_2",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_2.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 36,
                                "tipo": "presentacion",
                                "nombre": "Herramientas_para_pruebas_4",
                                "url": "https://Herramientas_para_pruebas/Herramientas_para_pruebas_4.com",
                                "descripcion": "Material sobre Herramientas para pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 10,
                        "nombre": "Evaluación de las pruebas",
                        "descripcion": "Descripción general de Evaluación de las pruebas.",
                        "recursos": [
                            {
                                "id": 37,
                                "tipo": "pdf",
                                "nombre": "Evaluación_de_las_pruebas_5",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_5.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 38,
                                "tipo": "video",
                                "nombre": "Evaluación_de_las_pruebas_5",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_5.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 39,
                                "tipo": "audio",
                                "nombre": "Evaluación_de_las_pruebas_2",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_2.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 40,
                                "tipo": "presentacion",
                                "nombre": "Evaluación_de_las_pruebas_4",
                                "url": "https://Evaluación_de_las_pruebas/Evaluación_de_las_pruebas_4.com",
                                "descripcion": "Material sobre Evaluación de las pruebas en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    }
                ]
            },
            {
                "id": 4,
                "nombre": "Calidad y Modelos de Madurez",
                "temas": [
                    {
                        "id": 11,
                        "nombre": "Calidad del proceso software",
                        "descripcion": "Descripción general de Calidad del proceso software.",
                        "recursos": [
                            {
                                "id": 41,
                                "tipo": "pdf",
                                "nombre": "Calidad_del_proceso_software_1",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_1.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 42,
                                "tipo": "video",
                                "nombre": "Calidad_del_proceso_software_5",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_5.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 43,
                                "tipo": "audio",
                                "nombre": "Calidad_del_proceso_software_5",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_5.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 44,
                                "tipo": "presentacion",
                                "nombre": "Calidad_del_proceso_software_2",
                                "url": "https://Calidad_del_proceso_software/Calidad_del_proceso_software_2.com",
                                "descripcion": "Material sobre Calidad del proceso software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 12,
                        "nombre": "Calidad del producto software",
                        "descripcion": "Descripción general de Calidad del producto software.",
                        "recursos": [
                            {
                                "id": 45,
                                "tipo": "pdf",
                                "nombre": "Calidad_del_producto_software_1",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_1.com",
                                "descripcion": "Material sobre Calidad del producto software en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 46,
                                "tipo": "video",
                                "nombre": "Calidad_del_producto_software_2",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_2.com",
                                "descripcion": "Material sobre Calidad del producto software en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 47,
                                "tipo": "audio",
                                "nombre": "Calidad_del_producto_software_3",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_3.com",
                                "descripcion": "Material sobre Calidad del producto software en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 48,
                                "tipo": "presentacion",
                                "nombre": "Calidad_del_producto_software_5",
                                "url": "https://Calidad_del_producto_software/Calidad_del_producto_software_5.com",
                                "descripcion": "Material sobre Calidad del producto software en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 13,
                        "nombre": "Modelos y normas de calidad",
                        "descripcion": "Descripción general de Modelos y normas de calidad.",
                        "recursos": [
                            {
                                "id": 49,
                                "tipo": "pdf",
                                "nombre": "Modelos_y_normas_de_calidad_4",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_4.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 50,
                                "tipo": "video",
                                "nombre": "Modelos_y_normas_de_calidad_4",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_4.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 51,
                                "tipo": "audio",
                                "nombre": "Modelos_y_normas_de_calidad_3",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_3.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 52,
                                "tipo": "presentacion",
                                "nombre": "Modelos_y_normas_de_calidad_5",
                                "url": "https://Modelos_y_normas_de_calidad/Modelos_y_normas_de_calidad_5.com",
                                "descripcion": "Material sobre Modelos y normas de calidad en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    },
                    {
                        "id": 14,
                        "nombre": "Modelos de madurez",
                        "descripcion": "Descripción general de Modelos de madurez.",
                        "recursos": [
                            {
                                "id": 53,
                                "tipo": "pdf",
                                "nombre": "Modelos_de_madurez_en_software_4",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_4.com",
                                "descripcion": "Material sobre Modelos de madurez en formato pdf.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 5,
                                    "lectura_escritura": 60,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 54,
                                "tipo": "video",
                                "nombre": "Modelos_de_madurez_en_software_1",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_1.com",
                                "descripcion": "Material sobre Modelos de madurez en formato video.",
                                "tipos_aprendizaje": {
                                    "visual": 30,
                                    "auditivo": 25,
                                    "lectura_escritura": 5,
                                    "kinestesico": 40
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 55,
                                "tipo": "audio",
                                "nombre": "Modelos_de_madurez_en_software_4",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_4.com",
                                "descripcion": "Material sobre Modelos de madurez en formato audio.",
                                "tipos_aprendizaje": {
                                    "visual": 10,
                                    "auditivo": 80,
                                    "lectura_escritura": 5,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            },
                            {
                                "id": 56,
                                "tipo": "presentacion",
                                "nombre": "Modelos_de_madurez_en_software_3",
                                "url": "https://Modelos_de_madurez/Modelos_de_madurez_en_software_3.com",
                                "descripcion": "Material sobre Modelos de madurez en formato presentacion.",
                                "tipos_aprendizaje": {
                                    "visual": 60,
                                    "auditivo": 5,
                                    "lectura_escritura": 30,
                                    "kinestesico": 5
                                },
                                "dificultad": 3
                            }
                        ]
                    }
                ]
            }
        ]
    },
                    
}
# Prueba de optimización
@pytest.mark.parametrize("algoritmo", ["GA_V2"])
def test_optimizacion(algoritmo):
    print(f"\nIniciando prueba de optimización del algoritmo {algoritmo}")
    
    for alumno_key in [k for k in datos_entrada_base.keys() if k.startswith("alumno")]:
        datos_entrada = dict(datos_entrada_base)
        datos_entrada["alumno"] = datos_entrada_base[alumno_key]
        unidad_key = f"unidad_aprendizaje_{alumno_key.split('_')[-1]}"
        datos_entrada["unidad_aprendizaje"] = datos_entrada_base.get(unidad_key, datos_entrada_base.get("unidad_aprendizaje"))
        datos_entrada["algoritmo"] = algoritmo
        print(f"\n==============================")
        print(f"Alumno: {datos_entrada['alumno']['nombre']}")
        print(f"==============================")
        
        response = requests.post(url, json=datos_entrada)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        print("Status code esperado: 200")
        print(f"Status code obtenido: {response.status_code}")
        
        
        assert response.headers['Content-Type'] == 'application/json', "Response is not in JSON format"
        resultado = response.json()
        
        print("\nResultados de la optimización:")
        print(f"Mejor solución: {resultado.get('mejor_solucion', 'No disponible')}")
        print(f"Puntaje de la mejor solución: {resultado.get('puntaje', 'No disponible')}")
        
        
        if 'generaciones' in resultado:
            for idx, gen in enumerate(resultado['generaciones']):
                print(f" Generación {idx+1}: {gen}")
        elif 'evolucion' in resultado and 'generaciones' in resultado['evolucion']:
            for idx, gen in enumerate(resultado['evolucion']['generaciones']):
                print(f" Generación {idx+1}: {gen}")
        else:
            print("\nNo se encontró información de generaciones en la respuesta.")
            
        
        required_fields = ['mejor_solucion', 'puntaje', 'asignacion']
        for field in required_fields:
            assert field in resultado, f"El campo '{field}' no está presente en la respuesta."
        
        
        assert isinstance(resultado.get("mejor_solucion", []), list), "El campo 'mejor_solucion' no es una lista válida."
        assert isinstance(resultado.get("puntaje", -1), float), "El puntaje no es un número flotante válido."
        assert isinstance(resultado.get("asignacion", []), list), "El campo 'asignacion' no es una lista válida."
        
        print(f"\nPrueba de optimización para {algoritmo} completada con éxito" )
        print(f"\n--------------------------------------------------------------------------- " )
