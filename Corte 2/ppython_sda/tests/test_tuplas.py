import pytest

from src import tuplas as tu


def test_create_and_sum_tuple():
    t = tu.create_tuple([1, 2, 3])
    assert isinstance(t, tuple)
    assert tu.sum_tuple(t) == 6


def test_index_of_and_count():
    t = (10, 20, 10, 30)
    assert tu.index_of(t, 20) == 1
    assert tu.index_of(t, 99) == -1
    assert tu.count_occurrences(t, 10) == 2


def test_replace_in_tuple_positive_and_negative_index():
    t = (1, 2, 3)
    t2 = tu.replace_in_tuple(t, 1, 99)
    assert t2 == (1, 99, 3)

    # negative index replacement
    t3 = tu.replace_in_tuple(t, -1, 42)
    assert t3 == (1, 2, 42)


def test_concat_tuples_safe_overflow_and_ok():
    a = (1, 2)
    b = (3, 4, 5)
    # ok when max_len large enough
    assert tu.concat_tuples_safe(a, b, max_len=10) == (1, 2, 3, 4, 5)

    # overflow when max_len smaller than result length
    with pytest.raises(OverflowError):
        tu.concat_tuples_safe(a, b, max_len=4)


def test_is_singleton_and_tuple_to_list():
    assert tu.is_singleton((1,))
    assert not tu.is_singleton(())
    assert tu.tuple_to_list((1, 2)) == [1, 2]
