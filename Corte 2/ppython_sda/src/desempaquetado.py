"""Utilities for tuple unpacking examples and safe unpacking helpers."""
from typing import Iterable, Tuple, Any, List, NamedTuple, Optional
from collections import namedtuple


def unpack_product(product: Tuple) -> Tuple[str, str, float]:
    """Unpack product tuple of the form (id, description, price).

    Raises ValueError if the tuple doesn't match the expected size.
    """
    if len(product) != 3:
        raise ValueError("product tuple must have exactly 3 elements")
    id_, description, price = product
    return id_, description, price


def safe_unpack(seq: Iterable, expected: int, default: Optional[Any] = None) -> Tuple:
    """Return a tuple of length `expected` filled with items from seq and
    `default` for missing values. If seq has more than expected items, extra
    items will be ignored.
    """
    lst = list(seq)
    if len(lst) >= expected:
        return tuple(lst[:expected])
    # pad with defaults
    return tuple(lst + [default] * (expected - len(lst)))


def unpack_with_star(seq: Iterable) -> Tuple[Any, List[Any], Any]:
    """Example of unpacking with star: returns (first, middle_list, last).

    If fewer than 2 elements are provided, raises ValueError.
    """
    lst = list(seq)
    if len(lst) < 2:
        raise ValueError("sequence must contain at least 2 elements")
    first, *middle, last = lst
    return first, middle, last


def to_namedtuple(name: str, t: Tuple) -> NamedTuple:
    """Convert a tuple to a namedtuple with fields f0, f1, ... (length-based).

    Example: to_namedtuple('P', ('a','b')) -> P(f0='a', f1='b')
    """
    fields = [f"f{i}" for i in range(len(t))]
    NT = namedtuple(name, fields)
    return NT(*t)
