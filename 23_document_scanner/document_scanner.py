"""Find a large four-corner document and show a top-down view."""

import cv2
import numpy as np

IMAGE_PATH = "images/document.jpg"
image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

original = image.copy()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
edges = cv2.Canny(blurred, 75, 200)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=cv2.contourArea, reverse=True)
document = None
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    corners = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    if len(corners) == 4:
        document = corners.reshape(4, 2).astype(np.float32)
        break

if document is None:
    raise ValueError("Could not find a four-corner document")

ordered = document[np.argsort(document[:, 1])]
top = ordered[:2][np.argsort(ordered[:2, 0])]
bottom = ordered[2:][np.argsort(ordered[2:, 0])]
source_points = np.float32([top[0], top[1], bottom[1], bottom[0]])
target_points = np.float32([[0, 0], [600, 0], [600, 800], [0, 800]])
matrix = cv2.getPerspectiveTransform(source_points, target_points)
scanned = cv2.warpPerspective(original, matrix, (600, 800))

cv2.imshow("Scanned document", scanned)
cv2.waitKey(0)
cv2.destroyAllWindows()
