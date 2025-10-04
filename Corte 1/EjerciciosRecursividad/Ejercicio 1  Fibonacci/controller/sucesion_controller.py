"""Controlador Sucesión Recursiva Fraccionaria
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Coordina la sucesión f(1)=2, f(n)=1/(n+f(n-1)).
"""

import sys
import os

# Ajustar rutas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from sucesion_model import SucesionModel
from sucesion_view import SucesionView

class SucesionController:
    def __init__(self):
        self.model = SucesionModel()
        self.view = SucesionView()

    def run(self):
        n = self.view.get_input()
        if n is None:
            self.view.show_error("Entrada inválida. Debe ser un entero.")
            return
        result = self.model.f(n)
        if isinstance(result, str):
            self.view.show_error(result)
        else:
            self.view.show_result(n, result)

if __name__ == "__main__":
    SucesionController().run()
