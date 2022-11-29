"""
renkler_bgr.py

R: red G: green B:blue
"""

import cv2
import numpy as np


def bgr_renkler():
    img = np.ones((510, 510,3), np.uint8)*80 #480*480 piksel boyutlu gri görüntü
    cv2.circle(img, (90,90), 80, (255, 0, 0), -1)
    cv2.circle(img, (250, 90), 80, (0, 255, 0), -1)
    cv2.circle(img, (410, 90), 80, (0, 0, 255), -1)
    cv2.circle(img, (90, 250), 80, (255, 255, 0), -1)
    cv2.circle(img, (250, 250), 80, (255, 0,  255), -1)
    cv2.circle(img, (410, 250), 80, (0, 255, 255), -1)
    cv2.circle(img, (170, 410), 80, (0, 0, 0), -1)
    cv2.circle(img, (330, 410), 80, (255, 255, 255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(img, '(255, 0, 0)', (15+30, 95), font, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(img, '(0, 255, 0)', (175 + 30, 95), font, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(img, '(0, 0, 255)', (335 + 30, 95), font, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(img, '(255, 255, 0)', (15 + 20, 250), font, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(img, '(255, 0, 255)', (175 + 20, 250), font, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(img, '(0, 255, 255)', (335 + 20, 250), font, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(img, '(0, 0, 0)', (95 + 40, 410), font, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(img, '(255, 255, 255)', (255+5, 410), font, 0.6,
                (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('imaj', img)
    cv2.imwrite('bgr_renkler.jpg', img)
    cv2.waitKey(0)
    while True:
        k = cv2.waitKey(5) & 0xFF
        if k == 27 or k == ord('q'): break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    bgr_renkler()
