import sys
import os

# Ajustar rutas para importar modelo y vista
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from suma_model import SumaModel
from suma_view import SumaView

class SumaController:
    def __init__(self):
        self.model = SumaModel()
        self.view = SumaView()

    def run(self):
        n = self.view.get_input()
        if n is None:
            self.view.show_error("Entrada no válida. Debe ingresar un número entero.")
            return
        result = self.model.suma_hasta(n)
        if isinstance(result, str):  # Mensaje de error
            self.view.show_error(result)
        else:
            self.view.show_result(n, result)

if __name__ == "__main__":
    SumaController().run()
