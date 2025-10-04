"""Operaciones básicas sobre conjuntos (HashSet) para propósitos educativos.

Se envuelven operaciones nativas de Python para hacer explícitos los costos y permitir pruebas.

Complejidad (n = tamaño del conjunto):
- add_element: O(1) promedio, O(n) peor caso por colisiones.
- remove_element: O(1) promedio; KeyError si no existe.
- contains: O(1) promedio.
- union / intersection / difference: O(n + m) donde n,m tamaños de los operandos.
- size: O(1).

Incluye un tipo BadHash para simular colisiones extremas (todos los objetos con el mismo hash) y observar degradación.
"""
from __future__ import annotations
from typing import Iterable, Any, Set

__all__ = [
    "create_set",
    "add_element",
    "remove_element",
    "contains",
    "union_sets",
    "intersection_sets",
    "difference_sets",
    "size",
    "BadHash",
]


def create_set(items: Iterable[Any] | None = None) -> Set[Any]:
    return set(items) if items is not None else set()


def add_element(s: Set[Any], elem: Any) -> None:
    s.add(elem)


def remove_element(s: Set[Any], elem: Any) -> None:
    s.remove(elem)  # Propaga KeyError si no existe (intencional)


def contains(s: Set[Any], elem: Any) -> bool:
    return elem in s


def union_sets(a: Set[Any], b: Set[Any]) -> Set[Any]:
    return a | b


def intersection_sets(a: Set[Any], b: Set[Any]) -> Set[Any]:
    return a & b


def difference_sets(a: Set[Any], b: Set[Any]) -> Set[Any]:
    return a - b


def size(s: Set[Any]) -> int:
    return len(s)


class BadHash:
    """Objeto con hash constante para forzar colisiones en una tabla hash.

    Útil para demostrar degradación de rendimiento cuando todos los elementos
    caen en el mismo bucket.
    """
    __slots__ = ("value",)

    def __init__(self, value: int):
        self.value = value

    def __hash__(self) -> int:  # Todos igual
        return 42

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BadHash):
            return False
        return self.value == other.value

    def __repr__(self) -> str:  # pragma: no cover (no crítico para tests)
        return f"BadHash({self.value})"


if __name__ == "__main__":  # Pequeña demo manual
    s = create_set(range(5))
    add_element(s, 99)
    print("Set:", s)
    print("Contains 3?", contains(s, 3))
    print("Size:", size(s))
    # Demostración de BadHash
    deg = create_set()
    for i in range(5):
        add_element(deg, BadHash(i))
    print("Colisiones forzadas:", deg)
