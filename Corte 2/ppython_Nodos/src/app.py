"""Aplicación de consola con dos módulos de demostración:

1. Polinomio (lista enlazada de términos) - original.
2. Archivo (shelve) - TDA simple para leer/guardar/modificar.

Uso:
    python -m src.app

Se muestra un menú principal para elegir qué módulo ejecutar.
El estilo es sencillo (nivel estudiante) a propósito.
"""

from typing import List, Tuple

from src.controller.polinomio_controller import PolinomioController
from src.view.console_view import format_polynomial, request_terms_interactively

# Importaciones para módulo archivos
from src.controller.archivo_controller import ArchivoController
from src.view import archivo_view as archivo_view
from src.controller.calendario_controller import CalendarioController
from src.view import calendario_view
from src.controller.polinomio_controller import PolinomioController as _PC
from src.view import polinomio_ops_view


def run_interactive() -> None:
    """Ejecuta la aplicación en modo interactivo: solicita términos y muestra el resultado."""
    controller = PolinomioController()
    terms = request_terms_interactively()
    if not terms:
        print("No se ingresaron términos. Saliendo.")
        return
    controller.add_terms_from_iterable(terms)
    formatted = format_polynomial(controller.get_terms_list())
    print("Polinomio resultante:")
    print(formatted)


def run_sample() -> None:
    """Ejecuta la aplicación con un polinomio de ejemplo para demostración."""
    sample_terms: List[Tuple[int, float]] = [(5, 1), (3, -4), (2, 3)]
    controller = PolinomioController()
    controller.add_terms_from_iterable(sample_terms)
    print("Polinomio de ejemplo:")
    print(format_polynomial(controller.get_terms_list()))


def loop_archivos():
    """Menú interactivo para el TDA de archivos (shelve)."""
    ctrl = ArchivoController()
    while True:
        archivo_view.mostrar_menu()
        op = archivo_view.pedir_opcion()
        if op == "0":
            ctrl.cerrar()
            print("Volviendo al menú principal...")
            break
        elif op == "1":  # abrir
            ruta = archivo_view.pedir_ruta()
            ok = ctrl.abrir(ruta)
            archivo_view.mostrar_resultado("Abierto" if ok else "Error al abrir")
        elif op == "2":  # guardar
            dato = archivo_view.pedir_dato()
            pos = ctrl.guardar(dato)
            if pos is None:
                archivo_view.mostrar_resultado("No hay archivo abierto")
            else:
                archivo_view.mostrar_resultado(f"Guardado en posicion {pos}")
        elif op == "3":  # leer
            pos = archivo_view.pedir_posicion()
            if pos is None:
                continue
            val = ctrl.leer(pos)
            archivo_view.mostrar_resultado(f"Valor: {val!r}")
        elif op == "4":  # modificar
            pos = archivo_view.pedir_posicion()
            if pos is None:
                continue
            dato = archivo_view.pedir_dato()
            ok = ctrl.modificar(pos, dato)
            archivo_view.mostrar_resultado("Modificado" if ok else "No existe esa posicion")
        elif op == "5":  # listar
            valores = ctrl.listar()
            archivo_view.mostrar_lista(valores)
        elif op == "6":  # cerrar
            ctrl.cerrar()
            archivo_view.mostrar_resultado("Cerrado")
        else:
            print("Opcion invalida")


def main_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Polinomio - modo interactivo")
    print("2. Polinomio - ejemplo rápido")
    print("3. Archivo (shelve) - menú archivos")
    print("4. Calendario del mes")
    print("5. Polinomio avanzado (restar/dividir/etc)")
    print("0. Salir")
    return input("Opcion: ").strip()


def main() -> None:
    """Punto de entrada principal con menú de módulos."""
    while True:
        op = main_menu()
        if op == "0":
            print("Saliendo...")
            break
        elif op == "1":
            try:
                run_interactive()
            except Exception:
                print("(Fallo en interactivo, mostrando ejemplo)")
                run_sample()
        elif op == "2":
            run_sample()
        elif op == "3":
            loop_archivos()
        elif op == "4":
            loop_calendario()
        elif op == "5":
            loop_polinomio_avanzado()
        else:
            print("Opcion invalida")


def loop_calendario():
    ctrl = CalendarioController()
    while True:
        calendario_view.mostrar_menu()
        op = calendario_view.pedir_opcion()
        if op == "0":
            print("Volviendo al menú principal...")
            break
        elif op == "1":
            d, nombre = ctrl.dia_actual()
            calendario_view.mostrar_dia(d, nombre)
        elif op == "2":
            calendario_view.mostrar_feriados(ctrl.feriados())
        elif op == "3":
            calendario_view.mostrar_fases(ctrl.fases())
        elif op == "4":
            calendario_view.mostrar_pesca(ctrl.pesca())
        else:
            print("Opcion invalida")


def loop_polinomio_avanzado():
    P = _PC()
    Q = _PC()
    while True:
        polinomio_ops_view.mostrar_menu()
        op = polinomio_ops_view.pedir_opcion()
        if op == "0":
            break
        elif op == "1":
            term = polinomio_ops_view.pedir_termino()
            if term:
                e,c = term
                P.add_term(e,c)
        elif op == "2":
            term = polinomio_ops_view.pedir_termino()
            if term:
                e,c = term
                Q.add_term(e,c)
        elif op == "3":
            polinomio_ops_view.mostrar_pol("P", P.get_terms_list())
            polinomio_ops_view.mostrar_pol("Q", Q.get_terms_list())
        elif op == "4":
            exp = polinomio_ops_view.pedir_exponente()
            if exp is not None:
                ok = P.remove_exponent(exp)
                polinomio_ops_view.mostrar_resultado("Eliminado" if ok else "No existia")
        elif op == "5":
            exp = polinomio_ops_view.pedir_exponente()
            if exp is not None:
                polinomio_ops_view.mostrar_resultado("SI" if P.has_exponent(exp) else "NO")
        elif op == "6":
            R = P.subtract(Q)
            polinomio_ops_view.mostrar_pol("P - Q", R.get_terms_list())
        elif op == "7":
            q, r = P.divide(Q)
            if q is None:
                polinomio_ops_view.mostrar_resultado("Division no valida (divisor vacio o coef 0)")
            else:
                polinomio_ops_view.mostrar_pol("Cociente", q.get_terms_list())
                polinomio_ops_view.mostrar_pol("Resto", r.get_terms_list())
        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()
