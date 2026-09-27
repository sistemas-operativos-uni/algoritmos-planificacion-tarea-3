"""
algoritmos/prioridad.py
--------------------------
Planificación por prioridad (Paso 3), no expropiativa. Menor número de
prioridad = mayor prioridad (se atiende primero).
"""

from modelo_pedido import clonar


def prioridad(pedidos):
    """Devuelve (pedidos_resueltos, tramos), en el mismo formato que
    fcfs()."""
    pedidos = clonar(pedidos)
    pendientes = pedidos.copy()
    listos = []
    t = 0
    tramos = []

    while pendientes or listos:
        recien_llegados = [p for p in pendientes if p.llegada <= t]
        for p in recien_llegados:
            pendientes.remove(p)
            listos.append(p)

        if not listos:
            t = min(p.llegada for p in pendientes)
            continue

        # Menor número de prioridad primero; empate: quien llegó primero
        listos.sort(key=lambda p: (p.prioridad, p.llegada))
        actual = listos.pop(0)

        inicio = max(t, actual.llegada)
        fin = inicio + actual.duracion
        actual.inicio_primera_atencion = inicio
        actual.finalizacion = fin
        tramos.append((actual.id, inicio, fin))
        t = fin

    return pedidos, tramos
