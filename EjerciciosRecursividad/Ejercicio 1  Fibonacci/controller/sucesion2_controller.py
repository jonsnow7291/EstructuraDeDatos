import sys
import os

# Ajustar rutas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'view')))

from sucesion2_model import Sucesion2Model
from sucesion2_view import Sucesion2View

class Sucesion2Controller:
    def __init__(self):
        self.model = Sucesion2Model()
        self.view = Sucesion2View()

    def run(self):
        n = self.view.get_input()
        if n is None:
            self.view.show_error("Entrada inválida. Debe ser entero.")
            return
        result = self.model.f(n)
        if isinstance(result, str):
            self.view.show_error(result)
        else:
            self.view.show_result(n, result)

if __name__ == '__main__':
    Sucesion2Controller().run()
