# 1. Introducción al proyecto

Torre de Control es un simulador de planificación de pedidos para CocinaPerú Express. Trata cada pedido como un proceso que tiene tiempo de llegada, duración y prioridad. Su objetivo es comparar cómo FCFS, SJF, Round Robin y Prioridad atienden los mismos pedidos. Para cada algoritmo muestra el orden de ejecución, las métricas por pedido y los promedios.

El programa está escrito en Python 3.8 o superior y usa solo la biblioteca estándar. Se ejecuta desde `simulador` con `python3 main.py`.

# 2. Setup inicial: fase 0

Se organizó el proyecto en `simulador` (código), `docs/context` (enunciado y plan), `docs/diagrams` (diagramas) y `docs/outputs` (capturas de ejecución). `README.md` describe cómo iniciar el simulador. La entrada `simulador/main.py` conecta los datos, los cuatro algoritmos y el cálculo de métricas.

El flujo del sistema es: conjuntos de pedidos en `datos_referencia.py` → algoritmo de planificación → pedidos resueltos y tramos de ejecución → `metricas.py` → tablas, Gantt y comparación de referencia. El diagrama `diagrams/ORQUESTACION ALGORITMOS - TAREA 3.png` muestra estas conexiones. `diagrams/COMPARACIÓN ALGORITMOS - TAREA 3.png` resume la elección de pedidos en SJF, Prioridad y Round Robin. El Gantt gráfico del conjunto de referencia está en `diagrams/TIEMPOS DE ESPERA - RPTA - TAREA 3.png`.

# 3. Implementación

## Fase 1. Modelo de pedidos

`modelo_pedido.py` define la clase `Pedido` con identificador, llegada, duración, prioridad, primera atención y finalización. La función `clonar` valida los datos y crea copias sin resultados previos; así cada algoritmo trabaja sobre el mismo conjunto original. Exige identificadores únicos, llegada no negativa y duración positiva.

`datos_referencia.py` contiene los cuatro pedidos del enunciado, un segundo conjunto de cinco pedidos y los promedios esperados del primer conjunto. En Prioridad, un número menor significa mayor prioridad.

## Fase 2. FCFS y SJF

`fcfs.py` ordena los pedidos por llegada y ejecuta cada uno hasta terminar. Cuando dos llegan al mismo tiempo, conserva su orden de entrada. Su principal límite es el efecto convoy: un pedido largo puede retrasar a varios cortos.

`sjf.py` elige el pedido de menor duración entre los que ya llegaron. Los empates se resuelven por llegada y, si esta también coincide, por orden de entrada. Si no hay pedidos listos, el reloj avanza a la siguiente llegada. Una secuencia continua de pedidos cortos podría postergar a uno largo.

## Fase 3. Round Robin y Prioridad

`round_robin.py` usa una cola FIFO y un quantum configurable; para los resultados de referencia se usa `q=4`. Cada turno ejecuta hasta cuatro unidades o hasta terminar el pedido. Las nuevas llegadas entran a la cola antes de reinsertar al pedido interrumpido. Si la cola queda vacía, el reloj avanza a la próxima llegada. El código rechaza un quantum no positivo.

`prioridad.py` elige, entre los pedidos ya llegados, el de menor número de prioridad y lo ejecuta completo. Desempata por llegada y orden de entrada. Una llegada continua de pedidos de mayor prioridad puede causar inanición; el envejecimiento sería una forma de mitigarlo, pero no forma parte de esta implementación.

Los cuatro algoritmos devuelven pedidos resueltos y una lista de tramos `(id, inicio, fin)`. Los tramos permiten mostrar el orden real de atención y el Gantt; en Round Robin un pedido puede ocupar varios tramos.

## Fase 4. Métricas, integración y evidencia

`metricas.py` calcula espera = finalización − llegada − duración y respuesta = primera atención − llegada. El retorno es finalización − llegada. En FCFS, SJF y Prioridad la espera y la respuesta coinciden; en Round Robin pueden diferir porque el pedido vuelve a la cola. Los promedios se calculan sobre todos los pedidos.

El enunciado original llama «respuesta» a finalización − llegada, pero ese cálculo es el retorno y no reproduce el valor de referencia de Round Robin. Por eso el simulador usa las definiciones anteriores. Esta discrepancia debe explicarse en el informe académico.

`main.py` ejecuta los cuatro algoritmos sobre ambos conjuntos. Imprime las métricas individuales, un Gantt esquemático y la tabla comparativa. Para el conjunto de referencia compara los promedios con los valores esperados y detiene la ejecución si hay una diferencia.

Las capturas de la ejecución están en `outputs/`: `01_referencia_fcfs_sjf.png`, `02_referencia_rr_prioridad.png`, `03_segundo_conjunto_fcfs_sjf.png` y `04_segundo_conjunto_rr_prioridad.png`. Las dos primeras muestran las verificaciones del conjunto de referencia; las otras dos muestran el conjunto propuesto por el equipo.

# 4. Resultados

Las capturas registran estos promedios, en unidades de tiempo:

| Conjunto | Algoritmo | Espera | Respuesta |
|---|---|---:|---:|
| Referencia | FCFS | 5.75 | 5.75 |
| Referencia | SJF | 5.25 | 5.25 |
| Referencia | Round Robin (q=4) | 9.25 | 4.00 |
| Referencia | Prioridad | 7.75 | 7.75 |
| Segundo | FCFS | 4.40 | 4.40 |
| Segundo | SJF | 2.40 | 2.40 |
| Segundo | Round Robin (q=4) | 4.60 | 3.60 |
| Segundo | Prioridad | 2.60 | 2.60 |

En ambos conjuntos, SJF consigue la menor espera promedio: 5.25 y 2.40. Si el objetivo es reducir el tiempo máximo hasta la primera atención, Round Robin ofrece el mejor resultado entre estos cuatro algoritmos: 8 unidades en el conjunto de referencia y 6 en el segundo. Esto permite recomendar SJF para minimizar la espera promedio y Round Robin para limitar cuánto tarda en comenzar la atención del pedido que más espera.
