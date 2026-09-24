"""Flip an image horizontally, vertically, or in both directions."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

flipped = cv2.flip(image, 1)
cv2.imshow("Horizontally flipped image", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
