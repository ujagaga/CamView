#!/usr/bin/env python3
# First install open-cv: pip install opencv-python

import cv2

WIDTH = 800
HEIGHT = 600

cam_id = 0
cam = cv2.VideoCapture(cam_id)
cam.set(3, WIDTH)
cam.set(4, HEIGHT)

title = 'Camview'

cv2.namedWindow(title, flags=cv2.WINDOW_GUI_NORMAL)
cv2.resizeWindow(title, WIDTH, HEIGHT)

while True:
    
    if cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) < 1:
        break
    ret, frame = cam.read()

    try:
        cv2.imshow(title, cv2.flip(frame, 1))
    except:
        pass

    keypress = cv2.waitKey(1)
    if 47 < keypress < 59:
        cam.release()

        try:
            cam_id = keypress - 48
            cam = cv2.VideoCapture(cam_id)
            cam.set(3, WIDTH)
            cam.set(4, HEIGHT)

        except Exception as e:
            print(e)
            cam_id = 0
            cam = cv2.VideoCapture(cam_id)
            cam.set(3, WIDTH)
            cam.set(4, HEIGHT)

cam.release()


