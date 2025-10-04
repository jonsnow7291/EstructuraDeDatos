"""Punto de entrada para la aplicación seno_mvc.

Usamos una importación absoluta (desde el directorio actual) para que
ejecutar `py main.py` desde la carpeta `seno_mvc` funcione sin error
de importación relativa.
"""

# Intentamos primero la importación cuando se ejecuta como paquete
# (python -m seno_mvc.main), y si falla, usamos la importación local
# válida cuando se ejecuta directamente con `py main.py` desde
# la carpeta `seno_mvc`.
try:
    # Ejecutando como paquete: python -m seno_mvc.main
    from seno_mvc.controller.controller import Controlador
except Exception:
    # Ejecutando como script dentro de la carpeta seno_mvc: py main.py
    from controller.controller import Controlador


def main():
    app = Controlador()
    app.iniciar()


if __name__ == "__main__":
    main()