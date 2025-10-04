print("*** Compresion de Listas ***")

# Una lista con el cuadrado de cada numero
numeros = [1, 2, 3, 4, 5]
cuadrados = [indice**2 for indice in numeros]
print(cuadrados)

# Lista de numeros pares
numeros = range(10 + 1)
pares = [indice for indice in numeros if indice % 2 == 0]
print(pares)

# Lista saludando a cada nombre
nombres = ["Ana", "Jerónimo", "Carlos"]
saludando = [f"Hola {nombre}" for nombre in nombres]
print(saludando)
