UNIVERSIDAD NACIONAL DE
INGENIERÍA Escuela de
Ingeniería de Software
PRÁCTICA DIRIGIDA N.º 04* · SEMANA 4
Planificación de Procesos: Simulador de Algoritmos de
Atención
Curso Sistemas Operativos (SW407)
Escuela Ingeniería de Software — Facultad de Ingeniería Industrial y de
Sistemas, UNI
Tema Semana 4 — Planificación de Procesos
Docente Mg. Ing. José Carlos, García La Riva
Ciclo / Semestre 2026-II*
Modalidad Grupal — equipos de 3 a 4 integrantes
Duración estimada 1 semana de trabajo autónomo + sustentación en clase*
Entorno requerido Máquina virtual Linux (ver Taller de VirtualBox) con gcc y/o Python 3
instalados
* Dato asumido para fines de plantilla — verificar y ajustar antes de la publicación oficial.
I. PROPÓSITO DE LA PRÁCTICA
Al finalizar esta práctica dirigida, el equipo estará en condiciones de:
● Implementar los algoritmos de planificación FCFS, SJF, Round Robin y por Prioridad.
● Calcular el tiempo de espera y el tiempo de respuesta de cada proceso, individual y en
promedio. ● Comparar cuantitativamente los cuatro algoritmos sobre un mismo conjunto de
procesos. ● Argumentar, con base en los resultados, en qué escenario conviene aplicar cada
algoritmo.
II. EL CASO: "COCINAPERÚ EXPRESS — TORRE DE CONTROL"

