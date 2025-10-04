"""Vista Sucesión Fraccionaria
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Interacción para f(1)=2, f(n)=1/(n+f(n-1)).
"""

class SucesionView:
    def get_input(self):
        try:
            return int(input("Ingrese n (entero positivo) para f(n): "))
        except ValueError:
            return None

    def show_result(self, n, value):
        print(f"f({n}) = {value:.10f}")

    def show_error(self, msg):
        print(f"Error: {msg}")
