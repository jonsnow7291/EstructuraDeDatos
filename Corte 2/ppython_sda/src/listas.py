"""Utilities for list comprehension examples used in the notebook.

Functions are small and easy to test/benchmark.
"""
from typing import Iterable, List, Any, Sequence, Optional


def create_numbers(n: int) -> List[int]:
    """Return list of numbers from 0 to n-1."""
    return list(range(n))


def squares_lc(nums: Iterable[int]) -> List[int]:
    """Return list of squares using list comprehension."""
    return [x * x for x in nums]


def squares_loop(nums: Iterable[int]) -> List[int]:
    """Return list of squares using an explicit loop."""
    out = []
    for x in nums:
        out.append(x * x)
    return out


def filter_even(nums: Iterable[int]) -> List[int]:
    """Return only even numbers using comprehension."""
    return [x for x in nums if x % 2 == 0]


def flatten(nested: Iterable[Iterable[Any]]) -> List[Any]:
    """Flatten one level of nesting."""
    return [y for x in nested for y in x]


def unique_preserve_order(seq: Sequence[Any]) -> List[Any]:
    """Return unique elements preserving first occurrence order."""
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def concat_safe(a: List[Any], b: List[Any], max_len: Optional[int] = None) -> List[Any]:
    """Concatenate two lists; raise OverflowError if length would exceed max_len."""
    res_len = len(a) + len(b)
    if max_len is not None and res_len > max_len:
        raise OverflowError("concatenation would exceed max_len")
    return a + b
