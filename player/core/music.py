from pydub import AudioSegment
from pydub.playback import play

mp3 = AudioSegment.from_mp3("/home/cdxy/Development/Python-projects/cliPlayer/asap.mp3")

test_play = lambda: play(mp3)
