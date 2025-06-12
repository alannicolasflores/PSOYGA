import random


def generar_perfil_vark(estilo_dominante):
    estilos = ['visual', 'auditivo', 'lectura_escritura', 'kinestesico']
    
    
    porcentaje_dominante = random.randint(50, 60)
    resto = 100 - porcentaje_dominante
    
   
    estilos_restantes = [e for e in estilos if e != estilo_dominante]
    puntos = sorted(random.sample(range(1, resto), 2))  # Generar 2 puntos aleatorios
    p1 = puntos[0]
    p2 = puntos[1] - puntos[0]
    p3 = resto - puntos[1]
    
    # Crear el perfil VARK con los valores calculados
    distribucion = {estilo_dominante: porcentaje_dominante}
    for e, p in zip(estilos_restantes, [p1, p2, p3]):
        distribucion[e] = p
    suma_actual = sum(distribucion.values())
    if suma_actual != 100:
        diferencia = 100 - suma_actual
        distribucion[estilo_dominante] += diferencia  # Ajustar el último estilo para que sume 100
   
   
    return distribucion