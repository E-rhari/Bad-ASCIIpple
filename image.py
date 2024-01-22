from PIL import UnidentifiedImageError
import PIL.Image as pimage
import os
import math
import json


def open_image(path):
    try:
        image = pimage.open(path)
    except FileNotFoundError:
        print("This don't exist stupid")
    except UnidentifiedImageError:
        print("This ain't no image retard")
    return image

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
    resizedImage = resize_image(image, newHeight=CONSOLE_HEIGHT-1)
    width, height = resizedImage.size
    if width > CONSOLE_WIDTH:
        resizedImage = resize_image(image, newWidth=CONSOLE_WIDTH)
    return resizedImage


def turn_gray(image):
    return image.convert("L")


def chooseDensity(createOwn=True):
    print("Choose a density:\n")
    while(True):
        densities = ""
        with open("./densities.json", "r") as densityFile:
            densities = json.load(densityFile)

        for density in densities:
            print(f"\t[{densities.index(density)}] - '{density}'")
        print(f"\t[{len(densities)}] - <Create your own!>")
        
        densityIndex = input("\n∮ R: ")

        try:
            densityIndex = int(densityIndex)
        except ValueError:
            print("Value must be a integer. Please select a valid option:\n")
            continue

        if(densityIndex < len(densities)):
            density = densities[int(densityIndex)]
        elif(densityIndex == len(densities)):
            density = createDensity()
        else:
            print(f"There is no such {densityIndex} density. Please select a valid option:\n")
            continue

        density = list(density)
        density.reverse()
        return density

    
def createDensity():
    newDensity = input("Your new denstity: ")

    densities = ""
    with open("./densities.json", "r") as densityFile:
        densities = json.load(densityFile)
        densities.append(newDensity)
    with open("./densities.json", "w") as densityFile:
        json.dump(densities, densityFile, indent=4)
    
    return newDensity


def pixel_to_ascii(image, density):
    pixels = image.getdata()
    asciiImage = ""
    for pixel in pixels:
        percent = pixel/255
        asciiImage += density[math.floor((len(density)-1) * percent)]

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


def ascii_magic(image, density=""):
    if not density:
        density = chooseDensity()

    resizedImage    = console_sensitive_image_resize(image)
    grayImage       = turn_gray(resizedImage)
    asciiCharacters = pixel_to_ascii(grayImage, density)
    width, height = grayImage.size
    return dispayable_ascii_image(asciiCharacters, width)