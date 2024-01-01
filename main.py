from video import *

badAppleVideo = open_video('Bad_Apple!!.mp4')
asciiFrames = render_video_in_ascii(badAppleVideo)

play_song('Bad_Apple.wav')
play_ascii_video(asciiFrames, get_fps(badAppleVideo))
