from src.model.nodo import Nodo


def test_nodo_repr_and_links():
    n1 = Nodo("a")
    n2 = Nodo("b")
    n1.siguiente = n2
    assert repr(n1) == "Nodo('a')"
    assert n1.dato == "a"
    assert n1.siguiente is n2


def test_nodo_default():
    n = Nodo()
    assert n.dato is None
    assert n.siguiente is None
