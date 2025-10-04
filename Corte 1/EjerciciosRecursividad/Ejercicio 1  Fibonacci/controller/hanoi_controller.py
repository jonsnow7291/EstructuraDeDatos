"""Controlador Torres de Hanoi
Autores: Juan Diego Chaparro, Angy Rivas, Karen Ravelo
Fecha: 2025-09-24
Descripción: Coordina la resolución recursiva del problema de Hanoi.
"""

import sys
import os

# Ajustar rutas
def _add_paths():
    base = os.path.dirname(__file__)
    mp = os.path.abspath(os.path.join(base, '..', 'model'))
    vp = os.path.abspath(os.path.join(base, '..', 'view'))
    for p in (mp, vp):
        if p not in sys.path:
            sys.path.insert(0, p)

_add_paths()

from hanoi_model import HanoiModel
from hanoi_view import HanoiView

class HanoiController:
    def __init__(self):
        self.model = HanoiModel()
        self.view = HanoiView()

    def run(self):
        n, origen, destino, auxiliar = self.view.get_inputs()
        if n is None:
            self.view.show_error("Entrada inválida.")
            return
        pasos = self.model.resolver(n, origen, destino, auxiliar)
        if isinstance(pasos, str):
            self.view.show_error(pasos)
        else:
            self.view.show_steps(pasos)

if __name__ == '__main__':
    HanoiController().run()
