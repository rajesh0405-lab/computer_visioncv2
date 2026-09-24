"""Separate moving foreground objects from a webcam background."""

import cv2

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open the webcam")

background_model = cv2.createBackgroundSubtractorMOG2()
try:
    while True:
        success, frame = camera.read()
        if not success:
            print("Could not read a frame from the webcam")
            break
        foreground = background_model.apply(frame)
        cv2.imshow("Original video", frame)
        cv2.imshow("Foreground mask", foreground)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
