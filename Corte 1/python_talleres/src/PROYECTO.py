import random
import json
import os
from datetime import datetime

class AdivinaElNumero:
    
    def __init__(self):
        self.archivo_puntuaciones = "puntuaciones.json"
        self.intentos_realizados = []
    
    def leer_int(self, msg, minimo=None, maximo=None):
        while True:
            try:
                valor = int(input(msg))
                if minimo is not None and valor < minimo:
                    print(f"El valor debe ser al menos {minimo}.")
                    continue
                if maximo is not None and valor > maximo:
                    print(f"El valor debe ser máximo {maximo}.")
                    continue
                return valor
            except ValueError:
                print("Ingresa un entero válido.")
    
    def juego_basico(self, intentos=3, minimo=1, maximo=20):
        secreto = random.randint(minimo, maximo)
        self.intentos_realizados = []
        
        print(f"Adivina el número entre {minimo} y {maximo}. Tienes {intentos} intentos.")
        
        for i in range(1, intentos + 1):
            n = self.leer_int(f"Intento {i}: ", minimo, maximo)
            self.intentos_realizados.append(n)
            
            if n == secreto:
                print("¡Correcto! ¡Ganaste!")
                self.mostrar_intentos()
                return True
            
            pista = "mayor" if n < secreto else "menor"
            print(f"No es. Pista: el secreto es {pista}.")
        
        print(f"Sin intentos. El número era {secreto}.")
        self.mostrar_intentos()
        return False
    
    def mostrar_intentos(self):
        print(f"Tus intentos fueron: {self.intentos_realizados}")
    
    def juego_personalizado(self):
        print("=== CONFIGURACIÓN PERSONALIZADA ===")
        
        minimo = self.leer_int("Número mínimo del rango: ", 1)
        maximo = self.leer_int("Número máximo del rango: ", minimo + 1)
        intentos = self.leer_int("Número de intentos: ", 1, 10)
        
        return self.juego_basico(intentos, minimo, maximo)
    
    def cargar_puntuaciones(self):
        try:
            if os.path.exists(self.archivo_puntuaciones):
                with open(self.archivo_puntuaciones, 'r') as f:
                    return json.load(f)
            return []
        except:
            return []
    
    def guardar_puntuacion(self, nombre, gano, intentos_usados, total_intentos):
        puntuaciones = self.cargar_puntuaciones()
        
        nueva_puntuacion = {
            "nombre": nombre,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "gano": gano,
            "intentos_usados": intentos_usados,
            "total_intentos": total_intentos,
            "intentos": self.intentos_realizados.copy()
        }
        
        puntuaciones.append(nueva_puntuacion)
        
        try:
            with open(self.archivo_puntuaciones, 'w') as f:
                json.dump(puntuaciones, f, indent=2)
            print("Puntuación guardada.")
        except:
            print("Error al guardar la puntuación.")
    
    def mostrar_puntuaciones(self):
        puntuaciones = self.cargar_puntuaciones()
        
        if not puntuaciones:
            print("No hay puntuaciones guardadas.")
            return
        
        print("\n=== HISTORIAL DE PUNTUACIONES ===")
        for i, p in enumerate(puntuaciones, 1):
            estado = "GANÓ" if p["gano"] else "PERDIÓ"
            print(f"{i}. {p['nombre']} - {estado}")
            print(f"   Fecha: {p['fecha']}")
            print(f"   Intentos: {p['intentos_usados']}/{p['total_intentos']}")
            print(f"   Números probados: {p['intentos']}")
            print()
    
    def juego_con_puntuaciones(self):
        nombre = input("Ingresa tu nombre: ")
        
        print("\n¿Qué tipo de juego quieres?")
        print("1. Juego básico (1-20, 3 intentos)")
        print("2. Juego personalizado")
        
        opcion = self.leer_int("Elige una opción (1-2): ", 1, 2)
        
        if opcion == 1:
            gano = self.juego_basico()
            intentos_totales = 3
        else:
            gano = self.juego_personalizado()
            intentos_totales = len(self.intentos_realizados) if not gano else len(self.intentos_realizados)
        
        intentos_usados = len(self.intentos_realizados)
        self.guardar_puntuacion(nombre, gano, intentos_usados, intentos_totales)
    
    def menu_principal(self):
        while True:
            print("\n" + "="*40)
            print("ADIVINA EL NUMERO")
            print("="*40)
            print("1. Juego básico")
            print("2. Juego personalizado")
            print("3. Juego con puntuaciones")
            print("4. Ver historial de puntuaciones")
            print("5. Salir")
            
            opcion = self.leer_int("Elige una opción (1-5): ", 1, 5)
            
            if opcion == 1:
                self.juego_basico()
            elif opcion == 2:
                self.juego_personalizado()
            elif opcion == 3:
                self.juego_con_puntuaciones()
            elif opcion == 4:
                self.mostrar_puntuaciones()
            elif opcion == 5:
                print("¡Gracias por jugar!")
                break


def main():
    juego = AdivinaElNumero()
    juego.menu_principal()


if __name__ == "__main__":
    main()
