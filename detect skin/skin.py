import cv2
import numpy as np
def detect_skin(image_path):
    image = cv2.imread(image_path)
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_skin = np.array([0, 20, 70])  
    upper_skin = np.array([20, 255, 255])   
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    
    output_image = np.zeros_like(image)
    output_image[mask == 255] = [255, 255, 255]  
    
    return output_image

