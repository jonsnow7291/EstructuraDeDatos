"""Benchmark membership: set vs list, and safe_add_with_limit behavior."""
import timeit
import statistics
import sys
from pathlib import Path

# Make src importable
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from src import suscriptores as S


def bench_membership(n: int, repeat: int = 5):
    setup = f"lst = list(range({n})); s = set(range({n})); x = {n-1}"
    stmt_list = "x in lst"
    stmt_set = "x in s"
    t_list = timeit.repeat(stmt_list, setup=setup, repeat=repeat, number=10000)
    t_set = timeit.repeat(stmt_set, setup=setup, repeat=repeat, number=10000)
    return statistics.mean(t_list), statistics.mean(t_set)


def bench_safe_add(n: int, repeat: int = 5):
    setup = f"s = set(range({n})); from src.suscriptores import safe_add_with_limit"
    stmt = "safe_add_with_limit(s, 'new', max_len={})".format(n+1)
    t = timeit.repeat(stmt, setup=setup, repeat=repeat, number=1000)
    return statistics.mean(t)


def run_all(sizes=(10, 100, 1000, 10000)):
    print("n, list_mem, set_mem, safe_add")
    for n in sizes:
        lm, sm = bench_membership(n)
        sa = bench_safe_add(n)
        print(f"{n}, {lm:.8f}, {sm:.8f}, {sa:.8f}")


if __name__ == '__main__':
    run_all()
