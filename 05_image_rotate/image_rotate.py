"""Rotate an image around its center."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

height, width = image.shape[:2]
center = (width // 2, height // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (width, height))

cv2.imshow("Rotated image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
