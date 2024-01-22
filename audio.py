import moviepy.editor
from pygame import mixer
import asyncio


def extract_audio(video):
    video.audio.write_audiofile(f"./temp/audio.mp3")


async def play_audio(path):
    mixer.init() 
    mixer.music.load(path) 
    mixer.music.set_volume(1)
    await asyncio.sleep(4)
    mixer.music.play()