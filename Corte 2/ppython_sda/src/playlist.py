"""Helpers for a simple playlist (list of song titles).

Used by the Notebook `05-Playlist-parte2-UP.ipynb` as an example module.
"""
from typing import List, Optional
import random


class PlaylistFullError(Exception):
    pass


def create_playlist(items: Optional[List[str]] = None) -> List[str]:
    return list(items) if items else []


def add_song(pl: List[str], song: str, max_capacity: Optional[int] = None) -> None:
    if max_capacity is not None and len(pl) >= max_capacity:
        raise PlaylistFullError('playlist reached max capacity')
    pl.append(song)


def remove_song(pl: List[str], song: str) -> bool:
    try:
        pl.remove(song)
        return True
    except ValueError:
        return False


def move_song(pl: List[str], old_index: int, new_index: int) -> None:
    song = pl.pop(old_index)
    pl.insert(new_index, song)


def shuffle_playlist(pl: List[str]) -> None:
    random.shuffle(pl)


def find_song(pl: List[str], song: str) -> Optional[int]:
    try:
        return pl.index(song)
    except ValueError:
        return None


def sort_playlist(pl: List[str], reverse: bool = False) -> None:
    pl.sort(reverse=reverse)
