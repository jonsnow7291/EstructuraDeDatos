"""Módulo controlador para operaciones con polinomios (MVC).

Proporciona la clase `PolinomioController` que media entre el modelo (`Polinomio`)
y una vista. El controlador implementa operaciones para agregar términos
y obtener una representación adecuada para mostrar.
"""

from typing import Iterable, List, Tuple, Optional

from src.model.polinomio import (
    Polinomio,
    agregar_termino,
    polinomio_a_lista,
    existe_termino,
    eliminar_termino,
    restar,
    dividir,
)


class PolinomioController:
    """Controlador que gestiona una instancia de `Polinomio`.

    El controlador expone métodos para agregar términos y obtener el polinomio
    como una lista ordenada de pares (exponente, coeficiente) para presentación.
    """

    def __init__(self, polinomio: Optional[Polinomio] = None):
        """Crear un controlador con un `Polinomio` opcional.

        Args:
            polinomio: Instancia opcional de `Polinomio`. Si es None, se crea una nueva.
        """
        self._polinomio = polinomio or Polinomio()

    @property
    def model(self) -> Polinomio:
        """Devuelve el modelo `Polinomio` subyacente."""
        return self._polinomio

    def add_term(self, exponent: int, coefficient) -> None:
        """Agregar un término al polinomio.

        Args:
            exponent: Exponente (entero) del término.
            coefficient: Coeficiente numérico del término.
        """
        if not isinstance(exponent, int):
            raise TypeError("exponent must be an int")
        agregar_termino(self._polinomio, exponent, coefficient)

    def add_terms_from_iterable(self, values: Iterable[Tuple[int, float]]) -> None:
        """Agregar múltiples términos desde un iterable de (exponente, coeficiente).

        Args:
            values: Iterable de tuplas (exponente, coeficiente).
        """
        for exponent, coefficient in values:
            self.add_term(int(exponent), coefficient)

    def get_terms_list(self) -> List[Tuple[int, float]]:
        """Devuelve el polinomio como lista de (exponente, coeficiente) ordenada por exponente (desc)."""
        return polinomio_a_lista(self._polinomio)

    # Nuevos métodos
    def has_exponent(self, exponent: int) -> bool:
        return existe_termino(self._polinomio, exponent)

    def remove_exponent(self, exponent: int) -> bool:
        return eliminar_termino(self._polinomio, exponent)

    def subtract(self, other: 'PolinomioController') -> 'PolinomioController':
        nuevo = restar(self._polinomio, other._polinomio)
        return PolinomioController(nuevo)

    def divide(self, other: 'PolinomioController'):
        q, r = dividir(self._polinomio, other._polinomio)
        if q is None:
            return None, None
        return PolinomioController(q), PolinomioController(r)
