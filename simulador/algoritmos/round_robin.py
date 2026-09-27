"""
algoritmos/round_robin.py
---------------------------
Round Robin (Paso 3), con quantum configurable. Sigue la misma lógica
del fragmento de referencia del enunciado: al vencer el quantum de un
pedido, primero se encolan las llegadas nuevas y luego (si aún le falta
trabajo) se reencola el pedido que acaba de correr.
"""

from modelo_pedido import clonar, por_id


def round_robin(pedidos, quantum):
    """Devuelve (pedidos_resueltos, tramos), en el mismo formato que
    fcfs(). A diferencia de los algoritmos no expropiativos, aquí un
    mismo pedido puede aparecer en varios tramos."""
    pedidos = clonar(pedidos)
    restante = {p.id: p.duracion for p in pedidos}
    llegada = {p.id: p.llegada for p in pedidos}
    ids_a_pedido = por_id(pedidos)

    pendientes = sorted(pedidos, key=lambda p: p.llegada)
    cola = []
    t = 0
    tramos = []

    def encolar_llegadas(hasta):
        while pendientes and llegada[pendientes[0].id] <= hasta:
            cola.append(pendientes.pop(0))

    encolar_llegadas(0)

    while cola:
        actual = cola.pop(0)
        if actual.inicio_primera_atencion is None:
            actual.inicio_primera_atencion = max(t, llegada[actual.id])

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

    resultado = [ids_a_pedido[p.id] for p in pedidos]
    return resultado, tramos
