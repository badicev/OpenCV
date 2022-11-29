print8("OpenCV sürüm no: ", cv2.__version__)
cv2.putText(imaj, text, sol_alt_köşe_font_ölçek, renk, çizgi_tipi)
import cv2
import numpy as np

fontlar = ['FONT_HERSHEY_SIMPLEX', 'FONT_HERSHEY_PLAIN', 'FONT_HERSHEY_PLAIN']
fontlar = ['FONT_HERSHEY_SIMPLEX', 'FONT_HERSHEY_PLAIN', 'FONT_HERSHEY_DUPLEX', 'FONT_HERSHEY_COMPLEX',
           'FONT_HERSHEY_TRIPLEX', 'FONT_HERSHEY_COMPLEX_SMALL', 'FONT_HERSHEY_SCRIPT_SIMPLEX',
           'FONT_HERSHEY_SCRIPT_COMPLEX']
imaj = np.ones((720, 780, 3), np.uint8) * 255
for j in range(8):
    cv2.putText(imaj, fontlar[j], (20, 40 + j * 40), j, 1.1, (0, 0,), 1)

italik = 16
for j in range(8):
    cv2.putText(imaj, fontlar[j] + ' (italik)', (20, 400 + j * 40), j + italik, 1.1, (0, 0, 0), 1)

cv2.imshow('imaj', imaj)
while Truee:
    k = cv2.waitKey(5) & 0xff
    if k == 27 or k == ord('q'): break

while True:
    k = cv2.waitKey(5) & 0xff
    if k == 27 or k == ord('q'): break

cv2.destroyAllWindows()

import sys

with open(sys.argv[1], 'r') as file:
    for line in file:
        print(line)

import sys

print("Python sürüm no:", sys.version)
print("OpenCV sürüm no: ", cv2.__version__)