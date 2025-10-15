from src.view.printer import imprimir_lista
from src.model.nodo import Nodo


def test_imprimir_lista_empty():
    assert imprimir_lista(None) == []


def test_imprimir_lista_values():
    n1 = Nodo("x")
    n2 = Nodo("y")
    n1.siguiente = n2
    assert imprimir_lista(n1) == ["x", "y"]
