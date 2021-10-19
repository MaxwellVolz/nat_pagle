"""This is for testing.

Static image template matching example.
Reference: https://www.learncodebygaming.com/blog/opencv-object-detection-in-games-python-tutorial-1
"""

import cv2 as cv
import numpy as np

haystack_img = cv.imread('images/albion_farm.jpg', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('images/albion_cabbage.jpg', cv.IMREAD_UNCHANGED)

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


threshold = 0.8
if max_val >= threshold:
    print('Found needle.')
    draw_rectangle_on_match()
else:
    print('Needle not found.')


cv.imshow('Result', result)
cv.waitKey()
cv.imwrite('result.jpg', haystack_img)
