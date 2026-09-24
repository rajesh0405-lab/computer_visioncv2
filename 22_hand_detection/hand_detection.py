"""Try a simple skin-color mask as an introduction to hand detection."""

import cv2
import numpy as np

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open the webcam")

try:
    while True:
        success, frame = camera.read()
        if not success:
            print("Could not read a frame from the webcam")
            break
        hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_skin = np.array([0, 20, 70])
        upper_skin = np.array([20, 255, 255])
        skin_mask = cv2.inRange(hsv_image, lower_skin, upper_skin)
        cv2.imshow("Possible hand regions", skin_mask)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
