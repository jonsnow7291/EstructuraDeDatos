class operacionesYExpresiones:
    def __init__(self, radio):
        PI = 3.1415
        self.radio = radio
        self.area = PI * (radio ** 2)
        
#? Comienzo de ejercicios
    #? Calculo de area
    def calcularArea(self):
        return self.area
    
    #? Verificacion de multiplo
    def VerificarMultiplo(self):
        if self.radio % 5 == 0:
            return f"El numero {self.radio} es multiplo de 5"
        else:
            return f"El numero {self.radio} no es multiplo de 5"

    #? verficador de edad 
    def VerEdad (edad):
        if edad >= 18 and edad < 65:
            return "tu edad esta entro los 18 y 65 años"
        else: 
            return "tu edad no esta entro los 18 y 65 años"
    #? Reto Extra: calculadora
    def calculadora(n1, n2, operacion):
        match operacion:
            case 1:
                return print (n1 + n2)
            case 2:
                return print (n1 - n2)
            case 3:
                return print (n1 / n2)
            case 4:
                return print (n1 * n2)
if __name__ == "__main__":
    operacion = operacionesYExpresiones(10)
    print (f"El area del circulo es: {operacion.calcularArea()}")
    print (operacion.VerificarMultiplo())
    print (operacionesYExpresiones.VerEdad(20))
    operacionesYExpresiones.calculadora(5,3,1)
    operacionesYExpresiones.calculadora(5,3,2)
    operacionesYExpresiones.calculadora(5,3,3)
    operacionesYExpresiones.calculadora(5,3,4)
            
            
    
