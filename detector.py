import cv2
import numpy as np
from config import CAR_CONTOUR_THRESH, WHEEL_SEARCH_AREA

def detect_car(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, CAR_CONTOUR_THRESH, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest)
    return x, y, w, h, largest

def detect_wheels(image, y_range=None):
    h_img, w_img = image.shape[:2]
    y_start = int(y_range[0] * h_img) if y_range else 0
    y_end = int(y_range[1] * h_img) if y_range else h_img
    roi = image[y_start:y_end, :]
    circles = cv2.HoughCircles(
        cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY),
        cv2.HOUGH_GRADIENT,
        1,
        50,
        param1=50,
        param2=30,
        minRadius=10,
        maxRadius=70
    )
    wheels = []
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for (cx, cy, r) in circles[0]:
            wheels.append((cx, cy + y_start, r))
    return wheels
