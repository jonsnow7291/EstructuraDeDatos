"""Benchmark unpacking patterns vs index/slice access."""
import timeit
import statistics
import sys
from pathlib import Path

# Make src importable
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from src import desempaquetado as ds


def bench_unpack_with_star(n: int, repeat: int = 5):
    setup = f"t = tuple(range({n}))"
    stmt = "first, middle, last = (t[0], t[1:-1], t[-1])"
    # measure a manual unpack using indices and slicing
    t1 = timeit.repeat(stmt, setup=setup, repeat=repeat, number=10000)

    stmt2 = "first, *middle, last = t"
    t2 = timeit.repeat(stmt2, setup=setup, repeat=repeat, number=10000)
    return statistics.mean(t1), statistics.mean(t2)


def bench_namedtuple_conversion(n: int, repeat: int = 5):
    setup = f"t = tuple(range({n}))"
    stmt = "from src.desempaquetado import to_namedtuple; nt = to_namedtuple('P', t)"
    t = timeit.repeat(stmt, setup=setup, repeat=repeat, number=1000)
    return statistics.mean(t)


def run_all(sizes=(10, 100, 1000)):
    print("n, index+slice, star_unpack, namedtuple_conv")
    for n in sizes:
        idx_slice, star = bench_unpack_with_star(n)
        nt = bench_namedtuple_conversion(n)
        print(f"{n}, {idx_slice:.8f}, {star:.8f}, {nt:.8f}")


if __name__ == '__main__':
    run_all()
