"""Modelo Serie Armónica
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Calcula h(n) de forma iterativa (y alternativa recursiva).
"""

class HarmonicaModel:
    """Modelo para calcular la serie armónica h(n) = 1 + 1/2 + ... + 1/n."""

    def calcular(self, n: int):
        if not isinstance(n, int):
            return "n debe ser un entero."
        if n <= 0:
            return "n debe ser un entero positivo."
        total = 0.0
        for i in range(1, n + 1):
            total += 1 / i
        return total
