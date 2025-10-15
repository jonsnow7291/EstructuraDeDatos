"""Controlador simple para el TDA de archivos con shelve.
Intenta ser sencillo (nivel estudiante) y manejar errores básicos.
"""
from __future__ import annotations
from typing import Any, Optional
from src.model.archivo_shelve import ArchivoShelve

class ArchivoController:
    def __init__(self):
        self._modelo = ArchivoShelve()
        self._abierto = False

    def abrir(self, ruta: str) -> bool:
        try:
            self._modelo.abrir(ruta)
            self._abierto = True
            return True
        except Exception:
            return False

    def cerrar(self) -> None:
        if self._abierto:
            self._modelo.cerrar()
            self._abierto = False

    def guardar(self, dato: Any) -> Optional[int]:
        if not self._abierto:
            return None
        try:
            pos = self._modelo.guardar(dato)
            return pos
        except Exception:
            return None

    def leer(self, posicion: int):
        if not self._abierto:
            return None
        try:
            return self._modelo.leer(posicion)
        except Exception:
            return None

    def modificar(self, posicion: int, dato: Any) -> bool:
        if not self._abierto:
            return False
        try:
            return self._modelo.modificar(posicion, dato)
        except Exception:
            return False

    def listar(self):
        if not self._abierto:
            return []
        try:
            return self._modelo.listar()
        except Exception:
            return []
