"""Modelo Suma Enteros 0..n
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Calcula la suma de 0 hasta n usando la fórmula cerrada.
"""

class SumaModel:
    """Modelo para calcular la suma de todos los enteros entre 0 y n (inclusive)."""

    def suma_hasta(self, n: int):
        if not isinstance(n, int):
            return "El valor debe ser un número entero."
        if n < 0:
            return "El número debe ser entero positivo o cero."
        # Fórmula matemática eficiente O(1)
        return n * (n + 1) // 2
