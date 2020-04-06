import cv2
import numpy as np
from PIL import Image, ImageGrab
from win32.win32gui import GetWindowText, GetForegroundWindow, GetWindowRect, GetCursorPos, GetCursorInfo
def GetScreen():
    rect = GetWindowRect(GetForegroundWindow())
    fish_area = (0, rect[3]/2, rect[2], int(rect[3]*0.778))

    img = ImageGrab.grab(fish_area)
    img = np.array(img)

    return img, fish_area


def MakeFrames(img):
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    return frame, frame_hsv


def MaskFrame(frame_hsv):
    h_min = np.array((0, 0, 253), np.uint8)
    h_max = np.array((255, 0, 255), np.uint8)

    return cv2.inRange(frame_hsv, h_min, h_max)

def CatchArea():
    img, fish_area = GetScreen()
    frame, frame_hsv = MakeFrames(img)
    mask = MaskFrame(frame_hsv)
    moments = cv2.moments(mask, 1)
    
    #Integrale änderungen
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    return dM01, dM10, dArea, fish_area