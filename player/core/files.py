from pathlib import Path
from typing import Dict


from .music import play_track

DEFAULT_DIR_PATH = Path.home() / "Music" / "cliPlayer"


def init_main_dir(path: str):
    if not DEFAULT_DIR_PATH.exists():
        DEFAULT_DIR_PATH.mkdir()
    elif path != "":
        Path(path).mkdir()
    else:
        pass


def check_main_dir():
    return True if DEFAULT_DIR_PATH.exists() else False


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
        play_track(track)
