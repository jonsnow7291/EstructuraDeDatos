class tiposYVariables:
    def __init__(self, entero: int, flotate: float, booleano: bool, cadena: str):
        self.entero = entero
        self.flotate = flotate
        self.booleano = booleano
        self.cadena = cadena
        
    #? imprimir tipo de dato y valor
    def nombrarTipos(self):
        print(f"{type(self.entero)}: {self.entero}")
        print(f"{type(self.flotate)}: {self.flotate}")
        print(f"{type(self.booleano)}: {self.booleano}")
        print(f"{type(self.cadena)}: {self.cadena}")
        
    #? parsear cadena a entero
    def parsearValor(self):
        print(f"Antes de parsear es de tipo : {type(self.cadena)} y su valor es: {self.cadena}")
        EnteroParseado = int (self.cadena)
        print(f"Despues de parsear es de tipo : {type(EnteroParseado)} y su valor es: {EnteroParseado}")
        
    #? recibir paramteros  y imprimirlos
    def printConParametros(self, edad: int, nombre: str):
        print(f"hola soy {nombre} y tengo {edad} años")