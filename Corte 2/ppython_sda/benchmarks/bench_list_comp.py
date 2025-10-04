"""Benchmark list comprehension vs loop and other list ops."""
import timeit
import statistics
import sys
from pathlib import Path

# Make src importable
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from src import listas as L


def bench_squares(n: int, repeat: int = 5):
    setup = f"nums = list(range({n}))"
    stmt_lc = "L.squares_lc(nums)"
    stmt_loop = "L.squares_loop(nums)"
    t_lc = timeit.repeat(stmt_lc, setup=setup, repeat=repeat, number=1000, globals=globals())
    t_loop = timeit.repeat(stmt_loop, setup=setup, repeat=repeat, number=1000, globals=globals())
    return statistics.mean(t_lc), statistics.mean(t_loop)


def bench_concat_and_flatten(n: int, repeat: int = 5):
    setup = f"a = list(range({n})); b = list(range({n}, {2*n})); nested = [list(range({n})) for _ in range(5)]"
    stmt_concat = "L.concat_safe(a, b)"
    stmt_flat = "L.flatten(nested)"
    t_concat = timeit.repeat(stmt_concat, setup=setup, repeat=repeat, number=1000, globals=globals())
    t_flat = timeit.repeat(stmt_flat, setup=setup, repeat=repeat, number=1000, globals=globals())
    return statistics.mean(t_concat), statistics.mean(t_flat)


def run_all(sizes=(10, 100, 1000, 5000)):
    print("n, lc_squares, loop_squares, concat, flatten")
    for n in sizes:
        lc, loop = bench_squares(n)
        concat, flat = bench_concat_and_flatten(n)
        print(f"{n}, {lc:.6f}, {loop:.6f}, {concat:.6f}, {flat:.6f}")


if __name__ == '__main__':
    run_all()
