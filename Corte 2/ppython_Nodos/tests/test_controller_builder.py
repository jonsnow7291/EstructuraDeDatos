from src.controller.list_builder import construir_desde_lista


def test_construir_empty():
    assert construir_desde_lista([]) is None


def test_construir_and_traverse():
    valores = ["uno", "dos", "tres"]
    cabeza = construir_desde_lista(valores)
    out = []
    cur = cabeza
    while cur is not None:
        out.append(cur.dato)
        cur = cur.siguiente
    assert out == valores
