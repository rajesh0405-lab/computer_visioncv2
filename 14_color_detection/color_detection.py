"""Detect a green region by converting an image to HSV color space."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_green = (35, 50, 50)
upper_green = (85, 255, 255)
mask = cv2.inRange(hsv_image, lower_green, upper_green)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Green color mask", mask)
cv2.imshow("Detected green", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
