# PSOYGA - Sistema de Optimización de Recursos Educativos

Este sistema utiliza algoritmos genéticos para optimizar la selección de recursos educativos basándose en los estilos de aprendizaje del estudiante y su nivel de conocimiento previo.

## Estructura del Proyecto

```
PSOYGA/
├── GA/                     # Implementación original del algoritmo genético
├── GA_V2/                 # Implementación mejorada del algoritmo genético
├── function_app.py        # API HTTP con Azure Functions
└── test_input.json       # Ejemplo de formato de entrada
```

## Uso del Sistema

### Formato de Entrada

El sistema espera un JSON con la siguiente estructura:

```json
{
    "alumno": {
        "id": 1,
        "nombre": "Nombre del Alumno",
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
                    "nombre_tema": "Nombre del Tema",
                    "nivel": 2
                }
            ]
        }
    },
    "unidad_aprendizaje": {
        "id": 1,
        "nombre": "Nombre de la Unidad",
        "modulos": [
            {
                "id": 1,
                "temas": [
                    {
                        "id": 1,
                        "recursos": [
                            {
                                "id": 1,
                                "tipo": "tipo_recurso"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "algoritmo": "GA_V2"  // Opcional: "GA" o "GA_V2" (por defecto)
}
```

### Uso de la API

El sistema expone un endpoint HTTP POST `/optimize_resources` que acepta el JSON descrito anteriormente.

```http
POST /optimize_resources
Content-Type: application/json

{
    "alumno": { ... },
    "unidad_aprendizaje": { ... },
    "algoritmo": "GA_V2"
}
```

### Versiones del Algoritmo

- **GA_V2 (Recomendado)**: Versión mejorada del algoritmo genético con optimizaciones en el rendimiento y la calidad de las soluciones.
- **GA**: Implementación original del algoritmo genético.

### Parámetros Importantes

1. **Tipos de Aprendizaje**:
   - visual
   - auditivo
   - lectura_escritura
   - kinestesico

2. **Niveles de Conocimiento**:
   - Los niveles van de 0 a N, donde 0 representa ningún conocimiento
   - Se especifican en el `test_inicial` para cada tema

## Respuesta del Sistema

El sistema devolverá una lista optimizada de recursos educativos organizados por módulos y temas, considerando:
- Los estilos de aprendizaje del estudiante
- El nivel de conocimiento previo en cada tema
- La disponibilidad de recursos en la unidad de aprendizaje

## Ejemplo de Uso con curl

curl -X POST `
  http://localhost:7071/api/optimize_resources `
  -H 'Content-Type: application/json' `
  -d "@test_input.json"

Donde `@test_input.json` indica que se está usando el contenido del archivo `test_input.json` como body de la petición.

## Errores Comunes
