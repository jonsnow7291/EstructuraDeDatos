class FibonacciView:
    def get_input(self):
        try:
            num = int(input("Ingrese un número para calcular la sucesión de Fibonacci: "))
            return num
        except ValueError:
            return None

    def show_result(self, result):
        print(f"El resultado es: {result}")

    def show_error(self, message):
        print(f"Error: {message}")
