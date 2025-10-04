print("*** Agenda de Contactos ***")

agenda = {
    "Carlos": {
        "telefono": "55667711",
        "email": "carlos@mail.com",
        "direccion": "Calle Principal 132",
    },
    "María": {
        "telefono": "99887733",
        "email": "maria@mail.com",
        "direccion": "Avenida Central 456",
    },
    "Pedro": {
        "telefono": "55139078",
        "email": "pedro@mail.com",
        "direccion": "Plaza Mayor 789",
    },
}

print(agenda)

# Función que que muestra las claves y valores del diccionario personas.json de forma ordenada, que se
# se encuentra en la carpeta 'data' (usa el módulo json y la función sorted())
import json


def mostrar_diccionario_ordenado():
    with open("data/personas.json", "r") as file:
        personas = json.load(file)
        for persona in sorted(personas, key=lambda x: x["nombre"]):
            print(f"Nombre: {persona['nombre']}")
            print(f"Edad: {persona['edad']}")
            print(f"Ciudad: {persona['ciudad']}")
            print(f"Profesión: {persona['profesion']}")
            print(f"Email: {persona['email']}")
            print("-" * 20)
            print()  # Salto de línea extra entre personas


mostrar_diccionario_ordenado()
# Llamamos a la función para mostrar el diccionario ordenado
