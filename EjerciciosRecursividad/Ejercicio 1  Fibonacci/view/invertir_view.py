class InvertirView:
    def get_input(self):
        texto = input("Ingrese una secuencia de caracteres a invertir: ").strip()
        return texto

    def show_result(self, original, invertido):
        print(f"Original: {original}\nInvertido: {invertido}")

    def show_error(self, message):
        print(f"Error: {message}")
