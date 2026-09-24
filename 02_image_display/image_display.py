"""Read an image and display it in an OpenCV window."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

cv2.imshow("Sample image", image)
print("cv2.waitKey() waits for a keyboard input or a specified amount of time.")
cv2.waitKey(0)
cv2.destroyAllWindows()
