"""Controlador: coordina modelo y vista.

Las importaciones intentan funcionar tanto cuando el paquete se ejecuta
con `python -m seno_mvc.main` (imports relativos) como cuando se ejecuta
directamente `py main.py` desde la carpeta `seno_mvc` (imports locales).
"""

try:
    # Cuando se ejecuta como paquete: python -m seno_mvc.main
    from ..model.model import CalculadoraCientifica
    from ..view.view import VistaConsola
except Exception:
    # Cuando se ejecuta como script dentro de la carpeta seno_mvc: py main.py
    from model.model import CalculadoraCientifica
    from view.view import VistaConsola


class Controlador:
    """Intermediario entre la vista y el modelo."""

    def __init__(self):
        self.modelo = CalculadoraCientifica()
        self.vista = VistaConsola()

    def iniciar(self):
        self.vista.mostrar_mensaje_inicial()
        grados, terminos = self.vista.obtener_datos_usuario()
        rad = self.modelo.grados_a_radianes(grados)
        resultado = self.modelo.seno_aproximado(rad, terminos)
        self.vista.mostrar_resultado(grados, resultado)
        self.vista.mostrar_mensaje_final()
