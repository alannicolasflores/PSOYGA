#!/bin/bash

# Cambiar al directorio del proyecto
cd /Volumes/SSD_JOEL/TT/TT-1/PSOYGA

# Función para reiniciar los procesos en las terminales ya abiertas
reiniciar_funciones_y_pruebas() {
    # Terminal 1: Detener el proceso de Azure Function (func start)
    echo "Reiniciando el servidor de Azure Functions..."
    pkill -f "func start"  # Mata el proceso que está ejecutando `func start`

    # Esperar 5 segundos para asegurarse de que el proceso se detenga
    sleep 5

    # Terminal 2: Detener el proceso de pytest
    echo "Reiniciando las pruebas con pytest..."
    pkill -f "pytest"  # Mata el proceso que está ejecutando `pytest`

    # Esperar 2 segundos antes de reiniciar los procesos
    sleep 2

    # Reiniciar el servidor de Azure Functions en la misma terminal
    osascript -e 'tell application "Terminal" to do script "cd /Volumes/SSD_JOEL/TT/TT-1/PSOYGA && source env/bin/activate && func start"'

    # Esperar 10 segundos para dar tiempo a que 'func start' comience a ejecutarse
    sleep 10

    # Reiniciar las pruebas en la misma terminal de pruebas
    osascript -e 'tell application "Terminal" to do script "cd /Volumes/SSD_JOEL/TT/TT-1/PSOYGA && source env_tests/bin/activate && pytest -s tests/prueba_convergencia.py"'

    # Esperar a que los procesos terminen
    wait
}

# Usar inotifywait para esperar un cambio en el archivo de prueba
echo "Esperando cambios en el archivo 'prueba_convergencia.py'..."

# Monitorear el archivo `prueba_convergencia.py` para detectar cambios
inotifywait -e close_write tests/prueba_convergencia.py

# Cuando se detecte un cambio (guardar el archivo), ejecutar el proceso
echo "Cambio detectado en 'prueba_convergencia.py'. Reiniciando el proceso..."
reiniciar_funciones_y_pruebas

echo "Proceso completado. Esperando próximos cambios..."


