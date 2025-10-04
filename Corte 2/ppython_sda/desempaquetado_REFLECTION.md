# Reflexión sobre desempaquetado

Resumen rápido sobre cuándo usar desempaquetado por posición, `*rest` y conversiones a namedtuple:

- Desempaquetado posicional (id, desc, price) es claro y conciso cuando la estructura tiene tamaño conocido y fijo.
- `*rest` (star-unpacking) es práctico para separar extremos y trabajar con el bloque central sin copiar manualmente índices.
- La conversión a `namedtuple` mejora la legibilidad cuando se necesitan campos con nombre, pero conlleva coste de creación (ver benchmark).

Resultados empíricos

- Index+slicing es ligeramente más rápido que star-unpacking en las pruebas (ver `benchmarks/bench_desemp.py`).
- La conversión a namedtuple es significativamente más costosa (creación de tipos dinámicos y llamada), por lo que conviene usarla cuando la claridad del código lo justifica, no en bucles ajustados.

Recomendaciones

- Para acceso rápido en código crítico, usar index/slice si el tamaño es conocido.
- Para código expresivo y mantenible, `*rest` o `namedtuple` son buenos, con la consideración de coste cuando n es grande o la operación se repite mucho.
