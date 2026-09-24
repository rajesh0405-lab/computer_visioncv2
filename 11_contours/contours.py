"""Find the outlines of objects in a simple thresholded image."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresholded = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = image.copy()
cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
cv2.imshow("Contours", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
