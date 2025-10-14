import cv2 as cv
import numpy as np
# from google.colab.patches import cv2_imshow

def calculate_area(image):
    # Define more accurate color ranges in HSV
    colors = {
        "red": [([0, 100, 100], [10, 255, 255]), ([160, 100, 100], [179, 255, 255])],
        "green": [([35, 100, 100], [85, 255, 255])],
        "blue": [([100, 150, 0], [140, 255, 255])],
        "yellow": [([20, 100, 100], [30, 255, 255])],
        "purple": [([130, 50, 50], [160, 255, 255])],
        "gray": [([0, 0, 50], [180, 50, 200])], # Adjust gray range as needed
    }

    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    areas = {}
    found_color = False

    for name, ranges in colors.items():
        mask = np.zeros(image.shape[:2], dtype=np.uint8)

        # Create the mask based on color ranges
        for lower, upper in ranges:
            mask |= cv.inRange(hsv, np.array(lower), np.array(upper))

        # Find contours
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        total_area = 0

        for cnt in contours:
            contour_area = cv.contourArea(cnt)  # Use contour area directly
            x, y, w, h = cv.boundingRect(cnt)

            # Check if it's a square (w == h) or rectangle (w != h)
            if 0.95<=float(w/h)<=1.05:
                # For squares, add 4 to both width and height and then calculate area
                total_area += (w - 1) * (h - 1)
            else:
                # For rectangles, multiply the area by 3
                total_area += (h-1) * (w-1) * 3

            # # Display color name and dimensions (only for display, not for area calculation)
            # cv.putText(image, name, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)  # Display color name above shapes
            # cv.putText(image, f"w={w}, h={h}", (x, y + h + 20), cv.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)

        if total_area > 0:
            areas[name] = total_area
            found_color = True

    # If no color found, add black color with total pixel count
    if not found_color:
        black_area = image.shape[0] * image.shape[1]  # Total number of pixels in the image
        areas["black"] = black_area

    # # Display the image with color labels and dimensions
    # cv2_imshow(image)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    # Return areas in the requested format
    return "\n".join([f"{color}, {int(area)}" for color, area in areas.items()])

# image_path = "new4.png"
# image = cv.imread(image_path)

# if image is None:
#     print("Error: Could not read the image file.")
# else:
#     print(calculate_area(image))
