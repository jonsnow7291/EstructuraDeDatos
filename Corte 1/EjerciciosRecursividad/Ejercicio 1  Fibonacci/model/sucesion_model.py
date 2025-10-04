"""Modelo Sucesión Fraccionaria
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: f(1)=2, f(n)=1/(n + f(n-1)).
"""

class SucesionModel:
    """Modelo para calcular la sucesión definida por:
    f(1) = 2
    f(n) = 1 / (n + f(n-1)) para n >= 2
    """

    def f(self, n: int):
        if not isinstance(n, int):
            return "n debe ser entero."
        if n <= 0:
            return "n debe ser entero positivo (>=1)."
        if n == 1:
            return 2.0
        prev = self.f(n - 1)
        if isinstance(prev, str):
            return prev
        return 1 / (n + prev)
