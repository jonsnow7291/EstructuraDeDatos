"""Controlador Producto de Dos Enteros
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Coordina la operación de producto entre dos enteros.
"""

import sys
import os

# Ajustar rutas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from producto_model import ProductoModel
from producto_view import ProductoView

class ProductoController:
    def __init__(self):
        self.model = ProductoModel()
        self.view = ProductoView()

    def run(self):
        a, b = self.view.get_inputs()
        if a is None or b is None:
            self.view.show_error("Entradas inválidas. Debe ingresar números enteros.")
            return
        result = self.model.multiplicar(a, b)
        if isinstance(result, str):
            self.view.show_error(result)
        else:
            self.view.show_result(a, b, result)

if __name__ == "__main__":
    ProductoController().run()
