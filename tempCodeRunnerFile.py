import cv2
import numpy as np
from calibrator import pixel_to_meter
from helpers import format_measurement

def draw_measurements(image, x, y, w, h, contours, wheels):
    color = (0, 255, 0)  # Green color for main lines and circles

    # Draw the car bounding box
    cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    # --- Draw length line (horizontal middle line) ---
    line_y = y + h // 2
    cv2.line(image, (x, line_y), (x + w, line_y), (255, 0, 0), 2)  # Blue line for length
    length_cm = pixel_to_meter(w) * 100
    cv2.putText(image, f"Length: {length_cm:.1f} cm",
                (x + 10, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

    # --- Draw width line (vertical at the center x) ---
    line_x = x + w // 2
    cv2.line(image, (line_x, y), (line_x, y + h), (0, 255, 255), 2)  # Yellow line for width
    width_cm = pixel_to_meter(h) * 100
    cv2.putText(image, f"Width: {width_cm:.1f} cm",
                (line_x + 10, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # --- Draw circles around tyres and label radius ---
    for (cx, cy, r) in wheels:
        cv2.circle(image, (cx, cy), r, color, 2)
        radius_cm = pixel_to_meter(r) * 100
        cv2.putText(image, f"R: {radius_cm:.1f} cm",
                    (cx - r, cy - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return image
