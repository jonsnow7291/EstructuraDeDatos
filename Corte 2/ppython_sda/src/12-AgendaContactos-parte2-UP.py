print("*** Agenda de Contactos ***\n\n\n")

agenda = {
    "Carlos": {  # Carlos es la clave del diccionario principal
        "telefono": "55667711",
        "email": "carlos@mail.com",
        "direccion": "Calle Principal 132",
    },
    "María": {  # María es otra clave del diccionario principal
        "telefono": "99887733",
        "email": "maria@mail.com",
        "direccion": "Avenida Central 456",
    },
    "Pedro": {  # Pedro es otra clave del diccionario principal
        "telefono": "55139078",
        "email": "pedro@mail.com",
        "direccion": "Plaza Mayor 789",
    },
}


# Mostrar la agenda con un salto de línea por registro
print("Agenda completa:")
for nombre, datos in agenda.items():
    print(f"{nombre}: {datos}")
print()

# Acceder a la informacion de un contacto en especifico
print(
    f"""Información del contacto de María:
    Teléfono: {agenda['María']['telefono']} # Otra forma: {agenda.get('María').get('telefono')}
    Email: {agenda.get('María').get('email')}
    Dirección: {agenda.get('María').get('direccion')}"""
)

# Agregar un nuevo contacto
agenda["Ana"] = {
    "telefono": "55678392",
    "email": "ana@mail.com",
    "direccion": "Calle Salvador Diaz 321",
}


# Mostrar la agenda actualizada con salto de línea por registro
print("Agenda actualizada:")
for nombre, datos in agenda.items():
    print(f"{nombre}: {datos}")
print()

# Eliminar un contacto existente
agenda.pop("Pedro")
# del agenda['Pedro']
# print(agenda)

# Mostramos los contactos de la agenda
print("\nContactos en la Agenda")
for nombre, detalles in agenda.items():
    print(
        f"""Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}
"""
    )
print("Fin de la agenda de contactos")
