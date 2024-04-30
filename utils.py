import mss
import numpy as np
import cv2
import win32gui


def Screenshot(zone=0):
    # Zones: 0 = Full, 1 = TopLeft, 2 = TopRight, 3 = BottomLeft, 4 = BottomRight
    hwnd = win32gui.FindWindowEx(None, None, None, "PROClient")
    rect = win32gui.GetWindowRect(hwnd)
    if not rect:
        return

    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y

    if zone == 1:  # TopLeft
        w = w // 2
        h = h // 2
    elif zone == 2:  # TopRight
        x += w // 2
        w = w // 2
        h = h // 2
    elif zone == 3:  # BottomLeft
        y += h // 2
        w = w // 2
        h = h // 2
    elif zone == 4:  # BottomRight
        x += w // 2
        y += h // 2
        w = w // 2
        h = h // 2

    ssInstance = mss.mss()
    ss = ssInstance.grab({"left": x, "top": y, "width": w, "height": h})

    img = np.array(ss)
    img = cv2.cvtColor(img, cv2.IMREAD_COLOR)

    return img
