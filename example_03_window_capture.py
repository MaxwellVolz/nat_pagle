"""This is for testing.

Live image capturing using screenshot data.
"""

import cv2 as cv
import numpy as np
import pyautogui

image_collection = [
    ['new_world_images/haystacks/01_hold_to_cast.jpg', 'new_world_images/needles/01_hold_to_cast.jpg'],
    ['new_world_images/haystacks/02_cast_release.jpg', 'new_world_images/needles/02_cast_release.jpg'],
    ['new_world_images/haystacks/03_hook.jpg', 'new_world_images/needles/03_hook.jpg'],
    ['new_world_images/haystacks/04_release.jpg', 'new_world_images/needles/04_release.jpg'],
    ['new_world_images/haystacks/05_reel.jpg', 'new_world_images/needles/05_reel.jpg'],
    ['new_world_images/haystacks/06_success.jpg', 'new_world_images/needles/06_success.jpg'],
]

def get_screenshot():
    screenshot = pyautogui.screenshot('my_screenshot.png')
    # or: screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    return screenshot


screenshot = get_screenshot()


#
# while(True):
#
#     screenshot = get_screenshot()
#
#     cv.imshow('Computer Vision', screenshot)
#
#     # press 'q' with the output window focused to exit.
#     # waits 1 ms every loop to process key presses
#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllWindows()
#         break
