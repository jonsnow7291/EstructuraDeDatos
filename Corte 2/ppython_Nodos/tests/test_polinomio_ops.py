from src.model.polinomio import (
    Polinomio,
    agregar_termino,
    polinomio_a_lista,
    existe_termino,
    eliminar_termino,
    restar,
    dividir,
)


def construir(vals):
    p = Polinomio()
    for e,c in vals:
        agregar_termino(p, e, c)
    return p


def test_existe_y_eliminar():
    p = construir([(3,2),(1,5)])
    assert existe_termino(p,3)
    assert existe_termino(p,1)
    assert not existe_termino(p,2)
    assert eliminar_termino(p,3)
    assert not existe_termino(p,3)
    assert not eliminar_termino(p,9)


def test_restar():
    a = construir([(3,4),(1,2)])  # 4x^3 + 2x
    b = construir([(3,1),(2,5)])  # x^3 + 5x^2
    r = restar(a,b)               # 3x^3 -5x^2 +2x
    assert polinomio_a_lista(r) == [(3,3),(2,-5),(1,2)]


def test_dividir_simple():
    # (2x^2 + 4x) / (2x) = x + 2, resto 0
    a = construir([(2,2),(1,4)])
    b = construir([(1,2)])
    q, rem = dividir(a,b)
    assert polinomio_a_lista(q) == [(1,1),(0,2)]  # x + 2
    assert polinomio_a_lista(rem) == []


def test_dividir_con_resto():
    # (x^2 + 1) / (x) => q = x, resto 1
    a = construir([(2,1),(0,1)])
    b = construir([(1,1)])
    q, rem = dividir(a,b)
    assert polinomio_a_lista(q) == [(1,1)]
    assert polinomio_a_lista(rem) == [(0,1)]
