# Reflexión sobre comprensión de listas

Resumen y recomendaciones:

- Las list comprehensions en Python son expresivas y, para muchas operaciones, tan rápidas o más que loops explícitos.
- En las mediciones locales, las comprehensions muestran ventaja en algunos tamaños; para n grandes la diferencia puede depender de la operación y del overhead del entorno.
- Operaciones como `flatten` pueden ser más costosas si se aplican repetidamente sobre estructuras grandes; preferir diseños que minimicen copias innecesarias.

Usos reales:
- Transformaciones en pipelines de datos pequeños/medianos: comprehensions o map+filter.
- En código crítico en tiempo, medir y considerar implementaciones basadas en numpy o C si es necesario.
