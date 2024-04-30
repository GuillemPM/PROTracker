import sys
import cv2
import numpy as np
import mss

from tracker import Tracker


# ssHandler = mss.mss()

# battle_img = cv2.cvtColor(cv2.imread('battle2.png'), cv2.COLOR_BGR2GRAY)
# poke_img = cv2.imread('teddiursa.png', cv2.IMREAD_GRAYSCALE)

# cv2.imshow('Battle', battle_img)
# cv2.waitKey()

# cv2.imshow('Poke', poke_img)
# cv2.waitKey()

# result = cv2.Canny(battle_img, threshold1=200, threshold2=300)
# cv2.imshow('ad', result)
# cv2.waitKey()

# threshold = 0.8
# w, h = poke_img.shape[::-1]
# loc = np.where( result >= threshold)
# for pt in zip(*loc[::-1]):
#  cv2.rectangle(battle_img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

# cv2.imshow('Result', battle_img)
# cv2.waitKey()

tracker = Tracker()

while True:
    tracker.findClock()
    # tracker.search()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        sys.exit()
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# w = poke_img.shape[1]
# h = poke_img.shape[0]


# cv2.rectangle(battle_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)

# cv2.imshow('Battle_scanned', battle_img)
# cv2.waitKey()
