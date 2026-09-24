"""Create a simple foreground mask with color-based segmentation."""

import cv2
import numpy as np

IMAGE_PATH = "images/sample.jpg"
image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
segmented = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Segmentation mask", mask)
cv2.imshow("Segmented blue area", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
