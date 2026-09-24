"""Separate light and dark areas with a binary threshold."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded image", thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()
