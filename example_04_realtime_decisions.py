"""This is for testing.

Screenshot window capture in real-time.
Reference: https://www.learncodebygaming.com/blog/fast-window-capture
Test Mouse Clicks: https://www.onlinemictest.com/mouse-test/
"""
import time
import os

import cv2 as cv
import numpy as np
import pyautogui

hold_to_cast_img = cv.imread('new_world_images/needles/01_hold_to_cast_2.jpg', cv.IMREAD_UNCHANGED)
cast_release_img = cv.imread('new_world_images/needles/02_cast_release_2.jpg', cv.IMREAD_UNCHANGED)
hook_loc_img =  cv.imread('new_world_images/needles/02_hook_loc.jpg', cv.IMREAD_UNCHANGED)
hook_img = cv.imread('new_world_images/needles/03_hook_2.jpg', cv.IMREAD_UNCHANGED)
reel_img = cv.imread('new_world_images/needles/04_reel_2.jpg', cv.IMREAD_UNCHANGED)
release_img = cv.imread('new_world_images/needles/05_release_2.jpg', cv.IMREAD_UNCHANGED)
success_img = cv.imread('new_world_images/needles/06_success_2.jpg', cv.IMREAD_UNCHANGED)

loop_time = time.time()
current_action = 0
hook_top_left = 0
hook_top_right = 0

# Action control to prevent mousing up when mouse is up
mouse_up = True


def current_milli_time():
    return round(time.time() * 1000)


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


def search_party(haystack_img, needle_img, needle_name="unknown", confidence_threshold=0.85):
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


def search_party_gps(haystack_img, needle_img, needle_name="unknown", confidence_threshold=0.85):
    max_val = 0

    # print(f'Best match top left position: {max_loc}')
    # print(f'\nBest match confidence:{max_val}')
    while max_val < confidence_threshold:
        screenshot = get_screenshot()
        result = cv.matchTemplate(screenshot, needle_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]

    top_left = list(max_loc)
    search_area_top_left = tuple([top_left[0]-50, top_left[1]-50])
    bottom_right = (top_left[0] + needle_w + 20, top_left[1] + needle_h + 50)

    cv.rectangle(haystack_img, search_area_top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    save_file_name = f'test_data/{test_start_time}/{current_milli_time()}_{needle_name}.jpg'
    # print(f"Saving: {save_file_name}")
    cv.imwrite(save_file_name, haystack_img)

    return list(search_area_top_left), list(bottom_right)


def search_party_area(top_left, bottom_right, needle_img, needle_name="unknown", confidence_threshold=0.85,
                      max_attempts=100):
    attempts = 0
    max_val = 0
    # loop_time_area_search = time.time()
    # time.sleep(0.01)

    while max_val < confidence_threshold or attempts > max_attempts:
        attempts += 1
        # print(f'FPS {1 / (time.time() - loop_time_area_search)}')
        # loop_time_area_search = time.time()

        screenshot = pyautogui.screenshot(region=(top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
        # or: screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

        result = cv.matchTemplate(screenshot, needle_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        if max_val >= confidence_threshold:
            # print(f'Found [{needle_name}]   Confidence: {max_val:3d}')
            find_str = f'Found [{needle_name}]'
            conf_str = f'Confidence: {max_val:3.2f}'
            print(f'{find_str:20} {conf_str}')
            draw_rectangle_on_match(screenshot, needle_img, needle_name, max_loc)
            # input("Press Enter to continue...")
            return True
        else:
            # print('Needle not found.')
            return False

    return True


def set_mouse_up(mouse_is_up):
    if not mouse_is_up:
        pyautogui.mouseUp()
        print("Mouse Up!\n")
        global mouse_up
        mouse_up = True


def set_mouse_down(mouse_is_up):
    if mouse_is_up:
        pyautogui.mouseDown()
        # print("Mouse Down...\n")
        global mouse_up
        mouse_up = False


while True:

    screenshot = get_screenshot()

    cv.imshow('Computer Vision', screenshot)

    # print(f'FPS {1 / (time() - loop_time)}')
    loop_time = time.time()

    # Check

    if current_action == 0:
        # TODO: Start timer for time_between_casts, break if not enough time
        if search_party(screenshot, hold_to_cast_img, "casting"):
            set_mouse_down(mouse_up)

            release_time = round(np.random.uniform(1.3, 1.6), 3)
            print("release time:", release_time)
            time.sleep(release_time)
            set_mouse_up(mouse_up)

            time.sleep(1)

            hook_top_left, hook_top_right = search_party_gps(screenshot, hook_loc_img, "hook_location")

            # TODO: Start timer that will auto release after X seconds
            current_action = 2

    if current_action == 2:
        if search_party_area(hook_top_left, hook_top_right, hook_img, "hook"):
            set_mouse_down(mouse_up)
            current_action = 3
            print("search_party_area completed.")

    if current_action == 3:
        # Check if caught
        if search_party(screenshot, hold_to_cast_img, "casting"):
            set_mouse_up(mouse_up)
            current_action = 0

        # Check if need to back off
        if search_party_area(hook_top_left, hook_top_right, release_img, "spooling", 0.7):
            set_mouse_up(mouse_up)
            current_action = 4

    if current_action == 4:
        # Check if caught
        if search_party(screenshot, hold_to_cast_img, "casting"):
            set_mouse_up(mouse_up)
            current_action = 0

        if search_party_area(hook_top_left, hook_top_right, reel_img, "reeling"):
            set_mouse_down(mouse_up)
            current_action = 3

    if cv.waitKey(1) == ord('r'):
        current_action = 0

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
