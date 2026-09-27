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
 
`main.py` corre los cuatro algoritmos sobre el conjunto de referencia y el conjunto propio del equipo. Para cada conjunto imprime las métricas por pedido, los Gantt y la tabla comparativa. La comparación con valores esperados se aplica al conjunto de referencia.
 
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
 
Si alguna métrica difiere, la ejecución informa la diferencia y se detiene. Los valores de Round Robin corresponden exclusivamente a quantum = 4.

## Modelo y métricas

Cada `Pedido` contiene `id`, `llegada`, `duracion`, `prioridad`, `inicio_primera_atencion` y `finalizacion`. Round Robin conserva la duración restante en un diccionario local. Cada algoritmo recibe la lista de pedidos y devuelve `(pedidos_resueltos, tramos)`, donde cada tramo es `(id, inicio, fin)`.

Los identificadores deben ser únicos y no vacíos. Llegada, duración y prioridad son enteros; llegada >= 0 y duración > 0. El quantum es un entero positivo. Cada algoritmo trabaja con copias nuevas, sin modificar la entrada. Los conjuntos se editan en `simulador/datos_referencia.py` y el quantum se configura en las llamadas de `main.py`.

- Espera = finalización − llegada − duración.
- Respuesta = inicio de la primera atención − llegada.
- Retorno = finalización − llegada.

El enunciado original y `PROMPT.md` contienen fórmulas contradictorias con los valores de referencia. El simulador usa las definiciones anteriores; en los algoritmos no expropiativos, espera y respuesta coinciden. Esta aclaración debe incluirse en el informe y consultarse con el docente.

## Algoritmos

- **FCFS:** atiende por llegada y conserva el orden de entrada en empates. Un pedido largo puede retrasar a los cortos: efecto convoy.
- **SJF:** elige la menor duración entre los pedidos disponibles; desempata por llegada y orden de entrada. Una llegada continua de trabajos cortos puede causar inanición de los largos.
- **Round Robin:** reparte turnos de hasta un quantum; encola nuevas llegadas antes de reinsertar el pedido interrumpido. Cuando no hay pedidos listos, avanza hasta la siguiente llegada.
- **Prioridad:** elige el menor número entre los pedidos disponibles; desempata por llegada y orden de entrada. El envejecimiento podría reducir la inanición, pero no forma parte del algoritmo solicitado.

Los Gantt de consola son esquemáticos, muestran los límites temporales e incluyen los intervalos de inactividad; las flechas no están a escala.

El [Gantt del conjunto de referencia](docs/diagrams/TIEMPOS%20DE%20ESPERA%20-%20RPTA%20-%20TAREA%203.png) ya contiene los cuatro algoritmos. El diagrama «COMPARACIÓN ALGORITMOS» resume el flujo; para Round Robin debe añadirse a su lectura que, si la cola está vacía y quedan llegadas pendientes, se avanza hasta la próxima llegada antes de sacar un pedido.
 
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
│   ├── context/
│   │   ├── TAREA_SO_3.md
│   │   ├── PROJECT.md
│   │   └── WORKPLAN.md
│   └── diagrams/
└── README.md
```
 
## Equipo
 
| Rol | Integrante |
|---|---|
| Coordinador(a) | Renato |
| Dev FCFS/SJF | Gabriel |
| Dev RR/Prioridad | Kike + Renato |
| Analista de resultados | Adán |
 
Detalle de tareas y dependencias: [WORKPLAN.md](docs/context/WORKPLAN.md). Contexto completo: [PROJECT.md](docs/context/PROJECT.md). Enunciado original: [TAREA_SO_3.md](docs/context/TAREA_SO_3.md).
 