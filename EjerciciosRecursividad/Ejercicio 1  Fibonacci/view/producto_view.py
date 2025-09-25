class ProductoView:
    def get_inputs(self):
        try:
            a = int(input("Ingrese el primer número entero: "))
            b = int(input("Ingrese el segundo número entero: "))
            return a, b
        except ValueError:
            return None, None

    def show_result(self, a, b, result):
        print(f"El producto de {a} x {b} es: {result}")

    def show_error(self, message):
        print(f"Error: {message}")
