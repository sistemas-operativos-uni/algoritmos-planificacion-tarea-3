"""
algoritmos/sjf.py
-------------------
Shortest Job First (Paso 2), no expropiativo: entre los pedidos ya
llegados, siempre elige el de menor duración.
"""

from modelo_pedido import clonar


def sjf(pedidos):
    """Devuelve (pedidos_resueltos, tramos), en el mismo formato que
    fcfs()."""
    pedidos = clonar(pedidos)
    pendientes = pedidos.copy()
    listos = []
    t = 0
    tramos = []

    while pendientes or listos:
        # Mover a "listos" todo lo que ya llegó
        recien_llegados = [p for p in pendientes if p.llegada <= t]
        for p in recien_llegados:
            pendientes.remove(p)
            listos.append(p)

        if not listos:
            # Nadie ha llegado aún: avanzar el reloj hasta la próxima llegada
            t = min(p.llegada for p in pendientes)
            continue

        # Elegir el de menor duración (empate: el que llegó primero)
        listos.sort(key=lambda p: (p.duracion, p.llegada))
        actual = listos.pop(0)

        inicio = max(t, actual.llegada)
        fin = inicio + actual.duracion
        actual.inicio_primera_atencion = inicio
        actual.finalizacion = fin
        tramos.append((actual.id, inicio, fin))
        t = fin

    return pedidos, tramos