Tras el éxito del sistema de pedidos concurrentes, la gerencia de CocinaPerú Express
quiere decidir, con datos, qué política de atención conviene aplicar en cada sucursal.
Te encargan construir un simulador —la "Torre de Control"— que permita cargar una
lista de pedidos y calcular cómo los atendería cada uno de los algoritmos vistos en
clase.
El simulador debe recibir, para cada pedido, su tiempo de llegada, su duración de
preparación y su nivel de prioridad, y debe calcular, para cada uno de los cuatro
algoritmos (FCFS, SJF, Round Robin y Prioridad), el orden de atención, el tiempo de
espera de cada pedido y el tiempo de espera promedio del conjunto.
La gerencia pide además una recomendación final: dado un objetivo de negocio (por
ejemplo, "minimizar la espera promedio" o "que ningún cliente espere demasiado antes
de ser atendido"), el equipo debe indicar cuál de los cuatro algoritmos conviene aplicar
y por qué.
III. CONFORMACIÓN DEL EQUIPO Y ROLES
Formen equipos de 3 a 4 integrantes y asignen los siguientes roles. Un mismo integrante puede asumir
más de un rol si el equipo tiene 3 personas.
SW407 — Sistemas Operativos — Práctica Dirigida Página 1 de 5
UNIVERSIDAD NACIONAL DE INGENIERÍA
Escuela de Ingeniería de Software
Rol Responsabilidad principal
Coordinador(a) Organiza al equipo, integra las partes del informe y coordina la
entrega y la sustentación.
Desarrollador(a) Implementa los algoritmos no expropiativos por orden de llegada y por
FCFS/SJF duración.
Desarrollador(a) Implementa Round Robin (con quantum configurable) y el algoritmo por
RR/Prioridad prioridad.
Analista de Calcula las métricas, arma la tabla comparativa y verifica los resultados
resultados contra los valores de referencia.
IV. PASOS DE IMPLEMENTACIÓN
Paso 1. Diseñar el modelo de datos
Definan cómo representarán cada pedido (proceso) en su programa: identificador, tiempo de llegada,
duración y prioridad. Usen el conjunto de referencia de la Semana 4 para probar su simulador.
● Pedidos de referencia: P1 (llegada 0, duración 5, prioridad 3), P2 (llegada 1, duración 3, prioridad 4), P3
(llegada 2, duración 8, prioridad 1) y P4 (llegada 3, duración 6, prioridad 2).
● Entregable de este paso: la estructura de datos elegida (clase, diccionario o struct) documentada en el informe.
Paso 2. Implementar FCFS y SJF
Implementen ambos algoritmos no expropiativos: FCFS ordena por tiempo de llegada; SJF elige, entre los

pedidos ya llegados, el de menor duración.
● Verifiquen que su implementación de FCFS reproduzca una espera promedio de 5.75 con el conjunto de
referencia. ● Verifiquen que su implementación de SJF reproduzca una espera promedio de 5.25 con el
conjunto de referencia.
Paso 3. Implementar Round Robin y Prioridad
Implementen Round Robin con un quantum configurable (usen quantum = 4 para comparar con la
clase) y el algoritmo por prioridad no expropiativo (menor número de prioridad = mayor prioridad).
● Verifiquen que su Round Robin (quantum = 4) reproduzca una espera promedio de 9.25 y una respuesta
promedio de 4.0 con el conjunto de referencia.
● Verifiquen que su algoritmo de Prioridad reproduzca una espera promedio de 7.75 con el conjunto de
referencia.
# Fragmento de referencia — round_robin.py
def round_robin(pedidos, quantum):
restante = {p: d["duracion"] for p, d in pedidos.items()}
llegada = {p: d["llegada"] for p, d in pedidos.items()}
cola, t, fin = [], 0, {}
pendientes = sorted(pedidos, key=lambda p: llegada[p])
def encolar_llegadas(hasta):
while pendientes and llegada[pendientes[0]] <= hasta:
cola.append(pendientes.pop(0))
encolar_llegadas(0)
while cola:
p = cola.pop(0)
corre = min(quantum, restante[p])
SW407 — Sistemas Operativos — Práctica Dirigida Página 2 de 5
UNIVERSIDAD NACIONAL DE INGENIERÍA
Escuela de Ingeniería de Software
t += corre
restante[p] -= corre
encolar_llegadas(t)
if restante[p] > 0:
cola.append(p)
else:
fin[p] = t
return fin
Paso 4. Calcular tiempo de espera y de respuesta
Para cada algoritmo, calculen el tiempo de espera y el tiempo de respuesta de cada pedido, y sus
promedios. Recuerden que, en algoritmos no expropiativos, ambos tiempos coinciden; en Round
Robin, no.
● Tiempo de espera = tiempo de inicio de atención − tiempo de llegada.
● Tiempo de respuesta = tiempo de finalización − tiempo de llegada.
● Presenten los resultados de los cuatro algoritmos en una sola tabla para facilitar la comparación.
Paso 5. Comparar y recomendar
Con la tabla de resultados, respondan la pregunta de negocio planteada en el caso: ¿qué algoritmo
recomendarían si el objetivo es minimizar la espera promedio? ¿Y si el objetivo es que ningún cliente

espere mucho antes de ser atendido por primera vez?
● Sustenten la recomendación con los números obtenidos, no solo con la teoría.
● Prueben su simulador con un segundo conjunto de pedidos propuesto por el equipo y
verifiquen si la recomendación se mantiene.
Paso 6. Documentar los resultados
Redacten un informe grupal que integre el simulador y sus resultados.
● Portada, descripción del caso y la estructura de datos del Paso 1.
● Explicación del código de cada algoritmo (qué hace cada parte, no solo pegar el código).
● Tabla comparativa de los cuatro algoritmos, con espera y respuesta promedio.
● Capturas de pantalla de la ejecución del simulador con ambos conjuntos de pedidos.
● La recomendación final del Paso 5, con su justificación.
Paso 7. Preparar la sustentación grupal
Cada equipo presentará su simulador en clase (5 a 8 minutos), demostrando en vivo los cuatro
algoritmos sobre el conjunto de referencia.
● Todos los integrantes deben poder explicar cualquier parte del trabajo, no solo la de su rol
asignado. ● Preparen respuestas para preguntas sobre inanición, envejecimiento (aging) y el
efecto convoy.
SW407 — Sistemas Operativos — Práctica Dirigida Página 3 de 5
UNIVERSIDAD NACIONAL DE
INGENIERÍA Escuela de
Ingeniería de Software
V. ENTREGABLES
● Código fuente del simulador (Python o C), organizado en la carpeta o repositorio del
equipo. ● Informe escrito en PDF, según lo indicado en el Paso 6.
● Capturas de pantalla de la ejecución del simulador con ambos conjuntos de pedidos.
● Sustentación grupal en la fecha indicada por el docente.*
VI. RÚBRICA DE EVALUACIÓN
La práctica se califica sobre 20 puntos, aplicados de forma grupal según los siguientes criterios.
Criterio Ptje. Excelente Bueno Regular Deficiente
Comprensión 3 pts Traduce con Traduce Aplica los No logra traducir el
conceptual del precisión el caso correctamente el conceptos de caso a un
a un modelo de caso, con alguna forma parcial o modelo de
caso
procesos justificación con planificación
(llegada, incompleta. confusiones coherente.
duración, entre los

|     | prioridad)  | y     | algoritmos.  |     |
| --- | ----------- | ----- | ------------ | --- |
|     | justifica   | cada  |              |     |
|     | decisión    |   de  |              |     |
diseño.
Implementació 4 pts  Ambos algoritmos    Ambos funcionan  Solo uno de los  Ninguno de los dos
| n de  FCFS y  | funcionan          | con  detalles     | dos             | algoritmos        |
| ------------- | ------------------ | ----------------- | --------------- | ----------------- |
|               | correctamente y    | menores (p. ej.   | algoritmos      | funciona o  el    |
| SJF           | reproducen los     | pequeñas          | funciona        | código no         |
|               | tiempos de         | diferencias  de   | correctamente.  | compila/ejecuta.  |
|               | espera de          | redondeo).        |                 |                   |
referencia sin
errores.
Implementació 4 pts  Ambos algoritmos    Ambos funcionan  Solo uno de los  Ninguno de los dos
|     | funcionan    | con  detalles  | dos    | algoritmos  |
| --- | ------------ | -------------- | ------ | ----------- |
n de  Round
|     | correctamente,    | menores en la   | algoritmos  | funciona o  el  |
| --- | ----------------- | --------------- | ----------- | --------------- |
Robin y
|     | incluyendo el  | gestión de la cola  | funciona   | código no    |
| --- | -------------- | ------------------- | ---------- | ------------ |
Prioridad  manejo  del  o el  quantum.  correctamente.  compila/ejecuta.
quantum y el
orden  por
prioridad.
Cálculo de  3 pts  Calcula  Calcula  Calcula las  No presenta
|     | correctamente   | correctamente   | métricas de   | cálculo de   |
| --- | --------------- | --------------- | ------------- | ------------ |
métricas y
|     | tiempo de espera  | las métricas con  | forma incompleta  | métricas o los    |
| --- | ----------------- | ----------------- | ----------------- | ----------------- |
verificación
|     | y de  respuesta  | alguna  diferencia  | o  solo para  | resultados no    |
| --- | ---------------- | ------------------- | ------------- | ---------------- |
|     | (individual      | y   menor           | algunos       | corresponden al  |
|     | promedio)        | para                |               | caso.            |
|     |                  | frente a la         | algoritmos.   |                  |
|     | los              | referencia.         |               |                  |
cuatro algoritmos,
verificados
contra los
valores de
referencia.
Documentación e    3 pts  Informe  Informe completo  Informe  No presenta
informe escrito   completo y   con  alguna  incompleto o   informe o  el
|     | claro:               | sección poco   | con secciones  | contenido no    |
| --- | -------------------- | -------------- | -------------- | --------------- |
|     | diagrama de          | desarrollada.  | clave          | corresponde al  |
|     | Gantt de cada        |                | ausentes       | trabajo         |
|     | algoritmo, código    |                | (diagramas,    | realizado.      |
|     | explicado, tabla     |                | evidencia o    |                 |
|     | comparativa y        |                | explicación).  |                 |
capturas  de
evidencia.
Sustentación  3 pts  Todo el equipo  El equipo explica    La sustentación es    El equipo no puede
|     | domina  el tema,  | correctamente el    | superficial o solo  | sustentar su propio    |
| --- | ----------------- | ------------------- | ------------------- | ---------------------- |
grupal
|     | justifica en    | trabajo, con     | uno  o    dos      | trabajo.  |
| --- | --------------- | ---------------- | ------------------ | --------- |
|     | qué escenario   | participación    | integrantes        |           |
|     | usarían  cada   | desigual  entre  | pueden   explicar  |           |
|     | algoritmo y     | integrantes.     | el trabajo.        |           |
responde con
seguridad las
preguntas del
docente.

Puntaje total: 20 puntos. El puntaje obtenido se integra a la nota de Prácticas (PP) del curso, según la
fórmula de  evaluación vigente.*
* El docente puede aplicar un factor de evaluación individual (coevaluación entre pares) para ajustar la nota final de cada
integrante  según su participación real en el equipo.
SW407 — Sistemas Operativos — Práctica Dirigida Página 4 de 5
UNIVERSIDAD NACIONAL DE
INGENIERÍA Escuela de

Ingeniería de Software
VII. REFERENCIAS
Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts (10th ed.). Wiley —
Capítulo 5 (CPU Scheduling).
Tanenbaum, A. S., & Bos, H. (2015). Modern Operating Systems (4th ed.). Pearson.
Stallings, W. (2018). Operating Systems: Internals and Design Principles (9th ed.). Pearson. The Linux
Kernel documentation (2026). CFS Scheduler. kernel.org/doc/html/latest/scheduler/sched-design-CFS.html
Universidad Nacional de Ingeniería (2026). Sílabo SW407 — Sistemas Operativos, Escuela de Ingeniería
de Software.

SW407 — Sistemas Operativos — Práctica Dirigida Página 5 de 5