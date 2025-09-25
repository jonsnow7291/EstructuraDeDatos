"""Vista Suma de Enteros
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Interacción para la suma 0..n.
"""

class SumaView:
    def get_input(self):
        try:
            num = int(input("Ingrese un número entero positivo (o 0) para sumar desde 0 hasta n: "))
            return num
        except ValueError:
            return None

    def show_result(self, n, result):
        print(f"La suma de los enteros desde 0 hasta {n} es: {result}")

    def show_error(self, message):
        print(f"Error: {message}")
