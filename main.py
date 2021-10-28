"""Pat Nagle - new world fishing man

Hands-free fishing to reduce gamer oppression.
"""
import time
import os

import cv2 as cv
import numpy as np
import pyautogui
from pynput import keyboard
import pydirectinput
import msvcrt

# TODO: Delete this
print("""
Select your resolution:
    (1) 1920x1280
    (2) 2560x1440
    (3) 3620x2036
    (4) 1280x720
""")
resolution_selection = msvcrt.getch()

if resolution_selection == b'1':
    print("Selection: 1920x1280")
    prepare_cast_img = cv.imread('new_world_images/needles/00_needle_1920.jpg', cv.IMREAD_UNCHANGED)
    hold_to_cast_img = cv.imread('new_world_images/needles/01_hold_to_cast_1920.jpg', cv.IMREAD_UNCHANGED)
    cast_release_img = cv.imread('new_world_images/needles/02_cast_release_1920.jpg', cv.IMREAD_UNCHANGED)
    hook_loc_img = cv.imread('new_world_images/needles/02_hook_1920.jpg', cv.IMREAD_UNCHANGED)
    hook_img = cv.imread('new_world_images/needles/03_hook_1920.jpg', cv.IMREAD_UNCHANGED)
    reel_img = cv.imread('new_world_images/needles/04_reel_1920.jpg', cv.IMREAD_UNCHANGED)
    release_img = cv.imread('new_world_images/needles/05_release_1920.jpg', cv.IMREAD_UNCHANGED)
    release_img_2 = cv.imread('new_world_images/needles/05_release_1920.jpg', cv.IMREAD_UNCHANGED)
    success_img = cv.imread('new_world_images/needles/06_success_1920.jpg', cv.IMREAD_UNCHANGED)
elif resolution_selection == b'2':
    print("Selection: 2560x1440")
    prepare_cast_img = cv.imread('new_world_images/needles/00_needle_2560.jpg', cv.IMREAD_UNCHANGED)
    hold_to_cast_img = cv.imread('new_world_images/needles/01_hold_to_cast_2560.jpg', cv.IMREAD_UNCHANGED)
    cast_release_img = cv.imread('new_world_images/needles/02_cast_release_2560.jpg', cv.IMREAD_UNCHANGED)
    hook_loc_img = cv.imread('new_world_images/needles/02_hook_2560.jpg', cv.IMREAD_UNCHANGED)
    hook_img = cv.imread('new_world_images/needles/03_hook_2560.jpg', cv.IMREAD_UNCHANGED)
    reel_img = cv.imread('new_world_images/needles/04_reel_2560.jpg', cv.IMREAD_UNCHANGED)
    release_img = cv.imread('new_world_images/needles/05_release_2560.jpg', cv.IMREAD_UNCHANGED)
    release_img_2 = cv.imread('new_world_images/needles/05_release_2560.jpg', cv.IMREAD_UNCHANGED)
    success_img = cv.imread('new_world_images/needles/06_success_2560.jpg', cv.IMREAD_UNCHANGED)

elif resolution_selection == b'3':
    print("Selection: 3620x2036")
    prepare_cast_img = cv.imread('new_world_images/needles/00_needle.jpg', cv.IMREAD_UNCHANGED)
    hold_to_cast_img = cv.imread('new_world_images/needles/01_hold_to_cast_2.jpg', cv.IMREAD_UNCHANGED)
    cast_release_img = cv.imread('new_world_images/needles/02_cast_release_2.jpg', cv.IMREAD_UNCHANGED)
    hook_loc_img = cv.imread('new_world_images/needles/02_hook_loc.jpg', cv.IMREAD_UNCHANGED)
    hook_img = cv.imread('new_world_images/needles/03_hook_2.jpg', cv.IMREAD_UNCHANGED)
    reel_img = cv.imread('new_world_images/needles/04_reel_2.jpg', cv.IMREAD_UNCHANGED)
    release_img = cv.imread('new_world_images/needles/05_release_2.jpg', cv.IMREAD_UNCHANGED)
    release_img_2 = cv.imread('new_world_images/needles/05_release_3.jpg', cv.IMREAD_UNCHANGED)
    success_img = cv.imread('new_world_images/needles/06_success_2.jpg', cv.IMREAD_UNCHANGED)

