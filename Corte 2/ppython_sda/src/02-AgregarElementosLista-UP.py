"""Manejo de listas en Python - Agregar elementos a una listacls"""

print("*** Manejo de Listas ***")

mi_lista = [1, 2, 3, 4, 5]
print(f"{mi_lista} -> Lista original")

# Largo de una lista
print(f"Largo de la lista: {len(mi_lista)}")

# Acceder a los elementos de la lista por indice
print(f"Accedemos al valor del indice 4: {mi_lista[4]}")
print(f"Accedemos al valor del indice -1: {mi_lista[-1]}")

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f"Modificamos el valor del indice 1: {mi_lista[1]}")

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(f"{mi_lista} -> Se agregó el elemento 6")

# Añadir un nuevo elemento en un indice especifico
mi_lista.insert(2, 15)
print(f"{mi_lista} -> Se añadió el valor de 15 en el índice 2")
