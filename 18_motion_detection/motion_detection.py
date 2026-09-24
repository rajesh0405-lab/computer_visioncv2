"""Highlight movement by comparing webcam frames."""

import cv2

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open the webcam")

previous_gray = None
try:
    while True:
        success, frame = camera.read()
        if not success:
            print("Could not read a frame from the webcam")
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        if previous_gray is not None:
            difference = cv2.absdiff(previous_gray, gray)
            _, motion_mask = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
            cv2.imshow("Motion mask", motion_mask)
        previous_gray = gray
        cv2.imshow("Motion detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
