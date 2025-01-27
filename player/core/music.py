import subprocess
from pathlib import Path


def play_track(track_path: Path):
    if not isinstance(track_path, Path):
        raise TypeError("Arg is not a path.")

    subprocess.run(["mpv", "--no-audio-display", track_path])
