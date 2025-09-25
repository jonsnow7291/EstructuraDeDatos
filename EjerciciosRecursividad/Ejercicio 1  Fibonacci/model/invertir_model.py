class InvertirModel:
    """Modelo para invertir una secuencia de caracteres (string)."""

    def invertir(self, texto: str):
        if not isinstance(texto, str):
            return "La entrada debe ser un texto (string)."
        if texto == "":
            return "La cadena no debe estar vacía."
        # Uso de slicing para invertir
        return texto[::-1]
