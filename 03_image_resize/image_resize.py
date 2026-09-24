"""Change an image size while keeping the example easy to follow."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

resized = cv2.resize(image, (600, 400))
cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
