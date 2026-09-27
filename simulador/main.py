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

    for nombre, algoritmo in (
        ("FCFS", fcfs),
        ("SJF", sjf),
        (f"Round Robin (q={quantum})", round_robin),
        ("Prioridad", prioridad),
    ):
        if algoritmo is round_robin:
            resueltos, tramos = algoritmo(pedidos, quantum)
        else:
            resueltos, tramos = algoritmo(pedidos)
        filas, espera, respuesta = calcular_metricas(resueltos)
        imprimir_tabla(nombre, filas, espera, respuesta)
        imprimir_gantt(nombre, tramos)
        if verificar_referencia and not verificar(nombre, espera, respuesta):
            raise ValueError(f"{nombre} no coincide con los valores de referencia.")
        resumen[nombre] = (espera, respuesta)

    tabla_comparativa_global(resumen)
    return resumen


def main():
    ejecutar_todo(PEDIDOS_REFERENCIA, "CONJUNTO DE REFERENCIA (Semana 4)",
                  quantum=4, verificar_referencia=True)
    ejecutar_todo(PEDIDOS_PROPIOS, "SEGUNDO CONJUNTO (propuesto por el equipo)",
                  quantum=4, verificar_referencia=False)


if __name__ == "__main__":
    main()
