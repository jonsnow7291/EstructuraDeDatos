# ppython_Nodos — Ejemplos y scripts

Este repositorio contiene un cuaderno didáctico y una pequeña aplicación de ejemplo
para trabajar con nodos y polinomios en Python.

## Llenado por consola (ejemplo)

Se ha incluido un script que permite crear una lista enlazada pidiendo palabras al usuario:

- `scripts/llenado_consola.py` — lee palabras desde la consola y muestra la lista creada.

### Ejecutar con el entorno virtual

1. Activa el entorno virtual (opcional, recomendado):

```bash
source .venv/bin/activate
```

2. Ejecuta el script:

```bash
python scripts/llenado_consola.py
```

O sin activar el venv (usando el binario del venv):

```bash
PYTHONPATH=. .venv/bin/python scripts/llenado_consola.py
```

La función principal `construir_lista_desde_entrada()` devuelve la cabeza de la lista,
por lo que puedes importarla desde pruebas o desde `src` si necesitas manipular la lista
programáticamente.

## Ejemplo rápido predefinido

He incluido un fichero de ejemplo con entradas de polinomio y un script que lo ejecuta:

- `examples/input1.txt` — contiene líneas con `<exponente> <coeficiente>` y una línea vacía al final.
- `scripts/run_example_input1.sh` — ejecuta `src.app` alimentando stdin desde `examples/input1.txt`.

Para ejecutar el ejemplo rápido (sin activar el venv manualmente):

```bash
bash scripts/run_example_input1.sh
```

O, si prefieres ejecutarlo explícitamente:

```bash
PYTHONPATH=. .venv/bin/python -m src.app < examples/input1.txt
```
