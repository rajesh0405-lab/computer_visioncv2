"""Add a readable message to an image."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

cv2.putText(image, "Learning Computer Vision", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Text on image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
