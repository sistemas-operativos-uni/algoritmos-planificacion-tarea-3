"""
main.py
--------
Práctica Dirigida N.º 04 -- "Torre de Control" (CocinaPerú Express)

Punto de entrada: corre los cuatro algoritmos de planificación (FCFS,
SJF, Round Robin y Prioridad) sobre el conjunto de referencia y sobre
un segundo conjunto propuesto por el equipo, imprime las tablas de
resultados, los diagramas de Gantt en texto, y verifica los resultados
contra los valores de referencia del enunciado.

Ejecución (desde esta misma carpeta, para que las importaciones
encuentren modelo_pedido.py, datos_referencia.py, metricas.py y el
paquete algoritmos/):
    python3 main.py
"""

from datos_referencia import PEDIDOS_REFERENCIA, PEDIDOS_PROPIOS
from algoritmos.fcfs import fcfs
from algoritmos.sjf import sjf
from algoritmos.round_robin import round_robin
from algoritmos.prioridad import prioridad
from metricas import (
    calcular_metricas, imprimir_tabla, imprimir_gantt,
    tabla_comparativa_global, verificar,
)


def ejecutar_todo(pedidos, titulo, quantum=4, verificar_referencia=False):
    print(f"\n{'#'*60}\n# {titulo}\n{'#'*60}")

    resumen = {}

    resueltos, tramos = fcfs(pedidos)
    filas, pe, pr = calcular_metricas(resueltos)
    imprimir_tabla("FCFS", filas, pe, pr)
    imprimir_gantt("FCFS", tramos)
    if verificar_referencia:
        verificar("FCFS", pe, pr)
    resumen["FCFS"] = (pe, pr)

    resueltos, tramos = sjf(pedidos)
    filas, pe, pr = calcular_metricas(resueltos)
    imprimir_tabla("SJF", filas, pe, pr)
    imprimir_gantt("SJF", tramos)
    if verificar_referencia:
        verificar("SJF", pe, pr)
    resumen["SJF"] = (pe, pr)

    resueltos, tramos = round_robin(pedidos, quantum)
    filas, pe, pr = calcular_metricas(resueltos)
    nombre_rr = f"Round Robin (q={quantum})"
    imprimir_tabla(nombre_rr, filas, pe, pr)
    imprimir_gantt(nombre_rr, tramos)
    if verificar_referencia:
        verificar(nombre_rr, pe, pr)
    resumen[nombre_rr] = (pe, pr)

    resueltos, tramos = prioridad(pedidos)
    filas, pe, pr = calcular_metricas(resueltos)
    imprimir_tabla("Prioridad", filas, pe, pr)
    imprimir_gantt("Prioridad", tramos)
    if verificar_referencia:
        verificar("Prioridad", pe, pr)
    resumen["Prioridad"] = (pe, pr)

    tabla_comparativa_global(resumen)
    return resumen


def main():
    ejecutar_todo(PEDIDOS_REFERENCIA, "CONJUNTO DE REFERENCIA (Semana 4)",
                  quantum=4, verificar_referencia=True)
    ejecutar_todo(PEDIDOS_PROPIOS, "SEGUNDO CONJUNTO (propuesto por el equipo)",
                  quantum=4, verificar_referencia=False)


if __name__ == "__main__":
    main()
