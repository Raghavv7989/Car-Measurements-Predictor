import sys
import cv2
from config import *
from detector import detect_car, detect_wheels
from visualizer import draw_measurements
from calibrator import pixel_to_meter

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path>")
        return
    image = cv2.imread(sys.argv[1])
    if image is None:
        print("Image not found.")
        return
    x, y, w, h, contour = detect_car(image)
    wheels = detect_wheels(image, WHEEL_SEARCH_AREA)
    annotated = draw_measurements(image.copy(), x, y, w, h, contour, wheels, 300)
    cv2.imshow("Car Measurements", annotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
