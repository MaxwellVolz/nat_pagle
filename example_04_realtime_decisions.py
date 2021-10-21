"""This is for testing.

Screenshot window capture in real-time.
Reference: https://www.learncodebygaming.com/blog/fast-window-capture
Test Mouse Clicks: https://www.onlinemictest.com/mouse-test/
"""
from time import time
import os

import cv2 as cv
import numpy as np
import pyautogui

hold_to_cast_img = cv.imread('new_world_images/needles/01_hold_to_cast.jpg', cv.IMREAD_UNCHANGED)
cast_release_img = cv.imread('new_world_images/needles/02_cast_release.jpg', cv.IMREAD_UNCHANGED)
hook_img = cv.imread('new_world_images/needles/03_hook.jpg', cv.IMREAD_UNCHANGED)
reel_img = cv.imread('new_world_images/needles/04_reel.jpg', cv.IMREAD_UNCHANGED)
release_img = cv.imread('new_world_images/needles/05_release.jpg', cv.IMREAD_UNCHANGED)
success_img = cv.imread('new_world_images/needles/06_success.jpg', cv.IMREAD_UNCHANGED)

loop_time = time()
current_action = 0

# Action control to prevent mousing up when mouse is up
mouse_up = True


def current_milli_time():
    return round(time() * 1000)


cwd = os.getcwd()
test_start_time = current_milli_time()
current_run_directory = path = os.path.join(cwd, f"test_data\\{test_start_time}")
os.mkdir(current_run_directory)


def get_screenshot():
    screenshot = pyautogui.screenshot()
    # or: screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    return screenshot


def draw_rectangle_on_match(haystack_img, needle_img, needle_name, max_loc):
    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

    cv.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    save_file_name = f'test_data/{test_start_time}/{current_milli_time()}_{needle_name}.jpg'
    # print(f"Saving: {save_file_name}")
    cv.imwrite(save_file_name, haystack_img)


def search_party(haystack_img, needle_img, needle_name="unknown", confidence_threshold=0.8):
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    # print(f'Best match top left position: {max_loc}')
    # print(f'\nBest match confidence:{max_val}')

    if max_val >= confidence_threshold:
        # print(f'Found [{needle_name}]   Confidence: {max_val:3d}')
        find_str = f'Found [{needle_name}]'
        conf_str = f'Confidence: {max_val:3.2f}'
        print(f'{find_str:20} {conf_str}')
        draw_rectangle_on_match(haystack_img, needle_img, needle_name, max_loc)
        # input("Press Enter to continue...")
        return True
    else:
        # print('Needle not found.')
        return False


def set_mouse_up(mouse_is_up):
    if not mouse_is_up:
        pyautogui.mouseUp()
        print("Mouse Up!\n")
        global mouse_up
        mouse_up = True


def set_mouse_down(mouse_is_up):
    if mouse_is_up:
        pyautogui.mouseDown()
        print("Mouse Down...\n")
        global mouse_up
        mouse_up = False


while True:

    screenshot = get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    print(f'FPS {1 / (time() - loop_time)}')
    loop_time = time()

    # Check

    if current_action == 0:
        # TODO: Start timer for time_between_casts, break if not enough time
        if search_party(screenshot, hold_to_cast_img, "casting"):
            set_mouse_down(mouse_up)

            # TODO: Start timer that will auto release after X seconds
            current_action = 1

    if current_action == 1:
        if search_party(screenshot, cast_release_img, "release"):
            set_mouse_up(mouse_up)
            current_action = 2

    if current_action == 2:
        if search_party(screenshot, hook_img, "hook"):
            set_mouse_down(mouse_up)
            current_action = 3

    if current_action == 3:
        # Check if caught
        if search_party(screenshot, success_img, "catch"):
            set_mouse_up(mouse_up)
            current_action = 0

        # Check if need to back off
        if search_party(screenshot, release_img, "spooling"):
            set_mouse_up(mouse_up)
            current_action = 4

    if current_action == 4:
        # Check if caught
        if search_party(screenshot, success_img, "catch"):
            set_mouse_up(mouse_up)
            current_action = 0

        if search_party(screenshot, reel_img, "reeling"):
            set_mouse_down(mouse_up)
            current_action = 3


    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
