"""Vista Torres de Hanoi
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Interacción y visualización de pasos para Hanoi.
"""

class HanoiView:
    def get_inputs(self):
        try:
            n = int(input("Ingrese número de discos (entero positivo): "))
            origen = input("Nombre varilla origen (ej: A): ").strip() or 'A'
            destino = input("Nombre varilla destino (ej: C): ").strip() or 'C'
            auxiliar = input("Nombre varilla auxiliar (ej: B): ").strip() or 'B'
            return n, origen, destino, auxiliar
        except ValueError:
            return None, None, None, None

    def show_steps(self, pasos):
        print("\nPasos:")
        for i, p in enumerate(pasos, 1):
            print(f"{i}. {p}")
        print(f"Total movimientos: {len(pasos)}")

    def show_error(self, msg):
        print(f"Error: {msg}")
