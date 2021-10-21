"""This is for testing.

Static image matching to new world haystacks.
"""

import cv2 as cv
import numpy as np

# for loop on all images
image_collection = [
    ['new_world_images/haystacks/01_hold_to_cast.jpg', 'new_world_images/needles/01_hold_to_cast.jpg'],
    ['new_world_images/haystacks/02_cast_release.jpg', 'new_world_images/needles/02_cast_release.jpg'],
    ['new_world_images/haystacks/03_hook.jpg', 'new_world_images/needles/03_hook.jpg'],
    ['new_world_images/haystacks/04_reel.jpg', 'new_world_images/needles/04_reel.jpg'],
    ['new_world_images/haystacks/05_release.jpg', 'new_world_images/needles/05_release.jpg'],
    ['new_world_images/haystacks/06_success.jpg', 'new_world_images/needles/06_success.jpg'],
]

for image_set in image_collection:

    haystack_url = image_set[0]
    needle_url = image_set[1]

    haystack_img = cv.imread(haystack_url, cv.IMREAD_UNCHANGED)
    needle_img = cv.imread(needle_url, cv.IMREAD_UNCHANGED)

    output_url = f'new_world_images/output/{haystack_url.split("/")[-1]}'

    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)

    # Get Confidence Values
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    print(f'Best match top left position: {max_loc}')
    print(f'Best match confidence:{max_val}')

    def draw_rectangle_on_match():
        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]
        top_left = max_loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)


    threshold = 0.2
    if max_val >= threshold:
        print('Found needle.')
        draw_rectangle_on_match()
    else:
        print('Needle not found.')

    # cv.imshow('Result', result)
    cv.waitKey()
    cv.imwrite(output_url, haystack_img)
