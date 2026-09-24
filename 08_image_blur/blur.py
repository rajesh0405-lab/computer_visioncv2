"""Blur an image to reduce small details and noise."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

blurred = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow("Blurred image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
