# Torre de Control — Simulador de Algoritmos de Planificación
 
Práctica Dirigida N.º 04 · Sistemas Operativos (SW407) · UNI-FIIS
 
## Descripción
 
Simulador que calcula, sobre un mismo conjunto de pedidos, cómo los atendería cada uno de cuatro algoritmos de planificación de CPU: **FCFS**, **SJF**, **Round Robin** y **Prioridad**. Para cada algoritmo se obtiene el orden de atención, el tiempo de espera y el tiempo de respuesta de cada pedido, y sus promedios.
 
Caso: CocinaPerú Express — Torre de Control.
 
## Requisitos
 
- Python 3.8+
## Cómo ejecutar
 
```bash
cd simulador
python3 main.py
```
 
`main.py` corre los cuatro algoritmos sobre el conjunto de referencia, imprime la tabla comparativa y valida los resultados contra los valores esperados.
 
## Conjunto de referencia
 
| Pedido | Llegada | Duración | Prioridad |
|---|---|---|---|
| P1 | 0 | 5 | 3 |
| P2 | 1 | 3 | 4 |
| P3 | 2 | 8 | 1 |
| P4 | 3 | 6 | 2 |
 
## Valores esperados (validación)
 
| Algoritmo | Espera promedio | Respuesta promedio |
|---|---|---|
| FCFS | 5.75 | 5.75 |
| SJF | 5.25 | 5.25 |
| Round Robin (quantum = 4) | 9.25 | 4.00 |
| Prioridad | 7.75 | 7.75 |
 
Si el simulador no reproduce estos valores con el conjunto de referencia, hay un error en la implementación de ese algoritmo.
 
## Estructura
 
```
algoritmos-planificacion-tarea-3/
├── simulador/
│   ├── algoritmos/
│   │   ├── fcfs.py
│   │   ├── sjf.py
│   │   ├── round_robin.py
│   │   └── prioridad.py
│   ├── modelo_pedido.py
│   ├── metricas.py
│   ├── main.py
│   └── datos_referencia.py
├── docs/
│   ├── diseno/
│   └── capturas/
├── informe/
├── README.md
├── WORKPLAN.md
└── PROJECT.md
```
 
## Equipo
 
| Rol | Integrante |
|---|---|
| Coordinador(a) | — |
| Dev FCFS/SJF | — |
| Dev RR/Prioridad | — |
| Analista de resultados | — |
 
Detalle de tareas y dependencias: ver `WORKPLAN.md`. Contexto completo del proyecto: ver `PROJECT.md`.
 