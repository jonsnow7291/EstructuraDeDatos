"""Controlador Potencia
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Coordina el cálculo recursivo optimizado de base^exponente.
"""

import sys
import os

# Ajustar rutas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from potencia_model import PotenciaModel
from potencia_view import PotenciaView

class PotenciaController:
    def __init__(self):
        self.model = PotenciaModel()
        self.view = PotenciaView()

    def run(self):
        base, exp = self.view.get_inputs()
        if base is None or exp is None:
            self.view.show_error("Entradas inválidas. Debe ingresar enteros.")
            return
        result = self.model.potencia(base, exp)
        if isinstance(result, str):
            self.view.show_error(result)
        else:
            self.view.show_result(base, exp, result)

if __name__ == "__main__":
    PotenciaController().run()
