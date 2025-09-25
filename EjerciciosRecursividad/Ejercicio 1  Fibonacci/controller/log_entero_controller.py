import sys
import os

# Ajustar rutas de modelo y vista
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from log_entero_model import LogEnteroModel
from log_entero_view import LogEnteroView

class LogEnteroController:
    def __init__(self):
        self.model = LogEnteroModel()
        self.view = LogEnteroView()

    def run(self):
        n, b = self.view.get_inputs()
        if n is None or b is None:
            self.view.show_error("Entradas inválidas. Deben ser enteros.")
            return
        result = self.model.calcular(n, b)
        if isinstance(result, str):
            self.view.show_error(result)
        else:
            self.view.show_result(n, b, result)

if __name__ == "__main__":
    LogEnteroController().run()
