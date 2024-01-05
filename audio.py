import moviepy.editor
from pygame import mixer


def extract_audio(video):
    video.audio.write_audiofile(f"./temp/audio.mp3")


def play_audio(path):
    mixer.init() 
    mixer.music.load(path) 
    mixer.music.set_volume(1)
    mixer.music.play()