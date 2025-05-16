# Proyecto: Detección de anomalías en tiempo real con River
=====================================================

## Descripción general:
--------------------
Este proyecto implementa un sistema de monitoreo de métricas de red (por ejemplo, latencia, jitter, throughput) y detecta desviaciones inusuales al vuelo usando ML online con la librería River.

### Objetivos:
- Ingesta de métricas de red en tiempo real (p.ej. resultados de ping continuo).
- Extracción/normalización de features sencillas (media móvil, varianza, etc.).
- Modelo de detección de anomalías incremental (p.ej. Isolation Forest online, LOF, o estadístico Z-score adaptativo).
- Alerta inmediata cuando el modelo detecta un dato fuera de lo esperado.
- Registro y visualización opcional de eventos anómalos.

### Componentes principales:
1. DataPipeline: clase que conecta al orquestador de datos y obtiene métricas.
2. FeatureExtractor: calcula features en streaming (media, varianza, z-score, etc.)
3. AnomalyDetector: wrapper de River para un modelo on-line de detección.
4. AlertHandler: módulo que recibe eventos anotados como anomalías y ejecuta acciones (log, envío de notificación).
5. Runner: script que combina todos los componentes en un bucle infinito.

## Dependencias:
-------------
- river (pip install river)
- pythonping (pip install pythonping)  # Para simular latencia de red
- schedule                  # Para ejecutar tareas periódicas


