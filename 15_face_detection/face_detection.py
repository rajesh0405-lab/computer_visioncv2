"""Detect faces with OpenCV's built-in Haar cascade model."""

import cv2

IMAGE_PATH = "images/sample.jpg"
image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

print(f"Faces found: {len(faces)}")
cv2.imshow("Face detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
