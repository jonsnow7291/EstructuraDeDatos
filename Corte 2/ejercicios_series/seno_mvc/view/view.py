"""Vista: interacción por consola con el usuario."""


class VistaConsola:
    """Maneja la entrada/salida por consola."""

    def mostrar_mensaje_inicial(self):
        print("=== Calculadora de Seno (Serie de Maclaurin) ===")

    def obtener_datos_usuario(self):
        """Solicita al usuario el ángulo en grados y la cantidad de términos.

        Valida que las entradas sean numéricas (int o float para grados,
        int positivo para términos) y retorna (grados, terminos).
        """
        while True:
            try:
                angulo_str = input("Ingrese el ángulo en grados: ").strip()
                grados = float(angulo_str)
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número para los grados.")

        while True:
            try:
                terminos_str = input("Ingrese el número de términos (entero >=1): ").strip()
                terminos = int(terminos_str)
                if terminos < 1:
                    raise ValueError()
                break
            except ValueError:
                print("Entrada inválida. Por favor ingrese un entero mayor o igual a 1 para los términos.")

        return grados, terminos

    def mostrar_resultado(self, angulo, resultado):
        print(f"\nÁngulo: {angulo}°")
        print(f"Seno aproximado (serie de Maclaurin): {resultado}")

    def mostrar_mensaje_final(self):
        print("\nGracias por usar la Calculadora de Seno. ¡Hasta luego!")
