"""This is for testing.

Screenshot window capture in real-time.
Reference: https://www.learncodebygaming.com/blog/fast-window-capture
"""
from time import time

import cv2 as cv
import numpy as np
import pyautogui


def get_screenshot():
    screenshot = pyautogui.screenshot()
    # or: screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    return screenshot

loop_time = time()
while (True):

    screenshot = get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    print(f'FPS {1 / (time() - loop_time)}')
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
