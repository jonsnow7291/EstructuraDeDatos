class funciones :

    def __init__(self, numero1, numero2, nombre="camila guerrero"):
        self.lista = [1,1,2,3,5,8,13,21,34,55,89]
        self.numero1 = numero1
        self.numero2 = numero2
        self.nombre = nombre

    def saludo (self) -> str:
        return f"Hola {self.nombre}, bienvenido a Python"
    def suma (self) -> int:
        return self.numero1 + self.numero2
    
    def sumaEsPar(self) -> bool:
        return self.suma() % 2 == 0
    
    def promedio (self) -> float:
        suma = 0
        for numero in self.lista:
            suma = suma + numero
        return suma / len(self.lista)
    
    def normalizarNombre (self) -> str:
        nombreCap =  self.nombre.capitalize()
        nombreCap = nombreCap.replace(" ", "_")
        return nombreCap
    
if __name__ == "__main__":
    func = funciones(5,10)
    print(func.saludo())
    print(f"La suma es: {func.suma()}")
    print(f"La suma es par? : {func.sumaEsPar()}")
    print(f"El promedio es: {func.promedio()}")
    print(f"El nombre normalizado es: {func.normalizarNombre()}")
