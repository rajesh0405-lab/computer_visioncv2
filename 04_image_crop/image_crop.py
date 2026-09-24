"""Select a rectangular part of an image using array slicing."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

cropped = image[50:300, 80:400]
cv2.imshow("Cropped image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
