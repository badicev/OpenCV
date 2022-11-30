'''
hsv_renk.py
BGR renklerin HSV aralıklarını bulmak için.

'''

import numpy as np
import cv2
bgr = np.uint8([[[255, 0, 0]]])
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
print("renk = ", bgr)
print("hsv = ", hsv)


h0 = hsv[0][0][0]
h1 = hsv[0][0][1]
h2 = hsv[0][0][2]

if h0 != 255:
    ha0 = h0 - 10
    hu0 = h0 + 10
    if ha0 < 0:
        ha0 += 180
        hu0 += 180
else:
    ha0 = hu0 = 255
print(f"hsv alt= ({ha0} {100} {100})")
print(f"hsv üst= ({hu0} {255} {255})")