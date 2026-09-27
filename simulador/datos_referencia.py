"""
datos_referencia.py
---------------------
Práctica Dirigida N.º 04 -- "Torre de Control" (CocinaPerú Express)

Conjunto de referencia de la Semana 4, un segundo conjunto propuesto
por el equipo (Paso 5), y los valores de espera/respuesta promedio
esperados para verificar la implementación (Paso 2 y 3).
"""

from modelo_pedido import Pedido

# Conjunto de referencia de la Semana 4
PEDIDOS_REFERENCIA = [
    Pedido("P1", llegada=0, duracion=5, prioridad=3),
    Pedido("P2", llegada=1, duracion=3, prioridad=4),
    Pedido("P3", llegada=2, duracion=8, prioridad=1),
    Pedido("P4", llegada=3, duracion=6, prioridad=2),
]

# Segundo conjunto propio del equipo (Paso 5), para probar si la
# recomendación se mantiene. Edítenlo libremente.
PEDIDOS_PROPIOS = [
    Pedido("P1", llegada=0, duracion=4, prioridad=2),
    Pedido("P2", llegada=0, duracion=1, prioridad=1),
    Pedido("P3", llegada=2, duracion=6, prioridad=4),
    Pedido("P4", llegada=4, duracion=2, prioridad=3),
    Pedido("P5", llegada=5, duracion=3, prioridad=1),
]

# Valores de espera/respuesta promedio que el enunciado pide reproducir
# con el conjunto de referencia (Pasos 2 y 3).
REFERENCIA_ESPERADA = {
    "FCFS": {"espera": 5.75},
    "SJF": {"espera": 5.25},
    "Round Robin (q=4)": {"espera": 9.25, "respuesta": 4.0},
    "Prioridad": {"espera": 7.75},
}
