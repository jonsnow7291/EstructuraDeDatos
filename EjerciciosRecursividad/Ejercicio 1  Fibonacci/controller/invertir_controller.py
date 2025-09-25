import sys
import os

# Ajustar rutas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from invertir_model import InvertirModel
from invertir_view import InvertirView

class InvertirController:
    def __init__(self):
        self.model = InvertirModel()
        self.view = InvertirView()

    def run(self):
        texto = self.view.get_input()
        result = self.model.invertir(texto)
        if isinstance(result, str) and (result.startswith("La entrada") or result.startswith("La cadena")):
            self.view.show_error(result)
        else:
            self.view.show_result(texto, result)

if __name__ == "__main__":
    InvertirController().run()
