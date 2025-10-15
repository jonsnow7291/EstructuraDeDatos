"""Vista de consola muy sencilla para interactuar con ArchivoController.
No pretende ser perfecta, solo práctica para el taller.
"""
from __future__ import annotations
from typing import Optional, Any

def mostrar_menu():
    print("\n=== MENU ARCHIVO (shelve) ===")
    print("1. Abrir archivo")
    print("2. Guardar dato (append)")
    print("3. Leer posicion")
    print("4. Modificar posicion")
    print("5. Listar todo")
    print("6. Cerrar archivo")
    print("0. Salir")


def pedir_opcion() -> str:
    return input("Opcion: ").strip()


def pedir_ruta() -> str:
    return input("Ruta (nombre base, ej: datos_shelf): ").strip()


def pedir_dato() -> Any:
    return input("Dato a guardar (texto plano): ")


def pedir_posicion() -> Optional[int]:
    txt = input("Posicion (entero): ").strip()
    if not txt.isdigit():
        print("(No es entero)")
        return None
    return int(txt)


def mostrar_resultado(msg: str):
    print(msg)


def mostrar_lista(valores):
    if not valores:
        print("(lista vacia)")
        return
    for i, v in enumerate(valores):
        print(f"[{i}] => {v}")
