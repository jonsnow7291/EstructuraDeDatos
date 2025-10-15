"""Vista sencilla (menú) para operar con polinomios: restar, dividir, eliminar, existe.
Se trabaja con dos polinomios: P (principal) y Q (auxiliar) para operaciones.
"""
from __future__ import annotations
from typing import List, Tuple

def mostrar_menu():
    print("\n=== MENU POLINOMIO AVANZADO ===")
    print("1. Agregar término a P")
    print("2. Agregar término a Q")
    print("3. Mostrar P y Q")
    print("4. Eliminar término de P")
    print("5. Existe exponente en P?")
    print("6. Restar P - Q")
    print("7. Dividir P / Q")
    print("0. Volver")

def pedir_opcion():
    return input("Opcion: ").strip()

def pedir_termino():
    txt = input("<exponente> <coeficiente>: ").strip().split()
    if len(txt) != 2:
        print("Formato incorrecto")
        return None
    try:
        e = int(txt[0]); c = float(txt[1])
        return e, c
    except ValueError:
        print("Valores inválidos")
        return None

def pedir_exponente():
    txt = input("Exponente: ").strip()
    try:
        return int(txt)
    except ValueError:
        print("No es entero")
        return None

def mostrar_pol(label: str, terms: List[Tuple[int,float]]):
    print(label, ":", terms if terms else '[]')

def mostrar_resultado(msg: str):
    print(msg)
