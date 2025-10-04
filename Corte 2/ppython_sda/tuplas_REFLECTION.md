# Reflexión sobre uso de tuplas

Resumen breve sobre cuándo usar tuplas frente a alternativas (listas, namedtuple, dataclass):

- Inmutabilidad: usa `tuple` cuando necesites una colección inmutable (constantes, claves de diccionario).
- Rendimiento: crear y recorrer tuplas suele ser ligeramente más rápido y con menor overhead que listas en lecturas; sin embargo, listas son mejores cuando se requieren modificaciones frecuentes.
- Semántica: para un registro fijo de campos (por ejemplo coordenadas), `tuple` o `namedtuple` son apropiados; para colecciones dinámicas usa `list`.

Resultados empíricos (resumen esperado)

- Crear tuples: O(n) en tamaño n; instancia ligeramente más rápida que construir listas en algunos casos.
- Sum: O(n) al iterar todos los elementos.
- Concatenación (a + b): O(len(a)+len(b)) con copia completa; puede ser costosa si se realiza repetidamente.
- Conversión a lista: O(n) y útil cuando se necesita mutabilidad.

Notas sobre el experimento

- Recomendé medir con `benchmarks/bench_tuplas.py` para ver tiempos concretos en tu máquina.
- El script realiza mediciones para tamaños n = 10, 100, 1000, 5000. Ajusta `sizes` para explorar otros puntos.
