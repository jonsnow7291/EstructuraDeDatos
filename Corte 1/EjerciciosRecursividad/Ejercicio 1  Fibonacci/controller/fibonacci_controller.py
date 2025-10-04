"""Controlador Fibonacci
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Orquesta la interacción entre el modelo y la vista para
el cálculo del n-ésimo número de Fibonacci.
"""

import sys
import os

# Añadir las rutas de los directorios del modelo y la vista al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from fibonacci import FibonacciModel
from fibonacci_view import FibonacciView

class FibonacciController:
    def __init__(self):
        self.model = FibonacciModel()
        self.view = FibonacciView()

    def run(self):
        num = self.view.get_input()
        if num is not None:
            result = self.model.calculate_fibonacci(num)
            self.view.show_result(result)
        else:
            self.view.show_error("Entrada no válida. Por favor, ingrese un número entero.")

if __name__ == "__main__":
    controller = FibonacciController()
    controller.run()
