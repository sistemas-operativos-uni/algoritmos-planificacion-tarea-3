"""
algoritmos/round_robin.py
---------------------------
Round Robin (Paso 3), con quantum configurable. Sigue la misma lógica
del fragmento de referencia del enunciado: al vencer el quantum de un
pedido, primero se encolan las llegadas nuevas y luego (si aún le falta
trabajo) se reencola el pedido que acaba de correr.
"""

from collections import deque

from modelo_pedido import clonar


def round_robin(pedidos, quantum):
    """Devuelve (pedidos_resueltos, tramos), en el mismo formato que
    fcfs(). A diferencia de los algoritmos no expropiativos, aquí un
    mismo pedido puede aparecer en varios tramos."""
    if type(quantum) is not int or quantum <= 0:
        raise ValueError("El quantum debe ser un entero positivo.")
    pedidos = clonar(pedidos)
    restante = {p.id: p.duracion for p in pedidos}

    pendientes = deque(sorted(pedidos, key=lambda p: p.llegada))
    cola = deque()
    t = 0
    tramos = []

    def encolar_llegadas(hasta):
        while pendientes and pendientes[0].llegada <= hasta:
            cola.append(pendientes.popleft())

    encolar_llegadas(0)

    while cola or pendientes:
        if not cola:
            # La CPU espera hasta la próxima llegada; todavía quedan pedidos.
            t = pendientes[0].llegada
            encolar_llegadas(t)
        actual = cola.popleft()
        if actual.inicio_primera_atencion is None:
            actual.inicio_primera_atencion = t

        corre = min(quantum, restante[actual.id])
        inicio_tramo = t
        t += corre
        tramos.append((actual.id, inicio_tramo, t))
        restante[actual.id] -= corre

        encolar_llegadas(t)

        if restante[actual.id] > 0:
            cola.append(actual)
        else:
            actual.finalizacion = t

    return pedidos, tramos
