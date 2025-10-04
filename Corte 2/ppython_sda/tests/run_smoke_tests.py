"""Run lightweight checks for list_ops without pytest.

This script mirrors the pytest checks so it can be executed where pytest
isn't installed. It prints a simple summary and exits with code 0 on success
or 1 on failure.
"""
import sys
from ppython_sda.src import list_ops as lo


def run():
    errors = []

    try:
        assert lo.create_list(5) == [0, 1, 2, 3, 4]
    except AssertionError:
        errors.append('create_list_positive failed')

    try:
        assert lo.create_list(0) == []
        assert lo.create_list(-3) == []
    except AssertionError:
        errors.append('create_list_non_positive failed')

    try:
        lst = lo.create_list(2)
        lo.append_element(lst, 99)
        assert lo.find_value(lst, 99) == 2
    except AssertionError:
        errors.append('append_and_find failed')

    try:
        lst = lo.create_list(3)
        lo.safe_insert(lst, 7, idx=100)
        assert lst[-1] == 7
    except AssertionError:
        errors.append('safe_insert_out_of_range failed')

    try:
        lst = lo.create_list(3)
        val = lo.pop_element(lst)
        assert val == 2
        try:
            lo.pop_element([])
            errors.append('pop_empty did not raise')
        except IndexError:
            pass
    except AssertionError:
        errors.append('pop_and_access failed')

    try:
        lst = [1, 2, 3]
        assert lo.reverse_list(lst) == [3, 2, 1]
        assert lo.map_increment(lst, 2) == [3, 4, 5]
    except AssertionError:
        errors.append('reverse_and_map failed')

    if errors:
        print('FAILED:')
        for e in errors:
            print('-', e)
        return 1
    print('ALL SMOKE TESTS PASSED')
    return 0


if __name__ == '__main__':
    sys.exit(run())
