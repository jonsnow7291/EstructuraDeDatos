import pytest

from src import listas as L


def test_create_numbers_and_squares_equality():
    nums = L.create_numbers(10)
    assert nums == list(range(10))
    assert L.squares_lc(nums) == L.squares_loop(nums)


def test_filter_even_and_flatten():
    nums = range(11)
    evens = L.filter_even(nums)
    assert all(x % 2 == 0 for x in evens)

    nested = [[1, 2], [3], [], [4, 5]]
    flat = L.flatten(nested)
    assert flat == [1, 2, 3, 4, 5]


def test_unique_preserve_order():
    seq = [1, 2, 1, 3, 2, 4]
    assert L.unique_preserve_order(seq) == [1, 2, 3, 4]


def test_concat_safe_and_overflow():
    a = [1, 2]
    b = [3, 4]
    assert L.concat_safe(a, b, max_len=10) == [1, 2, 3, 4]
    with pytest.raises(OverflowError):
        L.concat_safe(a, b, max_len=3)


def test_edge_cases_empty():
    assert L.squares_lc([]) == []
    assert L.flatten([]) == []
    assert L.unique_preserve_order([]) == []
