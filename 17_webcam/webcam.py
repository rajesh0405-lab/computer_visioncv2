"""Show live webcam video. Press q to close the window."""

import cv2

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise RuntimeError("Could not open the webcam")

try:
    while True:
        success, frame = camera.read()
        if not success:
            print("Could not read a frame from the webcam")
            break
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    camera.release()
    cv2.destroyAllWindows()
