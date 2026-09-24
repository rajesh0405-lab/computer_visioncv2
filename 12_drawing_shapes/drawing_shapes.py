"""Draw lines, rectangles, circles, and text on a blank image."""

import cv2
import numpy as np

canvas = np.zeros((500, 700, 3), dtype=np.uint8)
cv2.line(canvas, (40, 40), (300, 40), (255, 0, 0), 4)
cv2.rectangle(canvas, (40, 100), (250, 250), (0, 255, 0), 3)
cv2.circle(canvas, (450, 180), 80, (0, 0, 255), -1)
cv2.putText(canvas, "OpenCV shapes", (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Drawing shapes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
