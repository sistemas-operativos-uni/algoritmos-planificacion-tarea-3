# PROJECT.md — Torre de Control: Simulador de Algoritmos de Planificación
 
## 1. Información académica
 
| Campo | Detalle |
|---|---|
| Curso | Sistemas Operativos (SW407) |
| Escuela | Ingeniería de Software — Facultad de Ingeniería Industrial y de Sistemas |
| Universidad | Universidad Nacional de Ingeniería (UNI) |
| Docente | Mg. Ing. José Carlos García La Riva |
| Ciclo | 2026-II |
| Práctica | Práctica Dirigida N.º 04, Semana 4 |
| Tema | Planificación de Procesos |
| Modalidad | Grupal, equipos de 3 a 4 integrantes |
| Duración | 1 semana de trabajo autónomo más sustentación en clase |
| Entorno requerido | Máquina virtual Linux con Python 3 (y gcc, si se opta por C) |
| Nombre del repositorio | algoritmos-planificacion-tarea-3 |
 
## 2. Propósito de la práctica
 
Al finalizar el equipo debe estar en condiciones de:
 
- Implementar los algoritmos de planificación FCFS, SJF, Round Robin y por Prioridad.
- Calcular el tiempo de espera y el tiempo de respuesta de cada proceso, individual y en promedio.
- Comparar cuantitativamente los cuatro algoritmos sobre un mismo conjunto de procesos.
- Argumentar, con base en los resultados, en qué escenario conviene aplicar cada algoritmo.
## 3. El caso: CocinaPerú Express — Torre de Control
 
Tras el sistema de pedidos concurrentes (Tarea 2), la gerencia de CocinaPerú Express quiere decidir, con datos, qué política de atención conviene aplicar en cada sucursal. El equipo debe construir un simulador que reciba una lista de pedidos y calcule cómo los atendería cada uno de los cuatro algoritmos vistos en clase.
 
El simulador recibe, para cada pedido: tiempo de llegada, duración de preparación y nivel de prioridad. Calcula, para cada algoritmo, el orden de atención, el tiempo de espera de cada pedido y el tiempo de espera promedio del conjunto.
 
La gerencia pide además una recomendación final: dado un objetivo de negocio (por ejemplo, minimizar la espera promedio, o que ningún cliente espere demasiado antes de ser atendido), el equipo debe indicar cuál algoritmo conviene aplicar y por qué.
 
## 4. Alcance técnico del sistema
 
### Modelo de datos (Paso 1)
 
Cada pedido se representa con: identificador, tiempo de llegada, duración y prioridad. El equipo elige la estructura (clase, diccionario o struct) y la documenta en el informe.
 
### FCFS (First Come, First Served)
 
- No expropiativo.
- Ordena los pedidos estrictamente por tiempo de llegada.
- Valor de referencia a reproducir: espera promedio = 5.75.
### SJF (Shortest Job First)
 
- No expropiativo.
- Entre los pedidos ya llegados, elige siempre el de menor duración.
- Valor de referencia a reproducir: espera promedio = 5.25.
### Round Robin
 
- Expropiativo, con quantum configurable.
- Quantum usado para comparar con la clase: 4.
- Cada pedido recibe turnos sucesivos de duración igual al quantum hasta completarse; si llegan nuevos pedidos durante la ejecución, se encolan según su tiempo de llegada.
- Valores de referencia a reproducir: espera promedio = 9.25, respuesta promedio = 4.0.
### Prioridad
 
- No expropiativo.
- Menor número de prioridad implica mayor prioridad de atención.
- Valor de referencia a reproducir: espera promedio = 7.75.
### Cálculo de métricas
 
- Tiempo de espera = tiempo de inicio de atención menos tiempo de llegada.
- Tiempo de respuesta = tiempo de finalización menos tiempo de llegada.
- En algoritmos no expropiativos (FCFS, SJF, Prioridad), espera y respuesta coinciden. En Round Robin, no, porque un pedido puede ser interrumpido y retomado.
- Los resultados de los cuatro algoritmos se presentan en una sola tabla comparativa.
### Conjunto de referencia
 
| Pedido | Llegada | Duración | Prioridad |
|---|---|---|---|
| P1 | 0 | 5 | 3 |
| P2 | 1 | 3 | 4 |
| P3 | 2 | 8 | 1 |
| P4 | 3 | 6 | 2 |
 
El equipo debe además proponer un segundo conjunto de pedidos propio y verificar si la recomendación final se mantiene con ese conjunto.
 
## 5. Conceptos clave involucrados
 
| Concepto | Resumen |
|---|---|
| Planificación de CPU (scheduling) | Política que decide qué proceso listo se ejecuta a continuación. |
| No expropiativo (non-preemptive) | Una vez que un proceso empieza a ejecutarse, no se interrumpe hasta terminar (FCFS, SJF, Prioridad). |
| Expropiativo (preemptive) | El proceso en ejecución puede ser interrumpido antes de terminar (Round Robin). |
| Quantum | Porción fija de tiempo de CPU asignada a cada proceso en Round Robin antes de pasar al siguiente. |
| Tiempo de espera | Tiempo que un pedido pasa listo, esperando ser atendido por primera vez. |
| Tiempo de respuesta | Tiempo total desde que el pedido llega hasta que termina de atenderse. |
| Inanición (starvation) | Un proceso nunca llega a ser atendido porque siempre hay otros de mayor prioridad; riesgo característico del algoritmo por Prioridad. |
| Envejecimiento (aging) | Técnica que incrementa gradualmente la prioridad de un proceso que ha esperado mucho, para evitar inanición. |
| Efecto convoy | En FCFS, procesos cortos quedan atascados detrás de un proceso largo, incrementando la espera promedio del conjunto. |
 
