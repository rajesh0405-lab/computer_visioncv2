"""Track a blue object in webcam video with an HSV color mask."""

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
        mask = cv2.inRange(hsv_image, np.array([90, 50, 50]), np.array([130, 255, 255]))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest = max(contours, key=cv2.contourArea)
            if cv2.contourArea(largest) > 500:
                x, y, width, height = cv2.boundingRect(largest)
                cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
        cv2.imshow("Object tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
