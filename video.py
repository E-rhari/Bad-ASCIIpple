import moviepy.editor
from pygame import mixer
import image
import PIL
import os
from time import time


def open_video(path):
    try:
        capture = moviepy.editor.VideoFileClip(path)
    except IOError:
        print(f"File {path} not found!")
        exit()

    return capture


def get_fps(video):
    return video.fps


def get_total_frames(video):
    return int(video.fps * video.duration)


def render_video_in_ascii(video):
    totalFrames = get_total_frames(video)
    videoFrames = video.iter_frames()

    asciiFrames = []
    for frame in videoFrames:
        pilFrame = PIL.Image.fromarray(frame)
        asciiFrames.append(image.ascii_magic(pilFrame))
    
    return asciiFrames


def play_song(path):
    mixer.init() 
    mixer.music.load(path) 
    mixer.music.set_volume(1)
    mixer.music.play()


def play_ascii_video(asciiFrames, fps):
    startTime = time()
    for asciiFrame in asciiFrames:
        for character in asciiFrame:
            print(character, end="")
            if time() - startTime >= (1/fps):
                break
        while time() - startTime < (1/fps):
            continue
        startTime = time()
        os.system('cls')