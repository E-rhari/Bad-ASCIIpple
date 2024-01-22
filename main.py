from video import *
from audio import *


def bad_apple():
    ascii_video_magic("Bad_Apple!!.mp4")


def video():
    videoPath = input("Insert relative path to video: ")
    ascii_video_magic(videoPath)


def image():
    imagePath = input("Insert relative path to image: ")
    imageFile = open_image(imagePath)
    print(ascii_magic(imageFile))


def help():
    for command, explanation in COMMAND_LIST.items():
        print(f"- {command}\t{explanation}")
    print("\n")


COMMAND_LIST = {"bad_apple":"Plays Bad Apple as ASCII",
                "video":    "\tPlays a video in terminal as ASCII",
                "image":    "\tDisplays an image in terminal as ASCII",
                "exit":     "\tExits the application",
                "help":     "\tProvides help concerning Bad-ASCIIpple commands.",
                }


print(ascii_magic(open_image("splash.png")), end="")
help()

userCommand = ""
commandFunction = None

while userCommand != "exit":
    userCommand = input("∮ ")
    userCommand = userCommand.lower()

    if userCommand == "" or userCommand == "exit":
        continue
    elif userCommand in COMMAND_LIST.keys():
        exec(f"commandFunction = {userCommand}")
        commandFunction()
        continue
    else:
        print("Error: Command not found\n")