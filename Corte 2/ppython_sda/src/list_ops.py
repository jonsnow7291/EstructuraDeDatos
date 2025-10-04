"""Utility functions for list examples used in the notebook and tests.

This module keeps implementations simple and explicit for teaching purposes.
"""
from typing import Any, List, Optional, Callable


def create_list(n: int) -> List[int]:
    """Create a list with integers from 0 to n-1. If n < 0 returns empty list."""
    if n <= 0:
        return []
    return list(range(n))


def append_element(lst: List[Any], value: Any) -> None:
    """Append value to end of list."""
    lst.append(value)


def safe_insert(lst: List[Any], value: Any, idx: int = 0) -> None:
    """Insert value at idx. If idx out of bounds, insert at end.

    This avoids raising IndexError for very large positive indices.
    Negative indices are handled by Python's native behavior.
    """
    if idx >= len(lst):
        lst.append(value)
    else:
        lst.insert(idx, value)


def pop_element(lst: List[Any], idx: int = -1) -> Any:
    """Pop element at idx (default last). Raises IndexError if list empty."""
    return lst.pop(idx)


def access_index(lst: List[Any], idx: int) -> Any:
    """Return element at idx. Raises IndexError if out of range."""
    return lst[idx]


def find_value(lst: List[Any], value: Any) -> Optional[int]:
    """Return first index of value or None if not found."""
    try:
        return lst.index(value)
    except ValueError:
        return None


def reverse_list(lst: List[Any]) -> List[Any]:
    """Return a new list with reversed contents."""
    return lst[::-1]


def map_increment(lst: List[int], delta: int = 1) -> List[int]:
    """Return a new list where each element is incremented by delta."""
    return [x + delta for x in lst]


class MaxCapacityError(Exception):
    """Raised when attempting to append beyond a configured maximum capacity."""


def append_with_limit(lst: List[Any], value: Any, max_capacity: Optional[int] = None) -> None:
    """Append value to list unless it would exceed max_capacity.

    If max_capacity is None, behaves like normal append. If list length is
    already >= max_capacity, raises MaxCapacityError.
    """
    if max_capacity is None:
        lst.append(value)
        return
    if len(lst) >= max_capacity:
        raise MaxCapacityError(f'list reached max capacity {max_capacity}')
    lst.append(value)
