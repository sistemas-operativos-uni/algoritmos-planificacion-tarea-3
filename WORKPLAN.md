# WORKPLAN — Algoritmos de Planificación (Torre de Control)
 
## Fases y bloqueos
 
| Fase | Bloquea a | Responsable |
|---|---|---|
| 1. Diseño del modelo de datos | Todo lo demás | Renato |
| 2. FCFS + SJF | Fase 4 (Métricas y verificación) | Dev FCFS/SJF -> Gabriel |
| 3. Round Robin + Prioridad | Fase 4 (Métricas y verificación) | Dev RR/Prioridad -> Kike + Renato |
| 4. Métricas y verificación | Fase 5 (Informe), y retroalimenta a Fases 2/3 si algo no cuadra | Analista de resultados -> Adán|
| 5. Informe + recomendación + sustentación | — | Renato |
 
Fases 2 y 3 corren **en paralelo**, sin dependencia entre sí. Fase 4 no puede iniciar hasta que ambas fases 2 y 3 estén cerradas. A diferencia de un flujo lineal, la Fase 4 puede **devolver trabajo a Fase 2 o 3**: si un algoritmo no reproduce los valores de referencia, no se avanza a Fase 5 hasta corregirlo.
 
---
 
## Tareas por integrante
 
### Coordinador(a) -> Renato
- [ ] Convocar reunión de diseño (Fase 1): definir estructura de datos del pedido (clase, diccionario o struct) y cerrar el diseño de `modelo_pedido.py`.
- [ ] Crear repo, estructura de carpetas, README.md.
- [ ] Dar seguimiento al avance de Dev FCFS/SJF y Dev RR/Prioridad.
- [ ] Integrar todas las secciones del informe final, incluyendo la recomendación de negocio del Paso 5.
- [ ] Coordinar fecha y armado de la sustentación (5-8 min), demostrando en vivo los cuatro algoritmos.
- **Bloqueado por:** nada al inicio. Su tarea de integración (informe) está bloqueada por el cierre de Fase 4.
### Dev FCFS/SJF -> Gabriel
- [ ] Implementar `algoritmos/fcfs.py`: ordena por tiempo de llegada, calcula orden de atención.
- [ ] Implementar `algoritmos/sjf.py`: entre los pedidos ya llegados, elige el de menor duración.
- [ ] Validar con el conjunto de referencia: FCFS debe dar espera promedio = 5.75; SJF debe dar 5.25.
- [ ] Documentar en el informe qué hace cada parte del código (no solo pegar el código).
- **Bloqueado por:** Fase 1 (estructura de datos definida). **Bloquea a:** Analista (Fase 4).
### Dev RR/Prioridad -> Kike + Renato
- [ ] Implementar `algoritmos/round_robin.py` con quantum configurable (usar quantum = 4 para el conjunto de referencia).
- [ ] Implementar `algoritmos/prioridad.py` no expropiativo (menor número de prioridad = mayor prioridad).
- [ ] Validar con el conjunto de referencia: Round Robin debe dar espera promedio = 9.25 y respuesta promedio = 4.0; Prioridad debe dar espera promedio = 7.75.
- [ ] Documentar en el informe qué hace cada parte del código.
- **Bloqueado por:** Fase 1 (estructura de datos definida). **Bloquea a:** Analista (Fase 4).
### Analista de resultados -> Adán
- [ ] Implementar `metricas.py`: cálculo de tiempo de espera (inicio − llegada) y tiempo de respuesta (fin − llegada) por pedido y promedio, para los cuatro algoritmos.
- [ ] Verificar los cuatro algoritmos contra los valores de referencia; si alguno no cuadra, devolver observación al desarrollador correspondiente (Fase 2 o 3).
- [ ] Armar la tabla comparativa única con los cuatro algoritmos para el informe.
- [ ] Proponer y probar un segundo conjunto de pedidos (definido por el equipo) y verificar si la recomendación se mantiene.
- [ ] Preparar el diagrama de Gantt de cada algoritmo para el informe.
- **Bloqueado por:** cierre de Fase 2 y Fase 3. **Bloquea a:** Coordinador (informe, Fase 5).
---
 
## Checklist de entrega final -> Renato
- [ ] Código fuente del simulador (los cuatro algoritmos) en el repo.
- [ ] Estructura de datos documentada (Paso 1).
- [ ] Diagrama de Gantt de cada algoritmo en `docs/diseno/`.
- [ ] Capturas de pantalla del simulador con ambos conjuntos de pedidos en `docs/capturas/`.
- [ ] Tabla comparativa de los cuatro algoritmos (espera y respuesta promedio).
- [ ] Recomendación final justificada con los números obtenidos, no solo con teoría.
- [ ] Informe PDF en `informe/`.
- [ ] Ensayo de sustentación: TODOS explican inanición, envejecimiento (aging) y efecto convoy.
 
