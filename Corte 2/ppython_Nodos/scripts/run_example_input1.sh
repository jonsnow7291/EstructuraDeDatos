#!/usr/bin/env bash
# Ejecuta src.app alimentando la entrada desde examples/input1.txt
# Uso: bash scripts/run_example_input1.sh

set -euo pipefail
PYTHON=PYTHONPATH=. .venv/bin/python
# Si el venv no está activado, usar la siguiente forma:
PYTHONPATH=. .venv/bin/python -m src.app < examples/input1.txt
