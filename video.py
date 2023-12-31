import cv2
import image

badAppleCapture = cv2.VideoCapture('Bad_Apple!!.mp4')

if(not badAppleCapture.isOpened()):
    print("That ain't working my dude")
    exit()

fps = badAppleCapture.get(5)
print(fps)