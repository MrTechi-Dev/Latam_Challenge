# Latam_Challenge

# Medición de Tiempo y Memoria en Python

Este proyecto Python muestra cómo medir el tiempo de ejecución y la memoria utilizada en diferentes funciones utilizando las bibliotecas `time` y `memory-profiler`. El código incluye ejemplos de funciones que procesan datos de tweets y realizan cálculos para encontrar las mejores fechas, emojis más utilizados y usuarios más mencionados.

## Requisitos

Asegúrate de tener las siguientes bibliotecas instaladas:

- `memory-profiler`: Para medir el uso de memoria.
- `collections`: Para contar elementos y trabajar con diccionarios.
- `datetime`: Para el manejo de fechas y horas.
- `typing`: Para proporcionar sugerencias de tipos en funciones.
- `time`: Para medir el tiempo de ejecución.
- `heapq`: Para realizar operaciones de montón.
- `json`: Para trabajar con archivos JSON.

Puedes instalar `memory-profiler` utilizando pip:

```bash
pip install memory-profiler

Uso

El proyecto incluye varias funciones, cada una con su propia documentación y perfilado. Aquí hay un resumen de las funciones principales:
q1_time(file_path: str)

Esta función devuelve las 10 mejores fechas donde hubo más tweets, optimizando el tiempo de ejecución.
q1_memory(file_path: str)

Esta función devuelve las 10 mejores fechas donde hubo más tweets, optimizando la memoria utilizando la biblioteca heapq.
q2_time(file_path: str)

Esta función devuelve los 10 emojis más utilizados, optimizando el tiempo de ejecución.
q2_memory(file_path: str)

Esta función devuelve los 10 emojis más utilizados, optimizando la memoria utilizando la biblioteca heapq.
q3_time(file_path: str)

Esta función devuelve los 10 usuarios más mencionados, optimizando el tiempo de ejecución.
q3_memory(file_path: str)

Esta función devuelve los 10 usuarios más mencionados, optimizando la memoria utilizando la biblioteca heapq.
Ejecución

Para ejecutar el código y medir el tiempo y la memoria, puedes utilizar las funciones proporcionadas en los ejemplos de uso al final del script. Asegúrate de proporcionar la ruta correcta al archivo JSON de tweets en file_pat

```python
top_dates_time = q1_time("/ruta/al/archivo.json")
print("Top 10 Fechas (Tiempo):", top_dates_time)

top_dates_memory = q1_memory("/ruta/al/archivo.json")
print("Top 10 Fechas (Memoria):", top_dates_memory)
```
### Repite el proceso para las otras funciones


# pylint score: 
```
Your code has been rated at 9.42/10 
```