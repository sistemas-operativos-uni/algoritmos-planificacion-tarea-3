"""
modelo_pedido.py
-----------------
Práctica Dirigida N.º 04 -- "Torre de Control" (CocinaPerú Express)

Modelo de datos (Paso 1): cómo se representa cada pedido, y utilidades
compartidas por los cuatro algoritmos de planificación (algoritmos/).
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Pedido:
    id: str
    llegada: int
    duracion: int
    prioridad: int          # menor número = mayor prioridad

    # Campos que se completan durante la simulación
    inicio_primera_atencion: Optional[int] = None   # para tiempo de respuesta
    finalizacion: Optional[int] = None              # para tiempo de espera/retorno


def clonar(pedidos):
    """Valida la entrada común y crea pedidos sin resultados anteriores."""
    if not pedidos:
        raise ValueError("Se necesita al menos un pedido.")
    for p in pedidos:
        if not isinstance(p.id, str) or not p.id.strip():
            raise ValueError("Cada pedido necesita un identificador no vacío.")
        if any(type(valor) is not int for valor in (p.llegada, p.duracion, p.prioridad)):
            raise ValueError("Llegada, duración y prioridad deben ser enteros.")
        if p.llegada < 0 or p.duracion <= 0:
            raise ValueError("La llegada debe ser no negativa y la duración positiva.")
    if len({p.id for p in pedidos}) != len(pedidos):
        raise ValueError("Los identificadores de los pedidos deben ser únicos.")
    # Reiniciar los resultados permite reutilizar también una lista ya simulada.
    return [Pedido(p.id, p.llegada, p.duracion, p.prioridad) for p in pedidos]
