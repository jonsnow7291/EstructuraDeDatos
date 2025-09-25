class HanoiModel:
    """Modelo para resolver Torres de Hanoi y generar pasos."""

    def resolver(self, n: int, origen: str, destino: str, auxiliar: str, pasos=None):
        if pasos is None:
            pasos = []
        if not isinstance(n, int) or n <= 0:
            return "n debe ser un entero positivo" if n <= 0 else "n inválido"
        # Caso base
        if n == 1:
            pasos.append(f"Mover disco 1 de {origen} a {destino}")
            return pasos
        # Mover n-1 al auxiliar
        self.resolver(n-1, origen, auxiliar, destino, pasos)
        # Mover el disco mayor
        pasos.append(f"Mover disco {n} de {origen} a {destino}")
        # Mover n-1 del auxiliar al destino
        self.resolver(n-1, auxiliar, destino, origen, pasos)
        return pasos
