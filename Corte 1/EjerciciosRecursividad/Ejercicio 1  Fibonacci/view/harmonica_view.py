"""Vista Serie Armónica
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Maneja entrada y salida para el cálculo de h(n).
"""

class HarmonicaView:
    def get_input(self):
        try:
            n = int(input("Ingrese un entero positivo n para calcular h(n): "))
            return n
        except ValueError:
            return None

    def show_result(self, n, value):
        # Mostrar con 10 decimales para mayor precisión visual
        print(f"h({n}) = {value:.10f}")

    def show_error(self, msg):
        print(f"Error: {msg}")
