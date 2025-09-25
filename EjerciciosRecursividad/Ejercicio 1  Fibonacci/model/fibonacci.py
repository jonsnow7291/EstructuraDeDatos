"""Modelo Fibonacci
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Implementa el cálculo recursivo del n-ésimo número de Fibonacci.
"""


class FibonacciModel:
    def calculate_fibonacci(self, n):
        if n <= 0:
            return "El número debe ser un entero positivo."
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self._fib(n)

    def _fib(self, n):
        if n <= 1:
            return n
        else:
            return self._fib(n-1) + self._fib(n-2)
