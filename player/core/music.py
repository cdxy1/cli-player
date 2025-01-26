from pathlib import Path

from pydub import AudioSegment
from pydub.playback import play


def start_playlist(track_path: Path):
    str_track = str(track_path)
    if "mp3" in str_track:
        track = AudioSegment.from_mp3(str_track)
    elif "wav" in str_track:
        track = AudioSegment.from_wav(str_track)

    try:
        play(track)
    finally:
        pass
