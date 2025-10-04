"""Vista Invertir Cadena
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Interacción para invertir texto.
"""

class InvertirView:
    def get_input(self):
        texto = input("Ingrese una secuencia de caracteres a invertir: ").strip()
        return texto

    def show_result(self, original, invertido):
        print(f"Original: {original}\nInvertido: {invertido}")

    def show_error(self, message):
        print(f"Error: {message}")
