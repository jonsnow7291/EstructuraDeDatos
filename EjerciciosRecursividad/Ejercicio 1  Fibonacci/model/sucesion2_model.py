class Sucesion2Model:
    """Modelo para la sucesión:
    f(1) = 2
    f(n) = f(n-1) + 2n para n >= 2

    (Observación: solución cerrada f(n) = n*(n+1), pero se implementa recursiva por el enunciado.)
    """

    def f(self, n: int):
        if not isinstance(n, int):
            return "n debe ser entero"
        if n <= 0:
            return "n debe ser entero positivo (>=1)"
        if n == 1:
            return 2
        prev = self.f(n - 1)
        if isinstance(prev, str):
            return prev
        return prev + 2 * n
