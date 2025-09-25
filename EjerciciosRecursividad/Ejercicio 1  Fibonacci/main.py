from controller.fibonacci_controller import FibonacciController


def ejecutar_suma_enteros():
    # Importación diferida para evitar cargas innecesarias
    from controller.suma_controller import SumaController
    SumaController().run()


def ejecutar_producto():
    from controller.producto_controller import ProductoController
    ProductoController().run()


def ejecutar_potencia():
    from controller.potencia_controller import PotenciaController
    PotenciaController().run()


def ejecutar_invertir():
    from controller.invertir_controller import InvertirController
    InvertirController().run()


def ejecutar_harmonica():
    from controller.harmonica_controller import HarmonicaController
    HarmonicaController().run()


def ejecutar_log_entero():
    from controller.log_entero_controller import LogEnteroController
    LogEnteroController().run()


def ejecutar_sucesion():
    from controller.sucesion_controller import SucesionController
    SucesionController().run()


def ejecutar_hanoi():
    from controller.hanoi_controller import HanoiController
    HanoiController().run()


def ejecutar_sucesion2():
    from controller.sucesion2_controller import Sucesion2Controller
    Sucesion2Controller().run()


def ejecutar_fibonacci():
    controller = FibonacciController()
    controller.run()


def mostrar_menu():
    print("==============================")
    print("   MENÚ DE EJERCICIOS")
    print("==============================")
    print("1. Sucesión de Fibonacci")
    print("2. Suma de enteros desde 0 hasta n")
    print("3. Producto de dos enteros")
    print("4. Potencia base^exponente")
    print("5. Invertir una secuencia de caracteres")
    print("6. Serie armónica h(n)")
    print("7. Logaritmo entero floor_b(n)")
    print("8. Sucesión recursiva f(n) = 1/(n + f(n-1))")
    print("9. Torres de Hanoi")
    print("10. Sucesión f(n)=f(n-1)+2n")
    print("0. Salir")


def main():
    opciones = {
        "1": ejecutar_fibonacci,
        "2": ejecutar_suma_enteros,
        "3": ejecutar_producto,
        "4": ejecutar_potencia,
        "5": ejecutar_invertir,
        "6": ejecutar_harmonica,
        "7": ejecutar_log_entero,
        "8": ejecutar_sucesion,
        "9": ejecutar_hanoi,
        "10": ejecutar_sucesion2,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "0":
            print("Saliendo... ¡Hasta luego!")
            break
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            print("Opción no válida. Intente nuevamente.\n")


if __name__ == "__main__":
    main()
