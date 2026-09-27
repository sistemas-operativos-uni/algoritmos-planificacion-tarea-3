"""
algoritmos/fcfs.py
--------------------
First-Come, First-Served (Paso 2): atiende los pedidos en orden de
llegada, sin expropiación.
"""

from modelo_pedido import clonar


def fcfs(pedidos):
    """Devuelve (pedidos_resueltos, tramos) para el conjunto dado.

    pedidos_resueltos: copia de los pedidos con inicio_primera_atencion
    y finalizacion ya calculados.
    tramos: lista de (id, inicio, fin) en el orden de ejecución, para
    el diagrama de Gantt.
    """
    pedidos = clonar(pedidos)
    pedidos.sort(key=lambda p: p.llegada)

    t = 0
    tramos = []
    for p in pedidos:
        inicio = max(t, p.llegada)
        fin = inicio + p.duracion
        p.inicio_primera_atencion = inicio
        p.finalizacion = fin
        tramos.append((p.id, inicio, fin))
        t = fin
    return pedidos, tramos
