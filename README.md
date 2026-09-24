# Computer Vision with Python & OpenCV

A beginner-friendly learning project by **Rajesh Dev**. This repository contains small, independent programs for practicing image processing, webcam operations, and basic computer vision with Python and OpenCV.

This is my own practice project inspired by common computer vision exercises. It is not the original source of Python or OpenCV, and it does not claim ownership of those tools.

## About the Project

The lessons start with simple image operations and gradually introduce useful computer vision ideas. Each folder contains one Python file that can be read, changed, and run on its own.

Most image lessons use `images/sample.jpg`. Add your own test image at that path before running them. The document scanner expects `images/document.jpg`.

## Objectives

- Learn how `cv2.imread()` reads an image.
- Learn how `cv2.imshow()` displays an image.
- Practice changing image size, position, color, and shape.
- Understand edges, thresholds, contours, masks, and segmentation.
- Try beginner-level face, eye, motion, and object detection.
- Build confidence by reading and modifying small programs.

## Technologies Used

- Python
- OpenCV (`opencv-python`)
- NumPy

## Installation

1. Install Python 3.9 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .venv\\Scripts\\Activate.ps1
   ```

4. Install the packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Create an `images` folder and add a test image named `sample.jpg`.

## How to Run the Programs

Run a file from the project root. For example:

```bash
python 01_image_reading/image_reading.py
python 09_edge_detection/edge_detection.py
python 17_webcam/webcam.py
```

Image windows close when you press a key. Webcam examples use `q` to quit. Camera examples require a working webcam. The face and eye lessons use Haar cascade files included with OpenCV, so no separate model download is needed.

## Folder Structure

```text
Rajesh-Computer-Vision/
├── README.md
├── requirements.txt
├── LICENSE
├── 01_image_reading/image_reading.py
├── 02_image_display/image_display.py
├── 03_image_resize/image_resize.py
├── 04_image_crop/image_crop.py
├── 05_image_rotate/image_rotate.py
├── 06_image_flip/image_flip.py
├── 07_image_grayscale/grayscale.py
├── 08_image_blur/blur.py
├── 09_edge_detection/edge_detection.py
├── 10_thresholding/thresholding.py
├── 11_contours/contours.py
├── 12_drawing_shapes/drawing_shapes.py
├── 13_text_on_image/text.py
├── 14_color_detection/color_detection.py
├── 15_face_detection/face_detection.py
├── 16_eye_detection/eye_detection.py
├── 17_webcam/webcam.py
├── 18_motion_detection/motion_detection.py
├── 19_background_subtraction/background_subtraction.py
├── 20_image_segmentation/segmentation.py
├── 21_object_tracking/object_tracking.py
├── 22_hand_detection/hand_detection.py
├── 23_document_scanner/document_scanner.py
├── 24_image_edge_project/edge_project.py
└── 25_mini_computer_vision_project/main.py
```

## Exercises

1. **Image reading** - Read an image and print its width, height, and channels.
2. **Image display** - Display an image in an OpenCV window.
3. **Image resize** - Change an image to a fixed width and height.
4. **Image crop** - Select a rectangular region with array slicing.
5. **Image rotate** - Rotate an image around its center.
6. **Image flip** - Flip an image horizontally.
7. **Grayscale** - Convert a color image to shades of gray.
8. **Blur** - Apply Gaussian blur to soften details.
9. **Edge detection** - Find strong edges with Canny.
10. **Thresholding** - Turn grayscale pixels into a simple black-and-white mask.
11. **Contours** - Draw outlines around regions in a thresholded image.
12. **Drawing shapes** - Draw lines, rectangles, circles, and text on a canvas.
13. **Text on image** - Add a message to a photograph.
14. **Color detection** - Find green pixels with an HSV mask.
15. **Face detection** - Find faces with OpenCV's Haar cascade.
16. **Eye detection** - Look for eyes inside detected face regions.
17. **Webcam** - Display live frames from the default camera.
18. **Motion detection** - Compare nearby webcam frames to reveal movement.
19. **Background subtraction** - Estimate the moving foreground in a video.
20. **Image segmentation** - Isolate blue pixels in an image.
21. **Object tracking** - Follow the largest blue region in webcam video.
22. **Hand detection** - Experiment with a simple skin-color mask.
23. **Document scanner** - Find a four-corner document and correct its perspective.
24. **Image edge project** - Create and save an edge image.
25. **Mini project** - Detect faces and save an annotated result image.

## What I Learned

I learned that computer vision programs are built from small steps: read data, convert it into a useful color space, process it, display the result, and clean up resources. I practiced `cv2.imread()`, `cv2.imshow()`, `cv2.waitKey()`, `cv2.destroyAllWindows()`, drawing functions, masks, contours, webcam frames, and basic cascade detection.

## Future Improvements

- Add a small `images` folder with personal test images.
- Add command-line arguments for input and output paths.
- Improve hand detection with a hand-landmark library.
- Add keyboard controls for camera settings.
- Compare different edge and blur settings.
- Add unit tests for the non-camera image-processing functions.

## Author

**Rajesh Dev**

**© 2026 Rajesh Kummari**

This project is shared for learning and practice.
