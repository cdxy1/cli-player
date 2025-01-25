from pathlib import Path
from typing import Optional

DEFAULT_DIR_PATH = Path.home() / "Music" / "cliPlayer"


def init_main_dir(path: Optional[str | None] = None):
    if not DEFAULT_DIR_PATH.exists() and path is None:
        DEFAULT_DIR_PATH.mkdir()
    elif path is not None:
        Path(path).mkdir()


def make_playlist_dir(name: str):
    if isinstance(name, str):
        Path(DEFAULT_DIR_PATH / f"{name}").mkdir()


def playlists_list():
    pl_dict = {}

    for pl in DEFAULT_DIR_PATH.iterdir():
        pl_dict[pl.name] = {pl}

    return pl_dict


def select_playlist():
    pass


print(playlists_list())
