class estructuraDeControl:
    def clasinotas():
        notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for nota in notas:
            if nota >= 1 and nota <= 20:
                print(f"Con la nota {nota} estas reprobado :/")
            elif nota >= 21 and nota <= 40:
                print(f"Con la nota {nota} estas aprobado >:)")
            elif nota >= 41 and nota <= 60:
                print(f"Con la nota {nota} estas bien : )")
            elif nota >= 61 and nota <= 80:
                print(f"Con la nota {nota} estas notable :D")
            elif nota >= 81 and nota <= 100:
                print(f"Con la nota {nota} estas sobresaliente <3")
                
    def imprimirTablas():
        for i in range (1,10):
            print (f"Tabla del {i}")
            for j in range (1,11):
                print (f"{i} x {j} = {i*j}")
            print ("------------------")

    def sacarPromedioYSumaLista():
        lista = []
        suma = 0
        while True:
            # Pedir un número al usuario
            numero = int(input("Ingrese un numero (0 para salir): "))
            
            suma += numero
            print(f"La suma actual es: {suma}")
            if numero == 0:
                break
            lista.append(numero)
        
        longitud = len(lista)
        promedio = suma / longitud
        print(f"El promedio es: {promedio}")
    
    def fizzBuzz(inicio,fin):
        for numero in range (inicio,fin+1):
            if numero % 3 == 0 and numero % 5 == 0:
                print ("FizzBuzz")
            elif numero % 3 == 0:
                print ("Fizz")
            elif numero % 5 == 0:
                print ("Buzz")
            else:
                print (numero)
                
if __name__ == "__main__":
    estructuraDeControl.clasinotas()
    estructuraDeControl.imprimirTablas()
    estructuraDeControl.sacarPromedioYSumaLista()
    estructuraDeControl.fizzBuzz(1,100)
        
        
        