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


def test_safe_remove_and_remove_all_and_delete_slice():
    lst = [1, 2, 3, 2, 4, 2]
    # safe_remove returns True when present
    assert lo.safe_remove(lst, 2) is True
    # remove_all removes all remaining 2s
    removed = lo.remove_all(lst, 2)
    assert removed == 2
    assert 2 not in lst
    # delete_slice: remove first two elements
    lo.delete_slice(lst, 0, 2)
    # list should be shorter now
    assert len(lst) == 1


def test_iteration_helpers():
    lst = [1, 2, 2, 3]
    assert lo.iterate_apply(lst, lambda x: x * 2) == [2, 4, 4, 6]
    assert lo.enumerate_list(['a', 'b']) == [(0, 'a'), (1, 'b')]
    assert lo.find_duplicates(lst) == {2}
    assert lo.filter_list(lst, lambda x: x % 2 == 1) == [1, 3]
    # safe_modify_by_copy should modify in-place without skipping
    t = [1, 2, 3]
    lo.safe_modify_by_copy(t, lambda x: x + 1)
    assert t == [2, 3, 4]
