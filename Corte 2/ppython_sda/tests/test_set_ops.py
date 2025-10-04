import pytest
from ppython_sda.src.set_ops import (
    create_set,
    add_element,
    remove_element,
    contains,
    union_sets,
    intersection_sets,
    difference_sets,
    size,
    BadHash,
)


def test_create_and_add():
    s = create_set()
    add_element(s, 1)
    add_element(s, 1)  # duplicado no cambia tamaño
    assert size(s) == 1 and contains(s, 1)


def test_remove_element_success():
    s = create_set([1,2,3])
    remove_element(s, 2)
    assert not contains(s, 2) and size(s) == 2


def test_remove_element_missing_raises():
    s = create_set([1])
    with pytest.raises(KeyError):
        remove_element(s, 99)


def test_union_and_intersection():
    a = create_set([1,2,3])
    b = create_set([3,4])
    assert union_sets(a,b) == {1,2,3,4}
    assert intersection_sets(a,b) == {3}


def test_difference():
    a = create_set([1,2,3])
    b = create_set([2])
    assert difference_sets(a,b) == {1,3}


def test_bad_hash_collision_behavior():
    s = create_set()
    elems = [BadHash(i) for i in range(50)]
    for e in elems:
        add_element(s, e)
    # Todos tienen el mismo hash pero deben coexistir sin pérdida
    assert size(s) == 50
    assert all(contains(s, e) for e in elems)


def test_bad_hash_equality():
    a = BadHash(1)
    b = BadHash(1)
    c = BadHash(2)
    s = create_set([a])
    assert contains(s, b)  # mismo valor -> igualdad
    assert not contains(s, c)
