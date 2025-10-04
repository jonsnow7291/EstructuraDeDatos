class colecciones: 
    def __init__(self):
        self.lista = []
        self.tupla = ()
        self.diccionario = {}
    #Lista para suma y promedio
    def manejarLista(self):
        self.lista = [1, 2, 3, 4, 5]
        longitud = len(self.lista)
        suma = 0
        for i in self.lista:
            suma += i
            print("la suma va en : "+str(suma))
        print(f"el total de la suma es: {suma}")
        promedio = suma / longitud
        print(f"el promedio es: {promedio}")
    # ejercicio de contactos
    def directorio(self):
        self.diccionario = [{"nombre": "camilo","telefono": 123456}, 
                            {"nombre": "maria","telefono": 654321}, 
                            {"nombre": "santiago","telefono": 390281390}, 
                            {"nombre": "martha","telefono": 4809328}, 
                            {"nombre": "celia","telefono": 5893405}]
        nombre = input ("Operador: buenas sumerce a quien necesita?").lower()
        print("random : quisiera comunicarme con: "+nombre)
        encontrado = False
        for contacto in self.diccionario:
            if contacto["nombre"].lower() == nombre:
                print (f"por supuesto, el numero de {contacto['nombre']} es {contacto['telefono']}")
                encontrado = True 
            else:
                print("Buscando...")
                continue
        if not encontrado:
            print("Lo siento, no tengo ese contacto en mi directorio.")
        
    def llamadoALista(self) :
        self.diccionario.append({"nombre": "Samara", "telefono": 1234567})
        self.diccionario.append({"nombre": "Camilo", "telefono": 1234567})
        self.diccionario.append({"nombre": "Santiago", "telefono": 1234567})
        print("Bueno, empieza el llamado a la lista")
        for contacto in self.diccionario:
            print(f"Esta, {contacto['nombre']}!!!")
    
    def inventarioSimple():
        inventario =[{},{},{}]
        inventario[0] = {"nombre": "Lapiz", "cantidad": 10, "precio": 500}
        inventario[1] = {"nombre": "Cuaderno", "cantidad": 5, "precio": 1000}
        inventario[2] = {"nombre": "Borrador", "cantidad": 20, "precio": 200}
        productoCaro = {};
        for item in inventario:
            print(f"Producto: {item['nombre']}, Cantidad: {item['cantidad']}, Precio: {item['precio']}")
            suma += item['cantidad'] * item['precio']
            if item['precio'] > productoCaro.get('precio', 0):
                productoCaro = item
        print(f"El valor total del inventario es: {suma}")
        print(f"el producto mas caro fue: {productoCaro['nombre']} con un precio de {productoCaro['precio']}")