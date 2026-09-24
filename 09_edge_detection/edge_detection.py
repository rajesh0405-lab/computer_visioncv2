"""Find strong intensity changes with the Canny edge detector."""

import cv2

IMAGE_PATH = r"C:\Users\wwwra\OneDrive\Attachments\Desktop\computer_vision\download (2).jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
