# Reflexión sobre uso de `set` para suscriptores

Resumen:

- `set` ofrece búsquedas O(1) promedio para membership — ideal para verificar si un correo ya está suscrito.
- Listas requieren búsqueda O(n) y degradan con el tamaño; los benchmarks lo muestran claramente.
- Para operaciones que requieren orden o índices, preferir `list` o estructuras auxiliares.

Caso límite implementado:
- `safe_add_with_limit` lanza `OverflowError` si al añadir se supera una capacidad máxima: útil para sistemas con cuotas.

Recomendación:
- Usar `set` para deduplicación y membership intensivo; usar `list` cuando el orden sea relevante.
