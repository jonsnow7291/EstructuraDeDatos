"""Vista de consola para mostrar polinomios y recibir entrada sencilla.

Este módulo proporciona funciones para formatear un polinomio para mostrar y
para solicitar entrada al usuario cuando se ejecuta en modo interactivo.
"""

from typing import List, Tuple


def format_polynomial(terms: List[Tuple[int, float]]) -> str:
    """Formatea un polinomio dado como una lista de pares (exponente, coeficiente).

    Se espera que la lista esté ordenada por exponente de forma descendente.
    Ejemplo: [(5, 1), (3, -4), (2, 3)] -> '1*x^5 -4*x^3 +3*x^2'
    """
    if not terms:
        return "0"
    parts = []
    for exponent, coefficient in terms:
        coeff_str = str(coefficient)
        if exponent == 0:
            parts.append(f"{coeff_str}")
        elif exponent == 1:
            parts.append(f"{coeff_str}*x")
        else:
            parts.append(f"{coeff_str}*x^{exponent}")
    return " + ".join(parts).replace("+ -", "- ")


def request_terms_interactively() -> List[Tuple[int, float]]:
    """Solicita al usuario que ingrese términos, uno por línea, en formato 'exponente coeficiente'.

    Una línea vacía finaliza la entrada. Devuelve una lista de tuplas (exponente, coeficiente).
    """
    out = []
    print(
        "Ingrese términos como: <exponente> <coeficiente>. Línea vacía para terminar."
    )
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            break
        parts = line.split()
        if len(parts) != 2:
            print("Entrada inválida. Formato: <exponente> <coeficiente>")
            continue
        try:
            exponent = int(parts[0])
            coefficient = float(parts[1])
        except ValueError:
            print("Valores inválidos. Exponente entero, coeficiente numérico.")
            continue
        out.append((exponent, coefficient))
    return out
