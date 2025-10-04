import pytest

from src import desempaquetado as ds


def test_unpack_product_ok():
    prod = ('P001', 'Camisa', 20.0)
    id_, desc, price = ds.unpack_product(prod)
    assert id_ == 'P001' and desc == 'Camisa' and price == 20.0


def test_unpack_product_error():
    with pytest.raises(ValueError):
        ds.unpack_product(('P001', 'Camisa'))


def test_safe_unpack_padding_and_truncation():
    s = [1]
    a, b, c = ds.safe_unpack(s, 3, default=0)
    assert (a, b, c) == (1, 0, 0)

    # truncation
    a, b = ds.safe_unpack([1, 2, 3], 2)
    assert (a, b) == (1, 2)


def test_unpack_with_star_normal_and_error():
    first, middle, last = ds.unpack_with_star([1, 2, 3, 4])
    assert first == 1 and middle == [2, 3] and last == 4

    with pytest.raises(ValueError):
        ds.unpack_with_star([1])


def test_to_namedtuple_fields_and_values():
    nt = ds.to_namedtuple('P', ('a', 'b'))
    assert hasattr(nt, 'f0') and hasattr(nt, 'f1')
    assert nt.f0 == 'a' and nt.f1 == 'b'
