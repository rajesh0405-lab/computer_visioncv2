"""Read an image with OpenCV and print its basic details."""

import cv2

IMAGE_PATH = "images/sample.jpg"

image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

print("Image loaded successfully")
print("Width:", image.shape[1])
print("Height:", image.shape[0])
print("Channels:", image.shape[2])
