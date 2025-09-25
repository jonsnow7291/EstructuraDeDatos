"""Modelo Logaritmo Entero
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Calcula floor_b(n) por divisiones sucesivas.
"""

class LogEnteroModel:
    """Modelo para calcular el logaritmo entero floor_{b}(n),
    es decir el mayor k tal que b**k <= n, usando divisiones sucesivas.
    """

    def calcular(self, n: int, b: int):
        if not isinstance(n, int) or not isinstance(b, int):
            return "n y b deben ser enteros."
        if n <= 0:
            return "n debe ser un entero positivo."
        if b <= 1:
            return "La base b debe ser un entero mayor que 1."
        k = 0
        valor = n
        while valor >= b:
            valor //= b
            k += 1
        return k
