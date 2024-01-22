import moviepy.editor
from image import *
from audio import *
import PIL
import os
from time import time
import asyncio


def open_video(path):
    try:
        capture = moviepy.editor.VideoFileClip(path)
    except IOError:
        print(f"File {path} not found!")
        exit()

    return capture


def get_fps(video):
    return video.fps


def render_video_as_ascii(video, density):
    videoFrames = video.iter_frames()

    asciiFrames = []
    for frame in videoFrames:
        pilFrame = PIL.Image.fromarray(frame)
        asciiFrames.append(ascii_magic(pilFrame, density))
    
    return asciiFrames


def play_ascii_video(asciiFrames, fps):
    startTime = time()
    for asciiFrame in asciiFrames:
        for character in asciiFrame:
            if time() - startTime >= (1/fps):
                break
            print(character, end="")
        while time() - startTime < (1/fps):
            continue
        startTime = time()
        os.system('cls')


def ascii_video_magic(path, density=""):
    if not density:
        density = chooseDensity()

    print("1/4 - Opening video...")
    video = open_video(path)

    print("2/4 - Extracting audio...")
    extract_audio(video)

    print("3/4 - Converting to ASCII...")
    asciiFrames = render_video_as_ascii(video, density)

    print("4/4 - Starting song...")
    asyncio.run(play_audio('./temp/audio.mp3'))

    play_ascii_video(asciiFrames, get_fps(video))