elif resolution_selection == b'4':
    print("Selection: 1280x720")
    prepare_cast_img = cv.imread('new_world_images/needles/00_needle_ian.jpg', cv.IMREAD_UNCHANGED)
    hold_to_cast_img = cv.imread('new_world_images/needles/01_hold_to_cast_ian.jpg', cv.IMREAD_UNCHANGED)
    cast_release_img = cv.imread('new_world_images/needles/02_cast_release_ian.jpg', cv.IMREAD_UNCHANGED)
    hook_loc_img = cv.imread('new_world_images/needles/02_hook_ian.jpg', cv.IMREAD_UNCHANGED)
    hook_img = cv.imread('new_world_images/needles/03_hook_ian.jpg', cv.IMREAD_UNCHANGED)
    reel_img = cv.imread('new_world_images/needles/04_reel_ian.jpg', cv.IMREAD_UNCHANGED)
    release_img = cv.imread('new_world_images/needles/05_release_ian.jpg', cv.IMREAD_UNCHANGED)
    release_img_2 = cv.imread('new_world_images/needles/05_release_ian.jpg', cv.IMREAD_UNCHANGED)
    success_img = cv.imread('new_world_images/needles/06_success_ian.jpg', cv.IMREAD_UNCHANGED)
else:
    print("Invalid selection. Goodbye.")

print("""
Nat Pagle here, a bit far from Dustwallow Marsh but I'll do my best!

How to use:
    1. Set your waypoint to behind the spot. (see below)
    2. Press 'b' to start/restart.
    3. Press 'n' to pause.


      /`-.                                  [X] <-- Waypoint
     /    `-.
  O /        `-.
  |-            `-.
  /\\               `-.
 /_/_                 `-.
########~~~~~~~~~~~~~~~~~`<))><~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Warning: Bot should not be left unmonitored for more that 20 minutes.

""")

DEBUG = False

loop_time = time.time()
current_action = "Waiting"

if DEBUG:
    current_action = "Prepare to Cast"

hook_top_left = 0
hook_bottom_right = 0

# Action control to prevent wasting effort
mouse_up = True
moving_right = True

def current_milli_time():
    return round(time.time() * 1000)


if DEBUG:
    cwd = os.getcwd()
    test_start_time = current_milli_time()
    current_run_directory = path = os.path.join(cwd, f"test_data\\{test_start_time}")
    os.mkdir(current_run_directory)

screen_width, screen_height = pyautogui.size()

bottom_mid_top_left_search_area = (screen_width * .5, screen_height * .5)
bottom_mid_bottom_right_search_area = ((screen_width * .7), (screen_height * .9))


def get_screenshot():
    screenshot = pyautogui.screenshot()
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
    if DEBUG:
        cv.imwrite(save_file_name, haystack_img)


def scan_for_image(haystack_img, needle_img, needle_name="unknown", confidence_threshold=0.8):
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if max_val >= confidence_threshold:
        find_str = f'Found [{needle_name}]'
        conf_str = f'Confidence: {max_val:3.2f}'

        if DEBUG:
            print(f'{find_str:20} {conf_str}')
            draw_rectangle_on_match(haystack_img, needle_img, needle_name, max_loc)
        return True
    else:
        # print('Needle not found.')
        return False


def get_hook_search_area(haystack_img, needle_img, needle_name="unknown", confidence_threshold=0.8, max_attempts=100):
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    if max_val >= confidence_threshold:

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]

        top_left = list(max_loc)
        search_area_top_left = tuple([top_left[0] - 100, top_left[1] - 50])
        # make column extend to bottom of screen for those long pulls
        bottom_right = (top_left[0] + needle_w + 100, screen_height - 5)

        if DEBUG:
            cv.rectangle(haystack_img, search_area_top_left, bottom_right, color=(0, 255, 0), thickness=2,
                         lineType=cv.LINE_4)
            save_file_name = f'test_data/{test_start_time}/{current_milli_time()}_{needle_name}.jpg'
            cv.imwrite(save_file_name, haystack_img)

        return list(search_area_top_left), list(bottom_right)

    else:
        return [-1, 0]


