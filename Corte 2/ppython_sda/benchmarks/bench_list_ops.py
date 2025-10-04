"""Simple micro-benchmark for list operations used in the notebook.

Run with: python benchmarks/bench_list_ops.py
"""
import timeit
from ppython_sda.src import list_ops as lo


def bench_for_n(n, repeats=3):
    setup = f'from ppython_sda.src import list_ops as lo; lst = lo.create_list({n})'
    results = {}
    results['append'] = timeit.timeit('lo.append_element(lst, 42)', setup=setup, number=1000) / 1000
    results['insert0'] = timeit.timeit('lo.safe_insert(lst, 42, idx=0)', setup=setup, number=500) / 500
    results['pop_end'] = timeit.timeit('lo.pop_element(lst)', setup=setup, number=1000) / 1000
    results['pop0'] = timeit.timeit('lst.pop(0)', setup=setup, number=500) / 500
    results['access'] = timeit.timeit('lo.access_index(lst, 0)', setup=setup, number=10000) / 10000
    results['search'] = timeit.timeit('lo.find_value(lst, -1)', setup=setup, number=200) / 200
    return results


if __name__ == '__main__':
    for n in [100, 1000, 5000]:
        r = bench_for_n(n)
        print(f'n={n}:', r)
