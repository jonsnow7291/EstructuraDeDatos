from src.model.nodo import Nodo


def construir_desde_lista(valores):
    """Construye y devuelve la cabeza de una lista enlazada a partir de `valores` (iterable).
    Devuelve None si `valores` está vacío.
    """
    iterator = iter(valores)
    try:
        first = next(iterator)
    except StopIteration:
        return None
    cabeza = Nodo(first)
    cur = cabeza
    for v in iterator:
        n = Nodo(v)
        cur.siguiente = n
        cur = n
    return cabeza
