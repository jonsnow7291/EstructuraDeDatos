from src.model.nodo import Nodo


class DatoPolinomio(object):
    """Clase que representa un término del polinomio (coeficiente y exponente)."""

    def __init__(self, valor, termino):
        """Crea un término del polinomio con coeficiente y exponente.

        Args:
            valor: coeficiente (numérico)
            termino: exponente (entero)
        """
        self.coeficiente = valor
        self.exponente = termino


class Polinomio(object):
    """Clase para representar un polinomio como lista enlazada de términos.

    El polinomio mantiene la referencia al término de mayor exponente
    en `termino_mayor` y el `grado` actual (mayor exponente).
    """

    def __init__(self):
        """Inicializa un polinomio vacío."""
        self.termino_mayor = None  # cabeza de la lista enlazada de términos
        self.grado = -1


def agregar_termino(polinomio, termino, valor):
    """Agrega un término (exponente `termino`, coeficiente `valor`) al polinomio.

    Inserta el nuevo término en la lista enlazada de forma que se mantenga el
    orden decreciente por exponente (termino mayor primero).

    Args:
        polinomio: instancia de Polinomio
        termino: exponente entero
        valor: coeficiente (numérico)
    """
    aux = Nodo()
    dato = DatoPolinomio(valor, termino)
    aux.dato = dato

    # Si el término es de mayor exponente que el grado actual, inserta al inicio
    if termino > polinomio.grado:
        aux.siguiente = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        # Buscar la posición adecuada (antes del primer término con exponente menor)
        actual = polinomio.termino_mayor
        # Si la lista está vacía o sólo existe un término y no se cumple la condición
        if actual is None:
            polinomio.termino_mayor = aux
            polinomio.grado = termino
            return

        # Avanzar hasta encontrar el lugar de inserción
        while (
            getattr(actual, "siguiente", None) is not None
            and termino < actual.siguiente.dato.exponente
        ):
            actual = actual.siguiente

        aux.siguiente = actual.siguiente
        actual.siguiente = aux


def polinomio_a_lista(polinomio):
    """Devuelve una lista de tuplas (exponente, coeficiente) recorriendo el polinomio."""
    out = []
    cur = polinomio.termino_mayor
    while cur is not None:
        d = cur.dato
        out.append((d.exponente, d.coeficiente))
        cur = cur.siguiente
    return out


# === NUEVAS OPERACIONES (nivel sencillo) ===

def existe_termino(polinomio, exponente):
    """Devuelve True si hay un término con ese exponente."""
    cur = polinomio.termino_mayor
    while cur is not None:
        if cur.dato.exponente == exponente:
            return True
        cur = cur.siguiente
    return False


def eliminar_termino(polinomio, exponente):
    """Elimina el término cuyo exponente coincide. Devuelve True si lo quita."""
    ant = None
    cur = polinomio.termino_mayor
    while cur is not None:
        if cur.dato.exponente == exponente:
            # quitarlo
            if ant is None:  # era cabeza
                polinomio.termino_mayor = cur.siguiente
            else:
                ant.siguiente = cur.siguiente
            # Recalcular grado si era el mayor
            if exponente == polinomio.grado:
                cabeza = polinomio.termino_mayor
                if cabeza is None:
                    polinomio.grado = -1
                else:
                    polinomio.grado = cabeza.dato.exponente
            return True
        ant = cur
        cur = cur.siguiente
    return False


def _construir_desde_lista(pares):
    p = Polinomio()
    for exp, coef in pares:
        agregar_termino(p, exp, coef)
    return p


def restar(p1, p2):
    """Resta p1 - p2 (listas enlazadas) devolviendo un nuevo Polinomio.
    Implementación: pasar a diccionario por exponente, restar coeficientes y reconstruir.
    """
    d = {}
    for e, c in polinomio_a_lista(p1):
        d[e] = d.get(e, 0) + c
    for e, c in polinomio_a_lista(p2):
        d[e] = d.get(e, 0) - c
    # filtrar ceros y ordenar desc
    lista = [(e, d[e]) for e in d if d[e] != 0]
    lista.sort(reverse=True)
    return _construir_desde_lista(lista)


def dividir(p_dividendo, p_divisor):
    """Divide p_dividendo / p_divisor devolviendo (cociente, residuo) como nuevos Polinomios.
    Implementación MUY simplificada: estilo división de polinomios usando la cabeza (mayor exponente)
    hasta que el exponente del dividendo sea menor que el del divisor.
    Si el divisor está vacío o su coeficiente líder es 0, devuelve (None, None).
    """
    lista_divisor = polinomio_a_lista(p_divisor)
    if not lista_divisor:
        return None, None
    exp_dv, coef_dv = lista_divisor[0]
    if coef_dv == 0:
        return None, None
    # Trabajar con una copia mutable del dividendo
    resto = _construir_desde_lista(polinomio_a_lista(p_dividendo))
    cociente_pairs = []
    while True:
        lista_resto = polinomio_a_lista(resto)
        if not lista_resto:
            break
        exp_r, coef_r = lista_resto[0]
        if exp_r < exp_dv:
            break
        # término del cociente
        nuevo_exp = exp_r - exp_dv
        nuevo_coef = coef_r / coef_dv
        cociente_pairs.append((nuevo_exp, nuevo_coef))
        # construir termino multiplicador
        temp = Polinomio()
        agregar_termino(temp, nuevo_exp, nuevo_coef)
        # multiplicar divisor por este termino y restar al resto
        prod_pairs = []
        for e, c in lista_divisor:
            prod_pairs.append((e + nuevo_exp, c * nuevo_coef))
        prod = _construir_desde_lista(prod_pairs)
        resto = restar(resto, prod)
    cociente = _construir_desde_lista(cociente_pairs)
    return cociente, resto
