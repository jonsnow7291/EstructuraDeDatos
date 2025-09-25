class PotenciaView:
    def get_inputs(self):
        try:
            base = int(input("Ingrese la base (entero): "))
            exp = int(input("Ingrese el exponente (entero no negativo): "))
            return base, exp
        except ValueError:
            return None, None

    def show_result(self, base, exp, result):
        print(f"{base}^{exp} = {result}")

    def show_error(self, message):
        print(f"Error: {message}")
