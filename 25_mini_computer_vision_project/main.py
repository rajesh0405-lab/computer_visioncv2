"""Mini project: detect faces in an image and save the result."""

import cv2

INPUT_PATH = "images/sample.jpg"
OUTPUT_PATH = "images/faces_found.jpg"

image = cv2.imread(INPUT_PATH)
if image is None:
    raise FileNotFoundError(f"Could not load image: {INPUT_PATH}")

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, 1.1, 5)

for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

if not cv2.imwrite(OUTPUT_PATH, image):
    raise OSError(f"Could not save image: {OUTPUT_PATH}")

print(f"Faces found: {len(faces)}")
print(f"Saved result to {OUTPUT_PATH}")
cv2.imshow("Mini computer vision project", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
