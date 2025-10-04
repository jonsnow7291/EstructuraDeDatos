"""Modelo Producto de Dos Enteros
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Multiplica dos enteros con validación básica.
"""

class ProductoModel:
    """Modelo para calcular el producto de dos números enteros."""

    def multiplicar(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return "Ambos valores deben ser números enteros."
        return a * b
