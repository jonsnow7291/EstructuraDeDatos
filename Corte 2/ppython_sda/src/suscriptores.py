"""Utilities to manage subscriber lists backed by Python sets.

Provides helper functions for tests and benchmarks.
"""
from typing import Iterable, Set, Optional


def create_set_from_list(items: Iterable[str]) -> Set[str]:
    return set(items)


def add_subscriber(s: Set[str], email: str) -> None:
    s.add(email)


def remove_subscriber(s: Set[str], email: str) -> None:
    s.remove(email)


def is_subscriber(s: Set[str], email: str) -> bool:
    return email in s


def count_subscribers(s: Set[str]) -> int:
    return len(s)


def union_sets(a: Set[str], b: Set[str]) -> Set[str]:
    return a.union(b)


def find_duplicates(seq: Iterable[str]) -> Set[str]:
    seen = set()
    dup = set()
    for x in seq:
        if x in seen:
            dup.add(x)
        else:
            seen.add(x)
    return dup


def safe_add_with_limit(s: Set[str], email: str, max_len: Optional[int] = None) -> None:
    """Add email to set but if max_len provided and addition would exceed it,
    raise OverflowError.
    """
    if max_len is not None:
        # if email already present, size doesn't increase
        if email not in s and len(s) + 1 > max_len:
            raise OverflowError("adding subscriber would exceed max_len")
    s.add(email)
