import cv2
from pygame import mixer
import image
import PIL
import os
from time import sleep
from time import time


def open_video(path):
    badAppleCapture = cv2.VideoCapture(path)

    if(not badAppleCapture.isOpened()):
        print("That ain't working my dude")
        exit()
    
    return badAppleCapture


def get_fps(video):
    return video.get(5)


def get_total_frames(video):
    return int(video.get(7))
 

def render_video_in_ascii(video):
    fps = get_fps(video)
    totalFrames = get_total_frames(video)

    asciiFrames = []
    for i in range(totalFrames):
        ret, frame = video.read()
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