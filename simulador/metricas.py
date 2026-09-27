"""
metricas.py
------------
Práctica Dirigida N.º 04 -- "Torre de Control" (CocinaPerú Express)

Cálculo de tiempo de espera y tiempo de respuesta (Paso 4), tablas de
resultados, diagrama de Gantt en texto, y verificación contra los
valores de referencia del enunciado.

DEFINICIONES USADAS (importante para el informe):
  - Tiempo de espera   = tiempo de retorno - duración
                        = (finalización - llegada) - duración
                        Es el tiempo TOTAL que el pedido pasa esperando
                        antes de ser atendido por completo. En Round
                        Robin esto puede acumularse en varios tramos (el
                        pedido entra y sale de la cola varias veces).

  - Tiempo de respuesta = primer instante en que el pedido recibe CPU
                          por primera vez - llegada.
                        En algoritmos NO expropiativos (FCFS, SJF,
                        Prioridad) el pedido recibe la CPU una sola vez
                        y la conserva hasta terminar, así que el tiempo
                        de respuesta coincide con el tiempo de espera.
                        En Round Robin NO coinciden: un pedido puede
                        empezar a ser atendido mucho antes de terminar.

  NOTA PARA EL INFORME: el enunciado de la práctica define el tiempo de
  respuesta como "finalización - llegada" (eso es, en realidad, el
  TIEMPO DE RETORNO o turnaround time, una tercera métrica distinta).
  Con esa fórmula literal, los promedios de Round Robin NO reproducen
  los valores de referencia (espera 9.25 / respuesta 4.0) del
  enunciado. Con la definición clásica usada aquí (primera vez que el
  proceso obtiene CPU - llegada) los cuatro algoritmos SÍ reproducen
  exactamente los valores de referencia. Vale la pena mencionar esta
  aclaración en la sección de metodología del informe, y confirmarla
  con el docente.
"""

from datos_referencia import REFERENCIA_ESPERADA


def calcular_metricas(pedidos_resueltos):
    """Devuelve, por pedido: espera y respuesta; y sus promedios."""
    filas = []
    for p in pedidos_resueltos:
        retorno = p.finalizacion - p.llegada
        espera = retorno - p.duracion
        respuesta = p.inicio_primera_atencion - p.llegada
        filas.append({
            "id": p.id, "llegada": p.llegada, "duracion": p.duracion,
            "finalizacion": p.finalizacion, "espera": espera,
            "respuesta": respuesta,
        })
    prom_espera = sum(f["espera"] for f in filas) / len(filas)
    prom_respuesta = sum(f["respuesta"] for f in filas) / len(filas)
    return filas, prom_espera, prom_respuesta


def imprimir_tabla(nombre, filas, prom_espera, prom_respuesta):
    print(f"\n--- {nombre} ---")
    print(f"{'Pedido':<8}{'Llegada':>9}{'Duración':>10}{'Fin':>6}{'Espera':>9}{'Respuesta':>11}")
    for f in sorted(filas, key=lambda x: x["id"]):
        print(f"{f['id']:<8}{f['llegada']:>9}{f['duracion']:>10}{f['finalizacion']:>6}"
              f"{f['espera']:>9}{f['respuesta']:>11}")
    print(f"{'PROMEDIO':<8}{'':>9}{'':>10}{'':>6}{prom_espera:>9.2f}{prom_respuesta:>11.2f}")


def imprimir_gantt(nombre, tramos):
    print(f"\nDiagrama de Gantt -- {nombre}")
    linea_ids = "|"
    linea_tiempos = "0"
    for tid, ini, fin in tramos:
        ancho = max(len(tid) + 2, (fin - ini))
        linea_ids += f" {tid} |"
        linea_tiempos += f"{'':>{max(1, ancho - len(str(fin)))}}{fin}"
    print(linea_ids)
    print(linea_tiempos)


def tabla_comparativa_global(resultados):
    """resultados: dict {nombre_algoritmo: (prom_espera, prom_respuesta)}"""
    print("\n=== TABLA COMPARATIVA DE LOS 4 ALGORITMOS ===")
    print(f"{'Algoritmo':<15}{'Espera prom.':>14}{'Respuesta prom.':>17}")
    for nombre, (espera, respuesta) in resultados.items():
        print(f"{nombre:<15}{espera:>14.2f}{respuesta:>17.2f}")


def verificar(nombre, prom_espera, prom_respuesta):
    """Compara (prom_espera, prom_respuesta) contra REFERENCIA_ESPERADA
    (datos_referencia.py) e imprime si coincide."""
    esperado = REFERENCIA_ESPERADA.get(nombre, {})
    ok = True
    if "espera" in esperado and abs(prom_espera - esperado["espera"]) > 0.01:
        ok = False
    if "respuesta" in esperado and abs(prom_respuesta - esperado["respuesta"]) > 0.01:
        ok = False
    estado = "OK ✓" if ok else "DIFERENTE ✗"
    print(f"  Verificación {nombre}: {estado} (referencia: {esperado})")