## 6. Estructura del repositorio
 
```
algoritmos-planificacion-tarea-3/
├── simulador/
│   ├── algoritmos/
│   │   ├── fcfs.py
│   │   ├── sjf.py
│   │   ├── round_robin.py
│   │   └── prioridad.py
│   ├── modelo_pedido.py       (estructura de datos, Paso 1)
│   ├── metricas.py            (cálculo de espera/respuesta y promedios)
│   ├── main.py                (corre los 4 algoritmos y muestra la tabla)
│   └── datos_referencia.py    (conjunto de referencia y conjunto propio del equipo)
├── docs/
│   ├── diseno/                (estructura de datos, diagramas de Gantt)
│   └── capturas/
├── informe/
├── README.md
├── WORKPLAN.md
├── PROJECT.md
└── .gitignore
```
 
## 7. Flujo de trabajo (workflow)
 
```
Fase 1: Diseño del modelo de datos (todo el equipo)
   │
   ├──► Fase 2: FCFS + SJF (Dev FCFS/SJF)         ──┐
   │                                                 │
   └──► Fase 3: Round Robin + Prioridad (Dev RR/Pr) ─┼──► Fase 4: Métricas y verificación (Analista)
                                                       │           │
                                                       │           ▼
                                                       └──► Fase 5: Informe, recomendación y sustentación (Coordinador)
```
 
Reglas de dependencia:
 
- La Fase 1 bloquea a todas las demás; nada se implementa sin la estructura de datos definida.
- Las Fases 2 y 3 son independientes entre sí y se ejecutan en paralelo.
- La Fase 4 no puede iniciar hasta que ambas Fases 2 y 3 estén cerradas.
- A diferencia de un flujo estrictamente lineal, la Fase 4 puede devolver trabajo a la Fase 2 o 3 si un algoritmo no reproduce los valores de referencia; no se avanza a la Fase 5 hasta que los cuatro algoritmos estén verificados.
- La Fase 5 depende del cierre de la Fase 4.
## 8. Roles del equipo
 
| Rol | Responsabilidad principal |
|---|---|
| Coordinador(a) | Organiza al equipo, integra las partes del informe, coordina entrega y sustentación. |
| Desarrollador(a) FCFS/SJF | Implementa los algoritmos no expropiativos por orden de llegada y por duración. |
| Desarrollador(a) RR/Prioridad | Implementa Round Robin (con quantum configurable) y el algoritmo por prioridad. |
| Analista de resultados | Calcula las métricas, arma la tabla comparativa y verifica los resultados contra los valores de referencia. |
 
Un mismo integrante puede asumir más de un rol si el equipo tiene 3 personas. El detalle de tareas por integrante, con sus bloqueos específicos, está en `WORKPLAN.md`.
 
## 9. Entregables
 
- Código fuente del simulador (Python), organizado en el repositorio del equipo.
- Estructura de datos documentada (Paso 1).
- Informe escrito en PDF, que incluye: portada, descripción del caso, estructura de datos, explicación del código de cada algoritmo, tabla comparativa de los cuatro algoritmos con espera y respuesta promedio, capturas de pantalla de la ejecución con ambos conjuntos de pedidos, y la recomendación final justificada.
- Capturas de pantalla de la ejecución del simulador con ambos conjuntos de pedidos.
- Sustentación grupal en clase, de 5 a 8 minutos, demostrando en vivo los cuatro algoritmos sobre el conjunto de referencia.
## 10. Criterios de evaluación (20 puntos, grupal)
 
| Criterio | Puntaje |
|---|---|
| Comprensión conceptual del caso | 3 pts |
| Implementación de FCFS y SJF | 4 pts |
| Implementación de Round Robin y Prioridad | 4 pts |
| Cálculo de métricas y verificación | 3 pts |
| Documentación e informe escrito | 3 pts |
| Sustentación grupal | 3 pts |
 
Nota sobre la sustentación: todos los integrantes deben poder explicar cualquier parte del trabajo, no solo la de su rol asignado. Se debe preparar respuestas sobre inanición, envejecimiento (aging) y efecto convoy.
 
El docente puede aplicar un factor de coevaluación entre pares para ajustar la nota individual según la participación real en el equipo.
 
## 11. Entorno de desarrollo
 
- El setup inicial del repositorio (estructura de carpetas, README, WORKPLAN, PROJECT, .gitignore, git init) no requiere máquina virtual y puede hacerse directamente en Windows.
- El simulador es Python puro, por lo que también puede escribirse y probarse en Windows sin problema.
- La toma de capturas de pantalla debe realizarse desde la máquina virtual Linux, por consistencia con el entorno exigido por el docente.
- Herramienta requerida en la VM: Python 3.
## 12. Referencias del curso
 
- Silberschatz, A., Galvin, P. B., y Gagne, G. (2018). *Operating System Concepts* (10th ed.). Wiley — Capítulo 5 (CPU Scheduling).
- Tanenbaum, A. S., y Bos, H. (2015). *Modern Operating Systems* (4th ed.). Pearson.
- Stallings, W. (2018). *Operating Systems: Internals and Design Principles* (9th ed.). Pearson.
- The Linux Kernel documentation (2026). CFS Scheduler, kernel.org.
- Universidad Nacional de Ingeniería (2026). Sílabo SW407 — Sistemas Operativos, Escuela de Ingeniería de Software.