"""
modelo_pedido.py
-----------------
Práctica Dirigida N.º 04 -- "Torre de Control" (CocinaPerú Express)

Modelo de datos (Paso 1): cómo se representa cada pedido, y utilidades
compartidas por los cuatro algoritmos de planificación (algoritmos/).
"""

from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Pedido:
    id: str
    llegada: int
    duracion: int
    prioridad: int          # menor número = mayor prioridad

    # Campos que se completan durante la simulación
    inicio_primera_atencion: int = None   # para tiempo de respuesta
    finalizacion: int = None              # para tiempo de espera/retorno


def clonar(pedidos):
    """Devuelve una copia independiente de la lista de pedidos, para que
    cada algoritmo trabaje sobre su propia copia sin contaminar a los
    demás algoritmos ni al conjunto de datos original."""
    return deepcopy(pedidos)


def por_id(pedidos):
    """Devuelve un diccionario {id: Pedido} para acceso rápido por id."""
    return {p.id: p for p in pedidos}


def reordenar_como_original(pedidos_originales, tramos):
    """Reconstruye la lista de Pedido con los resultados (inicio de la
    primera atención y finalización) en el mismo orden del conjunto
    original, a partir de los tramos (id, inicio, fin) calculados por
    un algoritmo que puede atender un pedido en más de un tramo (o, en
    el caso de SJF/Prioridad, en uno solo)."""
    por_id_tramo = {}
    for tid, ini, fin in tramos:
        por_id_tramo.setdefault(tid, []).append((ini, fin))

    resultado = []
    for original in pedidos_originales:
        copia = deepcopy(original)
        apariciones = por_id_tramo[original.id]
        copia.inicio_primera_atencion = apariciones[0][0]   # primera vez que corrió
        copia.finalizacion = apariciones[-1][1]             # última vez que corrió
        resultado.append(copia)
    return resultado
