class salidayentrada:
    
    def calcular_edad(self):
        nombre = input("Ingresa tu nombre: ")
        ano_nacimiento = int(input("Ingresa tu año de nacimiento: "))
        ano_actual = 2025
        edad = ano_actual - ano_nacimiento
        print(f"Hola {nombre}, tienes {edad} años.")
        return edad
    
    def calcular_factura(self):
        print("=== CALCULADORA DE FACTURA ===")
        subtotal = float(input("Ingresa el subtotal: $"))
        iva_porcentaje = 19
        iva = subtotal * (iva_porcentaje / 100)
        total = subtotal + iva
        print("\n--- FACTURA ---")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"IVA ({iva_porcentaje}%): ${iva:.2f}")
        print(f"Total: ${total:.2f}")
        print("----------------")
        return total
    
    def ejecutar_ejercicios(self):
        print("Ejercicio 1: Cálculo de edad")
        print("-" * 30)
        self.calcular_edad()
        print("\n" + "="*40 + "\n")
        print("Ejercicio 2: Cálculo de factura")
        print("-" * 30)
        self.calcular_factura()


def main():
    calculadora = salidayentrada()
    calculadora.ejecutar_ejercicios()


if __name__ == "__main__":
    main()