print("*** Manejo de Tuplas ***")

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# No podemos modificar una tupla
# mi_tupla[0] = 10
# mi_tupla.append(6)

# Iteramos los elementos de una tupla
for elemento in mi_tupla:
    # el parametro end=' ' es para que no haga un salto de linea, sino que ponga un espacio
    print(elemento, end=" ")

# Crear una tupla para una coordenada x,y
coordenadas = (3, 5)
# Accedemos a cada elemento de la tupla
print(f"\nCoordenada en el eje x: {coordenadas[0]}")
print(f"Coordenada en el eje y: {coordenadas[1]}")

# Crear una tupla unitaria
tupla_un_elemento = (10,)
print(f"Tupla de un elemento: {tupla_un_elemento}")

# Tupla anidada
tuplas_anidada = (1, (2, 3), (4, 5))
print(f"Segundo elemento tupla anidada: {tuplas_anidada[1]}")

# Ventajas de las tuplas sobre las listas
# 1. Las tuplas son inmutables, lo que las hace más seguras
# 2. Las tuplas pueden ser usadas como claves en diccionarios
# 3. Las tuplas pueden ser más rápidas que las listas para ciertas operaciones
# Ejemplo de uso de tuplas como claves en diccionarios

import time

lista = list(range(1000000))
tupla = tuple(range(1000000))

# Medir tiempo de acceso
inicio_lista = time.time()
_ = lista[500000]
fin_lista = time.time()

inicio_tupla = time.time()
_ = tupla[500000]
fin_tupla = time.time()

print("Acceso en lista:", fin_lista - inicio_lista)
print("Acceso en tupla:", fin_tupla - inicio_tupla)

# Ejemplo de uso de tuplas como claves en diccionarios
# Un diccionario es una estructura de datos que almacena pares clave-valor
coordenadas = {(10.5, 20.3): "Punto A", (15.2, 25.1): "Punto B"}
print(coordenadas[(10.5, 20.3)])

usuarios = ["Ana", "Luis", "Carlos"]
usuarios.append("María")
print(usuarios)
usuarios[0] = "Pedro"  # Esto no es posible en una tupla
usuarios.remove("Luis")  # Esto no es posible en una tupla


# Ejemplo de función que retorna múltiples valores usando tuplas
def calcular(numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    resta = numero_uno - numero_dos
    return suma, resta  # Retorna una tupla


resultado = calcular(10, 5)
print("Suma:", resultado[0])
print("Resta:", resultado[1])
