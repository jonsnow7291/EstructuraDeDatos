"""Benchmark empírico para operaciones de inventario basado en lista.

Objetivo: comparar tiempo de find/update/remove (búsqueda lineal) al crecer n.

Uso rápido (desde raíz del repo):
python -m ppython_sda.benchmarks.bench_inventory_ops
"""
from __future__ import annotations
import timeit
from typing import List
from ppython_sda.src.inventory_ops import add_product, find_by_id, update_stock, remove_product

SIZES = [10, 100, 1000, 5000]
REPEAT = 5
NUMBER = 50  # iteraciones internas por medición


def build_inventory(n: int):
    inv: List[dict] = []
    for i in range(n):
        add_product(inv, f"P{i}", i * 1.0, i % 17 + 1)
    return inv


def bench_operation(label: str, stmt: str, setup: str):
    tiempos = timeit.repeat(stmt=stmt, setup=setup, repeat=REPEAT, number=NUMBER)
    mejor = min(tiempos) / NUMBER
    promedio = sum(tiempos) / REPEAT / NUMBER
    print(f"{label:<20} best={mejor:.6e}s avg={promedio:.6e}s")


def main():
    print("Benchmark inventario (lista lineal)")
    print(f"REPEAT={REPEAT} NUMBER={NUMBER}\n")
    for n in SIZES:
        print(f"-- n={n} --")
        setup_common = (
            "from __main__ import build_inventory, find_by_id, update_stock, remove_product;"\
            f"inv=build_inventory({n})"
        )
        # Buscar id al inicio y al final
        bench_operation(
            f"find_first n={n}",
            "find_by_id(inv, 0)",
            setup_common,
        )
        bench_operation(
            f"find_last n={n}",
            f"find_by_id(inv, {n-1})",
            setup_common,
        )
        bench_operation(
            f"update_last n={n}",
            f"update_stock(inv, {n-1}, 123)",
            setup_common,
        )
        bench_operation(
            f"remove_last n={n}",
            f"remove_product(inv, {n-1})",
            setup_common,
        )
        print()

if __name__ == "__main__":  # pragma: no cover
    main()
