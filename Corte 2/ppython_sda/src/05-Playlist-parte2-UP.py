print("*** Playlist de Canciones ***")

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input("Cuantas canciones deseas agregar? "))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(
        f"Proporciona la cancion {indice + 1}: "
    )  # la f es para formatear cadenas, y permite incluir variables, en este caso indice
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabetico. sort
lista_reproduccion.sort(
    reverse=True
)  # Si queremos ordenarlo en orden inverso, agregamos el parametro reverse=True
lista_reproduccion.sort()  # Si queremos ordenarlo en orden normal, no necesitamos agregar el parametro reverse=True

# Mostar la lista lista iterando sus elementos
print("\nIteramos el playlist")
for cancion in lista_reproduccion:
    print(f"- {cancion}")
