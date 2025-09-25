"""Modelo Invertir Cadena
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Invierte una cadena validando el tipo de entrada.
"""

class InvertirModel:
    """Modelo para invertir una secuencia de caracteres (string)."""

    def invertir(self, texto: str):
        if not isinstance(texto, str):
            return "La entrada debe ser un texto (string)."
        if texto == "":
            return "La cadena no debe estar vacía."
        # Uso de slicing para invertir
        return texto[::-1]
