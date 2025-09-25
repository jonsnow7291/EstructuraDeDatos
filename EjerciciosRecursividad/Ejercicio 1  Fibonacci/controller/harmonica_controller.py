import sys
import os

# Añadir rutas de modelo y vista
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from harmonica_model import HarmonicaModel
from harmonica_view import HarmonicaView

class HarmonicaController:
    def __init__(self):
        self.model = HarmonicaModel()
        self.view = HarmonicaView()

    def run(self):
        n = self.view.get_input()
        if n is None:
            self.view.show_error("Entrada inválida. Debe ser un entero.")
            return
        resultado = self.model.calcular(n)
        if isinstance(resultado, str):
            self.view.show_error(resultado)
        else:
            self.view.show_result(n, resultado)

if __name__ == "__main__":
    HarmonicaController().run()
