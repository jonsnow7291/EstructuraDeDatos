class LogEnteroView:
    def get_inputs(self):
        try:
            n = int(input("Ingrese n (entero positivo): "))
            b = int(input("Ingrese b (base entera > 1): "))
            return n, b
        except ValueError:
            return None, None

    def show_result(self, n, b, k):
        print(f"log_base_{b}({n}) = {k}")

    def show_error(self, msg):
        print(f"Error: {msg}")
