import pytest

from src import suscriptores as S


def test_create_add_remove_and_membership():
    s = S.create_set_from_list(['a@mail.com', 'b@mail.com'])
    assert S.count_subscribers(s) == 2
    S.add_subscriber(s, 'c@mail.com')
    assert S.is_subscriber(s, 'c@mail.com')
    S.remove_subscriber(s, 'b@mail.com')
    assert not S.is_subscriber(s, 'b@mail.com')


def test_union_and_find_duplicates():
    a = S.create_set_from_list(['a', 'b'])
    b = S.create_set_from_list(['b', 'c'])
    u = S.union_sets(a, b)
    assert u == {'a', 'b', 'c'}

    seq = ['x', 'y', 'x', 'z', 'y']
    assert S.find_duplicates(seq) == {'x', 'y'}


def test_safe_add_with_limit_ok_and_overflow():
    s = set(['one'])
    S.safe_add_with_limit(s, 'two', max_len=3)
    assert S.count_subscribers(s) == 2

    with pytest.raises(OverflowError):
        S.safe_add_with_limit(s, 'three', max_len=2)


def test_remove_nonexistent_raises():
    s = set()
    with pytest.raises(KeyError):
        S.remove_subscriber(s, 'nosuch@mail.com')


def test_is_subscriber_false_on_empty():
    s = set()
    assert not S.is_subscriber(s, 'any@mail.com')
