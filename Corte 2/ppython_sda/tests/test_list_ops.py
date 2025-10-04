import pytest
from ppython_sda.src import list_ops as lo


def test_create_list_positive():
    lst = lo.create_list(5)
    assert lst == [0, 1, 2, 3, 4]


def test_create_list_non_positive():
    assert lo.create_list(0) == []
    assert lo.create_list(-3) == []


def test_append_and_find():
    lst = lo.create_list(2)
    lo.append_element(lst, 99)
    assert lo.find_value(lst, 99) == 2


def test_safe_insert_out_of_range():
    lst = lo.create_list(3)
    lo.safe_insert(lst, 7, idx=100)
    assert lst[-1] == 7


def test_pop_and_access():
    lst = lo.create_list(3)
    val = lo.pop_element(lst)
    assert val == 2
    with pytest.raises(IndexError):
        # popping from empty list should raise
        lo.pop_element([])


def test_reverse_and_map():
    lst = [1, 2, 3]
    assert lo.reverse_list(lst) == [3, 2, 1]
    assert lo.map_increment(lst, 2) == [3, 4, 5]


def test_append_with_limit_ok_and_overflow():
    lst = lo.create_list(2)
    lo.append_with_limit(lst, 'a', max_capacity=3)
    assert lst[-1] == 'a'
    with pytest.raises(lo.MaxCapacityError):
        # current len is 3, adding another should raise
        lo.append_with_limit(lst, 'b', max_capacity=3)
