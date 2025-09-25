class ProductoModel:
    """Modelo para calcular el producto de dos números enteros."""

    def multiplicar(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return "Ambos valores deben ser números enteros."
        return a * b
