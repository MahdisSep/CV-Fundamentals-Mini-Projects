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

## 🖼️ Examples

| Project | Input Image | Output Example |
| :--- | :--- | :--- |
| **Tic-Tac-Toe** |  | *Result: "X Wins"* |
| **Calculate Area** |  | *Output: A dictionary of color areas (e.g., {'red': 21300, 'green': 15496, ...})* |
| **Skin Detection** |  |  |

## 💡 How to Run

To run any of the scripts, you can call the main function with an image path.

### Example for `calculate_area.py`:

```python
import cv2
from calculate_area import calculate_area

img_path = 'path/to/your/image.png'
image = cv2.imread(img_path)

if image is not None:
    areas = calculate_area(image)
    print(areas)
else:
    print("Error: Could not load image.")
```

