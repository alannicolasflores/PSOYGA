import random
from typing import List


def generar_poblacion(tamano_poblacion: int, datos_materiales: dict) -> List[List[int]]:
    """
    Genera una población inicial de individuos binarios.
    
    Args:
        tamano_poblacion (int): Tamaño de la población.
        datos_materiales (dict): Datos de los materiales educativos.
    
    Returns:
        List[List[int]]: Población inicial de individuos.
    """
    longitud_individuo = sum(
        len(tema['recursos'])
        for modulo in datos_materiales['unidad_aprendizaje']['modulos']
        for tema in modulo['temas']
    )
    
    # Si solo hay un recurso, generar una población con todos los individuos seleccionando ese recurso
    if longitud_individuo == 1:
        return [[1] for _ in range(tamano_poblacion)]
    
    # Para más de un recurso, generar población aleatoria
    poblacion = []
    for _ in range(tamano_poblacion):
        individuo = [random.randint(0, 1) for _ in range(longitud_individuo)]
        poblacion.append(individuo)
    return poblacion
