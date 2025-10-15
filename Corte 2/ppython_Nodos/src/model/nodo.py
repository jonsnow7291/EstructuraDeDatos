class Nodo:
    """Nodo simplemente enlazado (módulo para pruebas)."""

    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def __repr__(self):
        return f"Nodo({self.dato!r})"
