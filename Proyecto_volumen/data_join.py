import json
import os
import random


def generar_perfil_vark(estilo_dominante):
    estilos = ['visual', 'auditivo', 'lectura_escritura', 'kinestesico']
    
    # Asignamos un porcentaje mayor al estilo dominante
    porcentaje_dominante = random.randint(50, 60)  # El estilo dominante será el más alto
    resto = 100 - porcentaje_dominante
    
    # Asignamos los porcentajes de los otros estilos de forma aleatoria
    estilos_restantes = [e for e in estilos if e != estilo_dominante]
    puntos = sorted(random.sample(range(1, resto), 2))  # Generar 2 puntos aleatorios para los estilos restantes
    p1 = puntos[0]
    p2 = puntos[1] - puntos[0]
    p3 = resto - puntos[1]
    
    # Crear el perfil VARK con los valores calculados
    distribucion = {estilo_dominante: porcentaje_dominante}
    for e, p in zip(estilos_restantes, [p1, p2, p3]):
        distribucion[e] = p
    
    # Asegurar que la suma total sea 100, ajustando el último estilo si es necesario
    suma_actual = sum(distribucion.values())
    if suma_actual != 100:
        diferencia = 100 - suma_actual
        distribucion[estilo_dominante] += diferencia  # Ajustar el último estilo para que sume 100
    
    return distribucion


# Definir el número de alumnos y los niveles
num_alumnos = 36
niveles = [1, 2, 3]
estilo_map = {'visual': 'Visual', 'auditivo': 'Auditivo', 'lectura_escritura': 'Lectura/Escritura', 'kinestesico': 'Kinestésico'}
nombres = ['Alan', 'Luis', 'Carlos', 'José', 'Maria', 'Ana', 'Pedro', 'Javier', 'Raúl', 'Marta']
apellidos1 = ['Pérez', 'Gómez', 'Martínez', 'López', 'Hernández', 'Rodríguez', 'Díaz', 'García', 'Jiménez', 'Sánchez']
apellidos2 = ['Fernández', 'Ruiz', 'Vázquez', 'Romero', 'Moreno', 'Muñoz', 'Alonso', 'Ramos', 'Torres', 'Gil']
temas = ["Fundamentos de ingeniería de software", "Plan de proyecto software", "Modelos de procesos", 
         "Principios y metodologías ágiles", "Ingeniería de requerimientos", "Diseño del sistema software", 
         "Herramientas de modelado", "Tipos de pruebas", "Herramientas para pruebas", 
         "Evaluación de las pruebas", "Calidad del proceso software", "Calidad del producto software", 
         "Modelos y normas de calidad", "Modelos de madurez"]

# Ruta donde se encuentran los archivos de alumnos
alumnos_path = "data/alumnos_IS"
# Ruta donde se encuentran los archivos de unidad
unidad_path = "data/unidad_IS"  
# Ruta donde se generarán los archivos combinados
ruta_salida = "data/datos_finales"  

# Crear la carpeta de salida si no existe
os.makedirs(ruta_salida, exist_ok=True)

# Verificar si hay archivos JSON en la carpeta de unidad
archivos_unidad = [f for f in os.listdir(unidad_path) if f.endswith('.json')]

if not archivos_unidad:
    raise FileNotFoundError(f"No se encontraron archivos JSON en la ruta: {unidad_path}")
else:
    print(f"Se encontraron {len(archivos_unidad)} archivos de unidad en la ruta: {unidad_path}")

# Procesar cada archivo de unidad
for archivo_unidad in archivos_unidad:
    ruta_unidad = os.path.join(unidad_path, archivo_unidad)
    
    with open(ruta_unidad, "r", encoding="utf-8") as f:
        unidad_datos = json.load(f)

    # Verificar que la unidad de aprendizaje se haya cargado correctamente
    if not unidad_datos:
        print(f"Error: La unidad de aprendizaje {archivo_unidad} está vacía.")
        continue  # Si la unidad está vacía, saltamos este archivo

    alumnos = {}  # Diccionario para almacenar todos los alumnos
    alumno_id = 1  # Empezar con el ID 1

    # Generar los datos para los 36 alumnos por cada estilo y nivel
    for estilo_corto, estilo_nombre in estilo_map.items():
        for nivel in niveles:
            # Generar 36 alumnos por estilo y nivel
            for i in range(num_alumnos):
                perfil_vark = generar_perfil_vark(estilo_corto)
                temas_nivel = [{"id_tema": idx+1, "nombre_tema": tema, "nivel": nivel} for idx, tema in enumerate(temas)]
                nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos1)} {random.choice(apellidos2)}"
                alumnos[f"alumno_{alumno_id}"] = {
                        "id": alumno_id,  # ID único para cada alumno
                        "nombre": nombre_completo,
                        "tipos_aprendizaje": {
                            "visual": perfil_vark['visual'],
                            "auditivo": perfil_vark['auditivo'],
                            "lectura_escritura": perfil_vark['lectura_escritura'],
                            "kinestesico": perfil_vark['kinestesico']
                        },
                        "test_inicial": {
                            "temas": temas_nivel
                        },
                        "unidad_aprendizaje": unidad_datos  # Aquí agregamos la unidad completa al alumno
                    }
                alumno_id += 1

    # Generar el archivo combinado con todos los alumnos y la unidad
    archivo_combinado = {
        "alumnos": alumnos,  # Todos los alumnos con su unidad de aprendizaje
        "unidad_aprendizaje": unidad_datos  # Unidad de aprendizaje
    }

    # Generar el nombre del archivo de salida para el archivo combinado
    nombre_salida = f"union_{archivo_unidad}"
    ruta_salida_final = os.path.join(ruta_salida, nombre_salida)

    # Guardar el archivo combinado
    with open(ruta_salida_final, "w", encoding="utf-8") as f:
        json.dump(archivo_combinado, f, indent=4, ensure_ascii=False)
    
    print(f"Archivo combinado generado: {ruta_salida_final}")

print(f"\nProceso completado. Archivos combinados generados en {ruta_salida}.")
