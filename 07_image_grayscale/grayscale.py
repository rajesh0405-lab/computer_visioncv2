"""Convert a color image into grayscale."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
