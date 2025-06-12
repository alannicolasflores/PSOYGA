#!/bin/bash

# Función para detener el proceso de 'func start' y 'pytest' y salir de los entornos virtuales
detener_procesos() {
    # Salir de los entornos virtuales si están activos
    echo "Comprobando si hay entornos virtuales activos..."

    if [[ "$VIRTUAL_ENV" != "" ]]; then
        deactivate
        echo "Salido del entorno virtual: $VIRTUAL_ENV."
    else
        echo "No hay entorno virtual activo para salir."
    fi

    # Detener el proceso de 'func start'
    echo "Deteniendo el servidor de Azure Functions ('func start')..."
    pkill -f "func start"  # Mata el proceso de 'func start'

    # Esperar un poco para asegurarse de que el proceso se haya detenido
    sleep 3

    # Detener el proceso de 'pytest'
    echo "Deteniendo las pruebas con 'pytest'..."
    pkill -f "pytest"  # Mata el proceso de 'pytest'

    # Confirmar que ambos procesos han sido detenidos
    echo "Proceso de 'func start' y 'pytest' detenidos."

    # Verificar si el puerto 7071 sigue en uso
    echo "Verificando si el puerto 7071 está en uso..."
    PORT_IN_USE=$(lsof -i :7071)
    if [ -n "$PORT_IN_USE" ]; then
        echo "El puerto 7071 sigue en uso, matando el proceso..."
        # Si el puerto sigue ocupado, matamos el proceso que está usando el puerto 7071
        lsof -t -i :7071 | xargs kill -9
        echo "Puerto 7071 liberado."
    else
        echo "El puerto 7071 ya está libre."
    fi
}

# Ejecutar la función para detener los procesos
detener_procesos

echo "Ejecución finalizada."

