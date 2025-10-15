def imprimir_lista(cabeza):
    """Devuelve una lista de valores recorriendo desde cabeza usando el atributo `siguiente`."""
    out = []
    cur = cabeza
    while cur is not None:
        out.append(cur.dato)
        cur = cur.siguiente
    return out
