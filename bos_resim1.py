import numpy as np
import cv2
deneme = np.zeros((400, 400, 3), dtype=np.uint8)
deneme[:] = (0, 255, 255)
cv2.imshow('deneme', deneme)
cv2.waitKey(0)
cv2.destroyAllWindows()

