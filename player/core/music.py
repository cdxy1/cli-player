import subprocess
from pathlib import Path


def play_track(track_path: Path):
    if not isinstance(track_path, Path):
        raise TypeError("Arg is not a path.")

    try:
        subprocess.run(["mpv", "--vo=tct", "--no-audio-display", track_path])
    except FileNotFoundError:
        pass  # File not found
    except subprocess.CalledProcessError:
        pass  # Execution error
