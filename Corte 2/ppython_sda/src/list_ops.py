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


def safe_remove(lst: List[Any], value: Any) -> bool:
    """Remove first occurrence of value. Returns True if removed, False if not found.

    This wraps `list.remove` to avoid raising ValueError when value is absent.
    """
    try:
        lst.remove(value)
        return True
    except ValueError:
        return False


def remove_all(lst: List[Any], value: Any) -> int:
    """Remove all occurrences of value from list in-place. Returns number removed."""
    count = 0
    # iterate over a copy to avoid skipping
    for x in lst[:]:
        if x == value:
            lst.remove(x)
            count += 1
    return count


def delete_slice(lst: List[Any], start: int, end: int) -> None:
    """Delete slice lst[start:end] in-place (like del lst[start:end])."""
    del lst[start:end]


def iterate_apply(lst: List[Any], func: Callable[[Any], Any]) -> List[Any]:
    """Return a new list where func has been applied to each element (safe, non-mutating)."""
    return [func(x) for x in lst]


def enumerate_list(lst: List[Any]) -> List[tuple]:
    """Return a list of (index, value) pairs for the input list."""
    return list(enumerate(lst))


def find_duplicates(lst: List[Any]) -> set:
    """Return a set of duplicated values found in the list."""
    seen = set()
    dups = set()
    for x in lst:
        if x in seen:
            dups.add(x)
        else:
            seen.add(x)
    return dups


def filter_list(lst: List[Any], predicate: Callable[[Any], bool]) -> List[Any]:
    """Return a new list containing items where predicate(item) is True."""
    return [x for x in lst if predicate(x)]


def safe_modify_by_copy(lst: List[Any], func: Callable[[Any], Any]) -> None:
    """Modify the list in-place by applying func to each element, iterating over a copy.

    This avoids problems when modifying the list structure during iteration.
    """
    for i, v in enumerate(list(lst)):
        lst[i] = func(v)