def scan_by_area(top_left, bottom_right, needle_img, needle_name="unknown", confidence_threshold=0.8):
    width = bottom_right[0] - top_left[0]
    height = bottom_right[1] - top_left[1]

    sub_screenshot = pyautogui.screenshot(region=(top_left[0], top_left[1], width, height))
    # or: screenshot = ImageGrab.grab()
    sub_screenshot = np.array(sub_screenshot)
    sub_screenshot = cv.cvtColor(sub_screenshot, cv.COLOR_RGB2BGR)

    result = cv.matchTemplate(sub_screenshot, needle_img, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    print(top_left, bottom_right, max_val)
    # print(top_left, bottom_right, width, height,"max_val:", max_val)
    # draw_rectangle_on_match(sub_screenshot, needle_img, needle_name, max_loc)

    if max_val >= confidence_threshold:
        find_str = f'Found [{needle_name}]'
        conf_str = f'Confidence: {max_val:3.2f}'

        if DEBUG:
            print(f'{find_str:20} {conf_str}')
            draw_rectangle_on_match(sub_screenshot, needle_img, needle_name, max_loc)

        return True
    else:
        return False


def set_mouse_up(mouse_is_up):
    if not mouse_is_up:
        pyautogui.mouseUp()
        if DEBUG:
            print("Mouse Up!\n")
        global mouse_up
        mouse_up = True


def set_mouse_down(mouse_is_up):
    if mouse_is_up:
        pyautogui.mouseDown()
        if DEBUG:
            print("Mouse Down...\n")
        global mouse_up
        mouse_up = False


def cast_line(screenshot):
    return


is_fishing = False


def on_press(key):
    global is_fishing
    global current_action
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        key_pressed = key.char  # single-char keys
    except AttributeError as e:
        key_pressed = key.name  # other keys

    if key_pressed == 'b':
        print("Start fishing")
        current_action = "Prepare to Cast"
        is_fishing = True

    if key_pressed == 'n':
        print("Stop fishing")
        is_fishing = False

    # Multi Catch
    if key_pressed in ['1', '2', 'left', 'right']:  # keys of interest
        print('Key pressed: ' + key_pressed)
        return False  # stop listener; remove this if want more keys


def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

# Main Loop
while True:
    # print("truing")
    if is_fishing:
        screenshot = get_screenshot()

        # cv.imshow('Computer Vision', screenshot)

        # print(f'FPS {1 / (time() - loop_time)}')
        loop_time = time.time()

        # Check for marker in top middle of screen
        if current_action == "Prepare to Cast":
            # Look for marker
            top_left_zone = (screen_width / 2 - 80, 5)
            bottom_right_zone = (screen_width / 2 + 80, 200)

            if scan_by_area(top_left_zone, bottom_right_zone, prepare_cast_img, "needle", 0.9):
                current_action = "Cast Line"
                print("Preparing to Cast")
            else:
                mouse_x, mouse_y = pyautogui.position()
                # pyautogui.move(100, 0, 1, pyautogui.easeInQuad)

                if mouse_x >= 2550:
                    moving_right = False
                elif mouse_x <= 50:
                    move_right = True

                if moving_right:
                    pydirectinput.move(30, None)
                else:
                    pydirectinput.move(-30, None)

                print(f"Moving the mouse! (x:{mouse_x}, y:{mouse_y})")

        if current_action == "Cast Line":
            # if scan_for_image(screenshot, hold_to_cast_img, "casting"):
            # print(bottom_mid_top_left_search_area, bottom_mid_bottom_right_search_area)
            print("about to cast line")
            if scan_by_area(bottom_mid_top_left_search_area, bottom_mid_bottom_right_search_area, hold_to_cast_img,
                            "hook", .7):

                set_mouse_down(mouse_up)
                release_time = round(np.random.uniform(1.0, 1.2), 3)
                time.sleep(release_time)
                set_mouse_up(mouse_up)
                time.sleep(1)

                if DEBUG:
                    print(f"Cast Release Time: {release_time}s")
                    print("Find hook location")

                current_action = "Find hook location"

        if current_action == "Find hook location":
            hook_top_left, hook_bottom_right = get_hook_search_area(screenshot, hook_loc_img, "hook_location")

            print(hook_top_left, hook_bottom_right)

            if hook_top_left != -1:
                current_action = "Waiting for fish"

        if current_action == "Waiting for fish":

            if scan_by_area(hook_top_left, hook_bottom_right, hook_img, "hook"):
                set_mouse_down(mouse_up)
                current_action = "Reeling it in"

                if DEBUG:
                    print("Setting the hook")

        if current_action == "Setting the hook":
            if scan_by_area(hook_top_left, hook_bottom_right, hook_img, "hook"):
                set_mouse_down(mouse_up)
                current_action = "Reeling it in"

                if DEBUG:
                    print("Setting the hook")

        if current_action == "Reeling it in":
            # Check if caught
            if scan_for_image(screenshot, hold_to_cast_img, "catch"):
                set_mouse_up(mouse_up)
                current_action = "Prepare to Cast"
                time.sleep(2)

                if DEBUG:
                    print("Caught! Cast Line...")

            # Check if need to back off
            if scan_by_area(hook_top_left, hook_bottom_right, release_img, "spooling", 0.7) or \
                    scan_by_area(hook_top_left, hook_bottom_right, release_img_2, "spooling", 0.7):
                set_mouse_up(mouse_up)
                current_action = "Free-Spool"

                if DEBUG:
                    print("Free-Spool")

        if current_action == "Free-Spool":
            # Check if caught
            if scan_for_image(screenshot, hold_to_cast_img, "catch"):
                set_mouse_up(mouse_up)
                current_action = "Prepare to Cast"
                time.sleep(2)

                if DEBUG:
                    print("Caught! Cast Line...")

            if scan_by_area(hook_top_left, hook_bottom_right, reel_img, "reeling"):
                set_mouse_down(mouse_up)
                current_action = "Reeling it in"

                if DEBUG:
                    print("Reeling it in")

        # 'B' and 'N' are unbound
        if cv.waitKey(1) == ord('b'):
            current_action = "Cast Line"
            print("Started...")

        if cv.waitKey(1) == ord('n'):
            current_action = "Waiting"
            print("Waiting")

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
