"""A small project that saves an edge version of a sample image."""

import cv2

INPUT_PATH = r"C:\Users\wwwra\OneDrive\Attachments\Desktop\computer_vision\download (2).jpg"
OUTPUT_PATH = r"C:\Users\wwwra\OneDrive\Attachments\Desktop\computer_vision\sample_edges.jpg"

image = cv2.imread(INPUT_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {INPUT_PATH}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 80, 160)
if not cv2.imwrite(OUTPUT_PATH, edges):
    raise OSError(f"Could not save image: {OUTPUT_PATH}")

cv2.imshow("Saved edge project", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"Saved the edge image to {OUTPUT_PATH}")
