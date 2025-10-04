"""Model: CalculadoraCientifica

Contiene la lógica de negocio: conversión de grados a radianes y
aproximación del seno mediante la serie de Maclaurin.
"""
import math


class CalculadoraCientifica:
    """Calculadora con métodos científicos necesarios para la app."""

    @staticmethod
    def grados_a_radianes(grados):
        """Convierte grados a radianes.

        Parámetros:
            grados (float): ángulo en grados.

        Retorna:
            float: ángulo en radianes.
        """
        return grados * math.pi / 180.0

    @staticmethod
    def seno_aproximado(x_radianes, terminos):
        """Calcula seno(x) usando la serie de Maclaurin hasta `terminos`.

        Parámetros:
            x_radianes (float): ángulo en radianes.
            terminos (int): número de términos a usar (>=1).

        Retorna:
            float: aproximación del seno de x.
        """
        if terminos < 1:
            raise ValueError("El número de términos debe ser al menos 1")

        suma = 0.0
        for n in range(terminos):
            numerador = ((-1) ** n) * (x_radianes ** (2 * n + 1))
            denominador = math.factorial(2 * n + 1)
            suma += numerador / denominador
        return suma
