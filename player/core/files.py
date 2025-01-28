from typing import Dict
from pathlib import Path

import click

from .music import play_track

DEFAULT_DIR_PATH = Path.home() / "Music" / "cliPlayer"


def init_main_dir():
    if not DEFAULT_DIR_PATH.exists():
        DEFAULT_DIR_PATH.mkdir()
    else:
        pass


def check_main_dir():
    return DEFAULT_DIR_PATH.exists()


def make_playlist_dir(name: str):
    if isinstance(name, str):
        Path(DEFAULT_DIR_PATH / f"{name}").mkdir()


def playlists_list():
    pl_dict = {}

    for pl in DEFAULT_DIR_PATH.iterdir():
        pl_dict[pl.name] = {pl}

    return pl_dict


def select_pl_dir(pl_dict: Dict[str, Path], pl_num: int):
    pl_dir = [list(i) for i in pl_dict.values()][pl_num]

    for track in pl_dir[0].iterdir():
        click.clear()
        play_track(track)
