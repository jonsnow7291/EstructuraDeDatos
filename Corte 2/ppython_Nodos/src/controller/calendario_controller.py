"""Controlador simple para el calendario del mes actual."""
from __future__ import annotations
from src.model.calendario import CalendarioMes

class CalendarioController:
    def __init__(self):
        self._model = CalendarioMes()

    def refrescar(self):
        # recrea modelo por si cambia de día
        self._model = CalendarioMes()

    def dia_actual(self):
        return self._model.dia_actual()

    def feriados(self):
        return self._model.feriados()

    def fases(self):
        return self._model.fases_luna()

    def pesca(self):
        return self._model.pesca()
