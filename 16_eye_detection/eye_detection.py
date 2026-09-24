"""Detect eyes inside faces using two Haar cascade models."""

import cv2

IMAGE_PATH = "images/sample.jpg"
image = cv2.imread(IMAGE_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {IMAGE_PATH}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
faces = face_cascade.detectMultiScale(gray_image, 1.1, 5)

for x, y, width, height in faces:
    face_gray = gray_image[y:y + height, x:x + width]
    face_color = image[y:y + height, x:x + width]
    eyes = eye_cascade.detectMultiScale(face_gray, 1.1, 5)
    for eye_x, eye_y, eye_width, eye_height in eyes:
        cv2.rectangle(face_color, (eye_x, eye_y), (eye_x + eye_width, eye_y + eye_height), (255, 0, 0), 2)

cv2.imshow("Eye detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
