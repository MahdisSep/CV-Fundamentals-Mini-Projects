# CV-Fundamentals-Mini-Projects

A collection of fundamental computer vision mini-projects implemented in Python, primarily utilizing the **OpenCV** library. These projects demonstrate key image processing concepts such as color space manipulation, thresholding, morphological operations, and feature detection (Hough Transform, Contours).

## 🚀 Projects Included

| Project File | Description | Key Concepts |
| :--- | :--- | :--- |
| `tic_tac_toe.py` | Detects the current state of a Tic-Tac-Toe game board (X Wins, O Wins, or Ongoing) from an image. | **Hough Circle Transform** for 'O's, **Hough Line Transform** for 'X's, Image Gridding. |
| `calculate_area.py` | Calculates the total pixel area for specific color regions (red, green, blue, yellow, purple, gray) within an image. | **HSV Color Space** for segmentation, **Contour Detection** (`cv2.findContours`), Area Calculation (`cv2.contourArea`). |
| `skin.py` | Segments and isolates skin regions in an image using color thresholding. | **HSV Color Space** (specific skin range), **Binary Masking**. |

## 🛠️ Requirements

The projects require the following libraries:
-   Python 3.x
-   OpenCV (`cv2`)
-   NumPy

You can install the dependencies using pip:
```bash
pip install opencv-python numpy
````

## 💡 How to Run

To run any of the scripts, you can call the main function with an image path.


