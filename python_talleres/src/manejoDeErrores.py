class IntentosAgotadosError(Exception):
    pass

class ManejoErrores:
    
    def conversor_robusto(self):
        while True:
            try:
                entrada = input("Ingresa un número entero: ")
                numero = int(entrada)
                print(f"Número convertido: {numero}")
                return numero
            except ValueError:
                print("Error: No es un número entero válido. Intenta de nuevo.")
    
    def calculadora_robusta(self):
        print("=== CALCULADORA ROBUSTA ===")
        
        while True:
            try:
                num1 = float(input("Ingresa el primer número: "))
                break
            except ValueError:
                print("Error: Ingresa un número válido.")
        
        while True:
            try:
                num2 = float(input("Ingresa el segundo número: "))
                break
            except ValueError:
                print("Error: Ingresa un número válido.")
        
        operacion = input("Operación (+, -, *, /): ")
        
        try:
            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                resultado = num1 / num2
            else:
                print("Operación no válida.")
                return
            
            print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
            return resultado
            
        except ZeroDivisionError:
            print("Error: No se puede dividir por cero.")
        except ValueError:
            print("Error: Valores no válidos para la operación.")
    
    def lector_menu(self):
        print("=== MENÚ ===")
        print("1. Opción 1")
        print("2. Opción 2") 
        print("3. Opción 3")
        print("4. Opción 4")
        
        while True:
            try:
                opcion = int(input("Selecciona una opción (1-4): "))
                if 1 <= opcion <= 4:
                    print(f"Has seleccionado la opción {opcion}")
                    return opcion
                else:
                    print("Error: La opción debe estar entre 1 y 4.")
            except ValueError:
                print("Error: Debes ingresar un número entero.")
    
    def leer_float(self, msg, intentos=3):
        for i in range(intentos):
            try:
                return float(input(msg))
            except ValueError:
                print(f"No es número. Intenta de nuevo. Te quedan {intentos - i - 1} intentos.")
        raise IntentosAgotadosError("Se agotaron los intentos.")
    
    def probar_leer_float(self):
        try:
            numero = self.leer_float("Ingresa un número decimal: ", 3)
            print(f"Número ingresado: {numero}")
        except IntentosAgotadosError as e:
            print(f"Error: {e}")
    
    def ejecutar_ejercicios(self):
        print("Ejercicio 1: Conversor robusto")
        print("-" * 30)
        self.conversor_robusto()
        
        print("\n" + "="*40 + "\n")
        
        print("Ejercicio 2: Calculadora robusta")
        print("-" * 30)
        self.calculadora_robusta()
        
        print("\n" + "="*40 + "\n")
        
        print("Ejercicio 3: Lector de menú")
        print("-" * 30)
        self.lector_menu()
        
        print("\n" + "="*40 + "\n")
        
        print("Reto extra: Leer float con límite de intentos")
        print("-" * 30)
        self.probar_leer_float()


def main():
    manejo = ManejoErrores()
    manejo.ejecutar_ejercicios()


if __name__ == "__main__":
    main()
