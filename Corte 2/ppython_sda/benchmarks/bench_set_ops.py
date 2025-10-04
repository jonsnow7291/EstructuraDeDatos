"""Benchmark de operaciones sobre sets.

Mide tiempos promedio para inserción y pertenencia en:
1. Caso normal (enteros hash regulares).
2. Caso degenerado con BadHash (todas las colisiones).

Uso:
python -m ppython_sda.benchmarks.bench_set_ops
"""
from __future__ import annotations
import timeit
from ppython_sda.src.set_ops import add_element, contains, create_set, BadHash

SIZES = [10, 100, 1000, 5000]
REPEAT = 5
NUMBER = 200


def bench(label: str, stmt: str, setup: str):
    tiempos = timeit.repeat(stmt=stmt, setup=setup, repeat=REPEAT, number=NUMBER)
    best = min(tiempos) / NUMBER
    avg = sum(tiempos) / REPEAT / NUMBER
    print(f"{label:<28} best={best:.3e}s avg={avg:.3e}s")


def main():
    print("Benchmark set_ops (normal vs colisiones forzadas)\n")
    print(f"REPEAT={REPEAT} NUMBER={NUMBER}\n")
    for n in SIZES:
        print(f"-- n={n} --")
        setup_normal = (
            "from ppython_sda.src.set_ops import create_set, add_element, contains;"\
            f"s=create_set(range({n}))"
        )
        bench(f"contains hit normal n={n}", "contains(s, 0)", setup_normal)
        bench(f"contains miss normal n={n}", "contains(s, -1)", setup_normal)
        bench(f"add new normal n={n}", f"add_element(s, {n}+1)", setup_normal)

        setup_degen = (
            "from ppython_sda.src.set_ops import create_set, add_element, contains, BadHash;"\
            f"s=create_set(BadHash(i) for i in range({n}))"
        )
        bench(f"contains hit degen n={n}", "contains(s, list(s)[0])", setup_degen)
        bench(f"add new degen n={n}", "add_element(s, BadHash(999999))", setup_degen)
        print()

if __name__ == "__main__":  # pragma: no cover
    main()
