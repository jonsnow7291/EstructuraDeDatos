from src.model.nodo import Nodo


class DatoPolinomio(object):
    """Clase que representa un término del polinomio (coeficiente y exponente)."""

    def __init__(self, valor, termino):
        """Crea un término del polinomio con coeficiente y exponente.

        Args:
            valor: coeficiente (numérico)
            termino: exponente (entero)
        """
        self.coeficiente = valor
        self.exponente = termino


class Polinomio(object):
    """Clase para representar un polinomio como lista enlazada de términos.

    El polinomio mantiene la referencia al término de mayor exponente
    en `termino_mayor` y el `grado` actual (mayor exponente).
    """

    def __init__(self):
        """Inicializa un polinomio vacío."""
        self.termino_mayor = None  # cabeza de la lista enlazada de términos
        self.grado = -1


def agregar_termino(polinomio, termino, valor):
    """Agrega un término (exponente `termino`, coeficiente `valor`) al polinomio.

    Inserta el nuevo término en la lista enlazada de forma que se mantenga el
    orden decreciente por exponente (termino mayor primero).

    Args:
        polinomio: instancia de Polinomio
        termino: exponente entero
        valor: coeficiente (numérico)
    """
    aux = Nodo()
    dato = DatoPolinomio(valor, termino)
    aux.dato = dato

    # Si el término es de mayor exponente que el grado actual, inserta al inicio
    if termino > polinomio.grado:
        aux.siguiente = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        # Buscar la posición adecuada (antes del primer término con exponente menor)
        actual = polinomio.termino_mayor
        # Si la lista está vacía o sólo existe un término y no se cumple la condición
        if actual is None:
            polinomio.termino_mayor = aux
            polinomio.grado = termino
            return

        # Avanzar hasta encontrar el lugar de inserción
        while (
            getattr(actual, "siguiente", None) is not None
            and termino < actual.siguiente.dato.exponente
        ):
            actual = actual.siguiente

        aux.siguiente = actual.siguiente
        actual.siguiente = aux


def polinomio_a_lista(polinomio):
    """Devuelve una lista de tuplas (exponente, coeficiente) recorriendo el polinomio."""
    out = []
    cur = polinomio.termino_mayor
    while cur is not None:
        d = cur.dato
        out.append((d.exponente, d.coeficiente))
        cur = cur.siguiente
    return out
