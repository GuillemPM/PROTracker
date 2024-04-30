from time import sleep
import utils
import os
import numpy as np
import cv2


class Tracker:
    def findClock(self):
        ss = utils.Screenshot(2)
        if ss is None:
            return

        clock_img = cv2.imread(
            os.path.join(os.path.dirname(__file__), "assets\\clock.png"),
            cv2.IMREAD_GRAYSCALE,
        )

        result = cv2.matchTemplate(
            cv2.cvtColor(ss, cv2.COLOR_RGB2GRAY), clock_img, cv2.TM_CCOEFF_NORMED
        )

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = clock_img.shape[1]
        h = clock_img.shape[0]
        print([max_loc[0], max_loc[1]])
        cv2.rectangle(ss, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)
        cv2.imwrite("prueba.png", ss)
        sleep(10)
        # cv2.imshow("abc", ss)

        # cv2.waitKey()
        return

    def search(self):
        ss = utils.Screenshot()
        if ss is None:
            return
        poke_img = cv2.imread(
            os.path.join(os.path.dirname(__file__), "assets\\pidgey2.jpg"),
            cv2.IMREAD_COLOR,
        )
        result = cv2.matchTemplate(ss, poke_img, cv2.TM_CCOEFF_NORMED)
        # print()

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        w = poke_img.shape[1]
        h = poke_img.shape[0]

        print([w, h])
        cv2.rectangle(ss, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)

        # cv2.imshow("abc", ss)
        # cv2.moveWindow("abc", 0, 0)
        # cv2.waitKey()
