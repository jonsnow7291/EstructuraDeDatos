print("*** Desempaquetado de Tuplas ***")  # unpacking

producto = ("P001", "Camisa", 20.00)

# Desempaquetado
id, descripcion, precio = producto

# Imprimir los valores
# la f antes de la cadena permite usar variables dentro de {}
print(f"Tupla completa: {producto}")
# Valores independientes ya desempaquetados
print(f"Producto: id = {id}, descripcion = {descripcion}, precio = {precio}")

#
persona = ("Alonso", 35, "Ingeniero")

nombre, edad, profesion = persona

print(nombre)  # Alonso
print(edad)  # 35
print(profesion)  # Ingeniero


# Desempaquetado con *
print("*** Desempaquetado con * ***")
numeros = [100, 200, 300, 400, 500]

a, *medio, e = numeros
print(a)  # 1
print(medio)  # [2, 3, 4]
print(e)  # 5
# El operador * permite capturar múltiples valores en una lista


# Desempaquetado en funciones


def operaciones(numero_uno, numero_dos):
    return numero_uno + numero_dos, numero_uno * numero_dos


suma, producto = operaciones(3, 4)

print(suma)  # 7
print(producto)  # 12

# Desempaquetado en bucles
print("*** Desempaquetado en bucles ***")
datos = {"nombre": "Alonso", "edad": 35}

for clave, valor in datos.items():
    print(f"{clave}: {valor}")


# Desempaquetado en listas de tuplas
pares = [(1, "uno"), (2, "dos"), (3, "tres")]

for numero, palabra in pares:
    print(f"{numero} se dice {palabra}")
