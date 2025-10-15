"""Modelo simple para manejo de datos tipo archivo usando shelve.

No es muy avanzado: guarda pares clave:valor en un shelf.
Se simula posiciones como enteros consecutivos (0,1,2,...) usando claves string.
"""
from __future__ import annotations
import shelve
from typing import Any, Optional

class ArchivoShelve:
    def __init__(self):
        self._db = None  # referencia al shelf
        self._ruta = None

    def abrir(self, ruta: str):
        """Abre (o crea) el 'archivo' en la ruta dada.
        Usa flag 'c' (create) por defecto.
        """
        if self._db is not None:
            # cerrar anterior
            try:
                self._db.close()
            except Exception:
                pass
        # writeback=False para mantenerlo simple
        self._db = shelve.open(ruta, flag='c', writeback=False)
        self._ruta = ruta
        return self

    def cerrar(self):
        if self._db is not None:
            try:
                self._db.close()
            finally:
                self._db = None
                self._ruta = None

    def _check(self):
        if self._db is None:
            raise RuntimeError("No hay archivo abierto. Llama abrir(ruta) primero.")

    def guardar(self, dato: Any):
        """Agrega al final. La 'posición' es el siguiente índice disponible."""
        self._check()
        # encontrar siguiente índice
        idx = 0
        if len(self._db) > 0:
            # claves son strings de enteros
            # max busca la mayor
            idx = max(int(k) for k in self._db.keys()) + 1
        self._db[str(idx)] = dato
        # sync para que se escriba
        try:
            self._db.sync()
        except Exception:
            pass
        return idx

    def leer(self, posicion: int) -> Optional[Any]:
        self._check()
        return self._db.get(str(posicion))

    def modificar(self, posicion: int, dato: Any) -> bool:
        self._check()
        key = str(posicion)
        if key not in self._db:
            return False
        self._db[key] = dato
        try:
            self._db.sync()
        except Exception:
            pass
        return True

    # Pequeña utilidad para listar (útil para la vista/controlador)
    def listar(self):
        self._check()
        # ordenar por índice numérico
        return [self._db[k] for k in sorted(self._db.keys(), key=lambda x: int(x))]

