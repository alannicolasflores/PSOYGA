#!/bin/bash

# Función para detener el proceso de 'func start' y 'pytest' y salir de los entornos virtuales
detener_procesos() {
    echo "Comprobando si hay entornos virtuales activos..."

    if [[ "$VIRTUAL_ENV" != "" ]]; then
        deactivate
        echo "Salido del entorno virtual: $VIRTUAL_ENV."
    else
        echo "No hay entorno virtual activo para salir."
    fi

    # Detener todos los procesos de 'func'
    echo "Deteniendo todos los procesos de Azure Functions ('func')..."
    pkill -9 -f "func" && echo "Procesos 'func' detenidos." || echo "No se encontraron procesos 'func'."

    # Detener todos los procesos de 'pytest'
    echo "Deteniendo todos los procesos de pruebas ('pytest')..."
    pkill -9 -f "pytest" && echo "Procesos 'pytest' detenidos." || echo "No se encontraron procesos 'pytest'."

    # Esperar un poco para asegurarse de que los procesos se hayan detenido
    sleep 2

    # Verificar si el puerto 7071 sigue en uso
    echo "Verificando si el puerto 7071 está en uso..."
    PORT_PIDS=$(lsof -t -i :7071)
    if [ -n "$PORT_PIDS" ]; then
        echo "El puerto 7071 sigue en uso, matando procesos asociados..."
        echo "$PORT_PIDS" | xargs kill -9
        echo "Puerto 7071 liberado."
    else
        echo "El puerto 7071 ya está libre."
    fi

    # Confirmar que ambos procesos han sido detenidos
    echo "Procesos de Azure Functions y pruebas detenidos correctamente."
}

# Ejecutar la función para detener los procesos
detener_procesos

echo "Ejecución finalizada."