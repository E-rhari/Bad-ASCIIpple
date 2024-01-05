from video import *
from audio import *


print("1/4 - Opening video...")
badAppleVideo = open_video('Bad_Apple!!.mp4')

print("2/4 - Extracting audio...")
extract_audio(badAppleVideo)

print("3/4 - Converting to ASCII...")
asciiFrames = render_video_in_ascii(badAppleVideo)

print("4/4 - Starting song...")
play_audio('./temp/audio.mp3')

play_ascii_video(asciiFrames, get_fps(badAppleVideo))
