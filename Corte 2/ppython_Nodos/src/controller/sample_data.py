from .list_builder import construir_desde_lista


def crear_lista_default(palabras=None):
    """Crea y devuelve la cabeza de una lista enlazada con 10 palabras por defecto.

    Si se proporciona `palabras` (iterable), se usará esa lista; si no, se usarán
    las palabras por defecto: ['uno', ..., 'diez'].
    """
    if palabras is None:
        palabras = [
            "uno",
            "dos",
            "tres",
            "cuatro",
            "cinco",
            "seis",
            "siete",
            "ocho",
            "nueve",
            "diez",
        ]
    return construir_desde_lista(palabras)
