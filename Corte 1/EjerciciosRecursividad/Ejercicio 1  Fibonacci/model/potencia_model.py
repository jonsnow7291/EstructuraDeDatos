"""Modelo Potencia Recursiva Rápida
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Calcula base^exponente usando exponentiación binaria recursiva.
"""

class PotenciaModel:
    """Modelo para calcular base^exponente con enteros (exponente >= 0)."""

    def potencia(self, base: int, exponente: int):
        if not isinstance(base, int) or not isinstance(exponente, int):
            return "Ambos valores deben ser enteros."
        if exponente < 0:
            return "El exponente debe ser un entero no negativo."
        return self._pow_rec(base, exponente)

    def _pow_rec(self, base: int, exp: int):
        # Exponente 0 => 1
        if exp == 0:
            return 1
        # Exponente 1 => base
        if exp == 1:
            return base
        # Optimización: exponenciación rápida dividiendo el exponente
        mitad = self._pow_rec(base, exp // 2)
        if exp % 2 == 0:
            return mitad * mitad
        else:
            return base * mitad * mitad
