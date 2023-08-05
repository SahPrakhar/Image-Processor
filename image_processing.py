import cv2
import numpy as np

def apply_grayscale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def apply_blur(image):
    blurred_image = cv2.blur(image, (30, 30))
    return blurred_image

def apply_edge_detection(image):
    edges = cv2.Canny(image, 100, 200)
    return edges

def apply_sharpen(image):
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1,  9, -1],
                                  [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
    return sharpened_image

def apply_rotation(image, angle):
    rows, cols, _ = image.shape
    rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    return rotated_image

def apply_color_adjustment(image, brightness=0, contrast=1.0, saturation=1.0):
    adjusted_image = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    hsv_image = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)
    s = cv2.addWeighted(s, saturation, 0, 0, 0)
    adjusted_hsv_image = cv2.merge((h, s, v))
    final_image = cv2.cvtColor(adjusted_hsv_image, cv2.COLOR_HSV2BGR)
    return final_image

def apply_threshold(image, threshold_value):
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

    return image