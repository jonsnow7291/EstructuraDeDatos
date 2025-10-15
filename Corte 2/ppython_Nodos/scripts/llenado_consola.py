"""Script con ejemplo de llenado por consola para crear una lista enlazada.

Este script reusa `src.model.nodo.Nodo` si está disponible; en caso contrario define
una clase local compatible. La función `construir_lista_desde_entrada()` devuelve
la cabeza de la lista creada para poder integrarla en pruebas o en la aplicación.

Uso:
    python scripts/llenado_consola.py

O desde el paquete (con PYTHONPATH=. o venv activado):
    PYTHONPATH=. .venv/bin/python -m scripts.llenado_consola
"""

from __future__ import annotations
from typing import Optional

try:
    # Intentar reutilizar la implementación del proyecto
    from src.model.nodo import Nodo  # type: ignore
except Exception:

    class Nodo:
        """Nodo simplemente enlazado (fallback local)."""

        def __init__(
            self, dato: Optional[object] = None, siguiente: Optional["Nodo"] = None
        ):
            self.dato = dato
            self.siguiente = siguiente

        def __repr__(self) -> str:  # pragma: no cover - demostración
            return f"Nodo({self.dato!r})"


def construir_lista_desde_entrada(prompt: str = "Palabra: ") -> Optional[Nodo]:
    """Lee palabras desde la consola hasta una línea vacía y devuelve la cabeza de la lista.

    Protege contra EOFError para entornos no interactivos.
    """
    print("Ingrese palabras. Deje vacío y presione Enter para terminar.")
    palabras = []
    while True:
        try:
            entrada = input(prompt).strip()
        except EOFError:
            break
        if entrada == "":
            break
        palabras.append(entrada)

    if not palabras:
        return None

    cabeza = Nodo(palabras[0])
    actual = cabeza
    for w in palabras[1:]:
        n = Nodo(w)
        actual.siguiente = n
        actual = n
    return cabeza


def imprimir_lista(cabeza: Optional[Nodo]) -> None:
    """Imprime una lista enlazada numerada a partir de la cabeza (None = vacía)."""
    if cabeza is None:
        print("No se ingresaron palabras.")
        return
    print("\nLista creada:")
    cur = cabeza
    idx = 1
    while cur is not None:
        print(f"{idx}. {cur.dato}")
        cur = cur.siguiente
        idx += 1


def main() -> None:
    cabeza = construir_lista_desde_entrada()
    imprimir_lista(cabeza)


if __name__ == "__main__":
    main()
