from ppython_sda.src import playlist as pl
import pytest


def test_create_and_add_find():
    p = pl.create_playlist()
    pl.add_song(p, 'Song A')
    pl.add_song(p, 'Song B')
    assert pl.find_song(p, 'Song A') == 0
    assert pl.find_song(p, 'Song Z') is None


def test_remove_and_move():
    p = pl.create_playlist(['A', 'B', 'C'])
    assert pl.remove_song(p, 'B') is True
    assert 'B' not in p
    pl.move_song(p, 1, 0)
    assert p[0] == 'C'


def test_shuffle_and_sort():
    p = pl.create_playlist(['b', 'a', 'c'])
    pl.sort_playlist(p)
    assert p == ['a', 'b', 'c']
    pl.shuffle_playlist(p)  # nondeterministic; just ensure no error


def test_capacity_error():
    p = pl.create_playlist(['x'])
    with pytest.raises(pl.PlaylistFullError):
        pl.add_song(p, 'y', max_capacity=1)
