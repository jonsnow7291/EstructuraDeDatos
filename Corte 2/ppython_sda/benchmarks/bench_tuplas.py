"""Benchmark common tuple operations using timeit.

Run as: python bench_tuplas.py
"""
import timeit
import statistics
import sys
from pathlib import Path

# Ensure the package `src` is importable when running this script directly.
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from src import tuplas as tu


def bench_create(n: int, repeat: int = 5):
    stmt = f"tuple(range({n}))"
    t = timeit.repeat(stmt, repeat=repeat, number=1000)
    return statistics.mean(t)


def bench_sum(n: int, repeat: int = 5):
    setup = f"t = tuple(range({n}))"
    stmt = "sum(t)"
    t = timeit.repeat(stmt, setup=setup, repeat=repeat, number=1000)
    return statistics.mean(t)


def bench_concat(n: int, repeat: int = 5):
    setup = f"a = tuple(range({n})); b = tuple(range({n}, {2*n}))"
    stmt = "a + b"
    t = timeit.repeat(stmt, setup=setup, repeat=repeat, number=1000)
    return statistics.mean(t)


def bench_tuple_to_list(n: int, repeat: int = 5):
    setup = f"t = tuple(range({n}))"
    stmt = "list(t)"
    t = timeit.repeat(stmt, setup=setup, repeat=repeat, number=1000)
    return statistics.mean(t)


def run_all(sizes=(10, 100, 1000, 5000)):
    print("n,create, sum, concat, to_list (seconds, mean of repeats)")
    for n in sizes:
        print(
            f"{n}, {bench_create(n):.6f}, {bench_sum(n):.6f}, {bench_concat(n):.6f}, {bench_tuple_to_list(n):.6f}"
        )


if __name__ == "__main__":
    run_all()
