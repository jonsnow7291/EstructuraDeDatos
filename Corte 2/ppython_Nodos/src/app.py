"""Punto de entrada para la aplicación MVC del Polinomio.

Uso:
    python -m src.app

La aplicación soporta entrada interactiva o cargar un ejemplo pequeño y
mostrar el polinomio formateado por consola.
"""

from typing import List, Tuple

from src.controller.polinomio_controller import PolinomioController
from src.view.console_view import format_polynomial, request_terms_interactively


def run_interactive() -> None:
    """Ejecuta la aplicación en modo interactivo: solicita términos y muestra el resultado."""
    controller = PolinomioController()
    terms = request_terms_interactively()
    if not terms:
        print("No se ingresaron términos. Saliendo.")
        return
    controller.add_terms_from_iterable(terms)
    formatted = format_polynomial(controller.get_terms_list())
    print("Polinomio resultante:")
    print(formatted)


def run_sample() -> None:
    """Ejecuta la aplicación con un polinomio de ejemplo para demostración."""
    sample_terms: List[Tuple[int, float]] = [(5, 1), (3, -4), (2, 3)]
    controller = PolinomioController()
    controller.add_terms_from_iterable(sample_terms)
    print("Polinomio de ejemplo:")
    print(format_polynomial(controller.get_terms_list()))


def main() -> None:
    """Punto de entrada principal. Intenta modo interactivo; si falla, muestra un ejemplo."""
    try:
        # Si se ejecuta en un terminal, pedir datos al usuario; si no, mostrar ejemplo
        run_interactive()
    except Exception:
        # En caso de cualquier fallo, mostrar demostración de ejemplo
        run_sample()


if __name__ == "__main__":
    main()
