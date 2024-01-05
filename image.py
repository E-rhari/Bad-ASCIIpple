import PIL.Image as pimage
from PIL import UnidentifiedImageError
import os
import math


def resize_image(image, newWidth=None, newHeight=None):
    width, height = image.size
    height *= 0.7
    ratio = height/width


    if newWidth == None and newHeight == None:
        print("You need at least one measurement of the image for resizing.")
        raise
    if newWidth  == None:
        newWidth = int(newHeight / ratio)
    if newHeight == None:
        newHeight = int(newWidth * ratio)

    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage


def console_sensitive_image_resize(image):
    CONSOLE_SIZE = os.get_terminal_size()
    CONSOLE_WIDTH = CONSOLE_SIZE[0]
    CONSOLE_HEIGHT = CONSOLE_SIZE[1]

    # return resize_image(image, newWidth=CONSOLE_WIDTH)
    return resize_image(image, newHeight=CONSOLE_HEIGHT-1)


def turn_gray(image):
    return image.convert("L")


def pixel_to_ascii(image):
    # DENSITY = list('Ñ@#W$9876543210?!abc;:+=-,. ')
    # DENSITY = list('@#$?!abc;:-,. ')
    DENSITY = list('@%#w*-. ')
    # print(DENSITY)
    # DENSITY = list("a@ ")
    DENSITY.reverse()
    pixels = image.getdata()
    asciiImage = ""
    for pixel in pixels:
        percent = pixel/255
        asciiImage += DENSITY[math.floor((len(DENSITY)-1) * percent)]
        # print(f'{pixel} - {percent}% - {(math.floor(len(DENSITY) -1) * percent)}')

    return asciiImage


def dispayable_ascii_image(asciiCharacters, width):
    asciiImage = ""
    caretPosition = 1
    for asciiCharacter in asciiCharacters:
        asciiImage += asciiCharacter
        if caretPosition < width:
            caretPosition += 1
        else:
            asciiImage += "\n"
            caretPosition = 1
    return asciiImage


def ascii_magic(image):
    resizedImage    = console_sensitive_image_resize(image)
    grayImage       = turn_gray(resizedImage)
    asciiCharacters = pixel_to_ascii(grayImage)
    width, height = grayImage.size
    return dispayable_ascii_image(asciiCharacters, width)


def main():
    imagePath = input("Insert the image path: ")
    try:
        image = pimage.open(imagePath)
        print(ascii_magic(image))
    except FileNotFoundError:
        print("This don't exist stupid")
    except UnidentifiedImageError:
        print("This ain't no image retard")


# main()