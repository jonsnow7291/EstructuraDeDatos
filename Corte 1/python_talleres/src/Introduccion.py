import datetime
from datetime import datetime


class introduccion:
    
    def __init__(self, numero1, numero2, nombre, ciudad):
        self.numero1 = numero1
        self.numero2 = numero2
        self.nombre = nombre
        self.ciudad = ciudad
        self.fechaActual = datetime .now()
        self.suma = self.numero1 + self.numero2

    def suma(self):
        return self.suma
    
    def imprimir(self):
         print (f"Hola {self.nombre}\n, bienvenido a {self.ciudad}. \n el dia de hoy es :{self.fechaActual}")
         
    def marco ():
        print("**********************************")
        print("*                                *")
        print("*        buenas como van         *")
        print("*                                *")
        print("**********************************")
        
if __name__ == "__main__":
    intro = introduccion(5, 10, "Marco", "Medellin")
    intro.imprimir()
    intro.suma()    
    introduccion.marco()