"""Vista sencilla para mostrar datos del calendario."""
from __future__ import annotations

def mostrar_menu():
    print("\n=== MENU CALENDARIO ===")
    print("1. Día actual")
    print("2. Feriados del mes")
    print("3. Fases lunares (días)")
    print("4. Calendario pesca (nivel)")
    print("0. Volver")

def pedir_opcion():
    return input("Opcion: ").strip()


def mostrar_dia(dia_num, nombre):
    print(f"Hoy es {dia_num} ({nombre})")


def mostrar_feriados(feriados):
    if not feriados:
        print("No hay feriados configurados en este mes.")
        return
    for d,n in sorted(feriados.items()):
        print(f"{d}: {n}")


def mostrar_fases(fases):
    for k,v in fases.items():
        print(f"{k}: {', '.join(str(x) for x in v) if v else '-'}")


def mostrar_pesca(niveles):
    # mostrar en filas simples: dia:nivel
    for d in sorted(niveles.keys()):
        print(f"{d}:{niveles[d]}", end='  ')
        if d % 10 == 0:
            print()
    print()
