"""Utilities for working with tuples used in course examples.

Provides small helper functions so we can write unit tests and benchmarks.
"""
from typing import Iterable, Tuple, Any, List, Optional


def create_tuple(iterable: Iterable) -> Tuple:
    """Create a tuple from an iterable."""
    return tuple(iterable)


def sum_tuple(t: Tuple) -> float:
    """Return the sum of numeric elements in a tuple.

    Non-numeric elements raise a TypeError from the built-in sum.
    """
    return sum(t)


def index_of(t: Tuple, value: Any) -> int:
    """Return index of value in tuple or -1 if not found."""
    try:
        return t.index(value)
    except ValueError:
        return -1


def replace_in_tuple(t: Tuple, index: int, value: Any) -> Tuple:
    """Return a new tuple where the element at `index` is replaced by `value`.

    Raises IndexError for invalid indices (to mirror list behaviour).
    """
    if index < 0:
        # support negative indices similar to list/tuple behaviour
        real_index = len(t) + index
    else:
        real_index = index

    if real_index < 0 or real_index >= len(t):
        raise IndexError("tuple index out of range")

    lst = list(t)
    lst[real_index] = value
    return tuple(lst)


def tuple_to_list(t: Tuple) -> List:
    """Convert tuple to list (shallow copy)."""
    return list(t)


def concat_tuples_safe(a: Tuple, b: Tuple, max_len: Optional[int] = None) -> Tuple:
    """Concatenate two tuples. If max_len is provided and the result would
    exceed max_len, raise OverflowError. This demonstrates handling an
    explicit 'overflow' / capacity limit.
    """
    result_len = len(a) + len(b)
    if max_len is not None and result_len > max_len:
        raise OverflowError(f"concatenation would exceed max_len={max_len}")
    return a + b


def is_singleton(t: Tuple) -> bool:
    """Return True if tuple contains exactly one element."""
    return len(t) == 1


def count_occurrences(t: Tuple, value: Any) -> int:
    """Return count of `value` in tuple."""
    return t.count(value)
