import math
import random
from datetime import datetime, date

class ModulosYLibrerias:
    
    def simular_dados(self):
        print("=== SIMULADOR DE 100 LANZAMIENTOS DE DADO ===")
        
        frecuencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        
        for _ in range(100):
            resultado = random.randint(1, 6)
            frecuencias[resultado] += 1
        
        print("Frecuencias de cada cara:")
        for cara, frecuencia in frecuencias.items():
            print(f"Cara {cara}: {frecuencia} veces ({frecuencia}%)")
        
        return frecuencias
    
    def calcular_hipotenusa(self):
        print("=== CALCULADORA DE HIPOTENUSA ===")
        
        try:
            a = float(input("Ingresa el primer cateto: "))
            b = float(input("Ingresa el segundo cateto: "))
            
            hipotenusa = math.hypot(a, b)
            
            print(f"Los catetos son: {a} y {b}")
            print(f"La hipotenusa es: {hipotenusa:.2f}")
            
            return hipotenusa
            
        except ValueError:
            print("Error: Ingresa números válidos.")
    
    def dias_hasta_fin_ano(self):
        print("=== DÍAS HASTA FIN DE AÑO ===")
        
        hoy = date.today()
        fin_ano = date(hoy.year, 12, 31)
        
        dias_restantes = (fin_ano - hoy).days
        
        print(f"Fecha actual: {hoy.strftime('%d/%m/%Y')}")
        print(f"Fin de año: {fin_ano.strftime('%d/%m/%Y')}")
        print(f"Días restantes: {dias_restantes} días")
        
        return dias_restantes
    
    def piedra_papel_tijera(self):
        print("=== PIEDRA, PAPEL O TIJERA ===")
        print("Mejor de 3 rondas")
        
        opciones = ["piedra", "papel", "tijera"]
        victorias_jugador = 0
        victorias_maquina = 0
        ronda = 1
        
        while victorias_jugador < 2 and victorias_maquina < 2:
            print(f"\n--- Ronda {ronda} ---")
            
            jugador = input("Elige (piedra/papel/tijera): ").lower()
            
            if jugador not in opciones:
                print("Opción inválida. Intenta de nuevo.")
                continue
            
            maquina = random.choice(opciones)
            
            print(f"Jugador: {jugador}")
            print(f"Máquina: {maquina}")
            
            if jugador == maquina:
                print("¡Empate!")
            elif (jugador == "piedra" and maquina == "tijera") or \
                 (jugador == "papel" and maquina == "piedra") or \
                 (jugador == "tijera" and maquina == "papel"):
                print("¡Ganaste esta ronda!")
                victorias_jugador += 1
            else:
                print("¡La máquina ganó esta ronda!")
                victorias_maquina += 1
            
            print(f"Marcador: Jugador {victorias_jugador} - {victorias_maquina} Máquina")
            ronda += 1
        
        print("\n=== RESULTADO FINAL ===")
        if victorias_jugador > victorias_maquina:
            print("¡FELICIDADES! Ganaste el juego.")
        else:
            print("La máquina ganó el juego. ¡Inténtalo de nuevo!")
        
        return victorias_jugador > victorias_maquina
    
    def ejecutar_ejercicios(self):
        print("Ejercicio 1: Simulador de dados")
        print("-" * 30)
        self.simular_dados()
        
        print("\n" + "="*40 + "\n")
        
        print("Ejercicio 2: Calculadora de hipotenusa")
        print("-" * 30)
        self.calcular_hipotenusa()
        
        print("\n" + "="*40 + "\n")
        
        print("Ejercicio 3: Días hasta fin de año")
        print("-" * 30)
        self.dias_hasta_fin_ano()
        
        print("\n" + "="*40 + "\n")
        
        print("Reto extra: Piedra, Papel o Tijera")
        print("-" * 30)
        self.piedra_papel_tijera()


def main():
    modulos = ModulosYLibrerias()
    modulos.ejecutar_ejercicios()


if __name__ == "__main__":
    main()
