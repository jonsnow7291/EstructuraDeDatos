print("*** Diccionarios en Python ***")
"""
En Python, un diccionario es una estructura de datos que permite almacenar información en pares de clave y valor. 
Es muy útil cuando quieres representar entidades con múltiples atributos, como una persona, un producto, o una configuración.
"""
# Creamos un dict de persona con clave y valor

persona = {
    "nombre": "Sergio",
    "edad": 30,
    "ciudad": "México",
    "profesion": "Ingeniero",
    "email": "sergio@example.com",
    "telefono": "555-1234",
}

# Mostramos el diccionario completo
print(f"Diccionario de persona: {persona}")

# Acceder a los elementos del diccionario
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}')
print(f'Ciudad: {persona.get("ciudad")}')
print(f'Profesión: {persona.get("profesion")}')
print(f'Email: {persona.get("email")}')
if "telefono" in persona:
    print(f"Teléfono: {persona['telefono']}")

# Modificar un valor en el diccionario
persona["edad"] = 31  # Actualizamos la edad
print(f'Edad actualizada: {persona["edad"]}')
persona["email"] = "sergio.nuevo@example.com"
print(f'Email actualizado: {persona["email"]}')

# Agregar un nuevo par clave-valor
persona["pais"] = "México"  # Agregamos el país de residencia
print(f'País agregado: {persona["pais"]}')
print(f"Diccionario actualizado: {persona}")

# Eliminar un par clave-valor
del persona["telefono"]  # Eliminamos el teléfono
print(f"Diccionario después de eliminar el teléfono: {persona}")
persona.pop("ciudad", None)  # Eliminamos la ciudad
print(f"Diccionario después de eliminar la ciudad: {persona}")
# persona.pop('direccion', None)  # Intentamos eliminar una clave que no existe (no genera error)
print(f"Diccionario después de intentar eliminar una clave inexistente: {persona}")
