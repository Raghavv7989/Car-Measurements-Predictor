import cv2
import numpy as np
from config import *
from calibrator import pixel_to_meter

def draw_measurements(image, x, y, w, h, contour, wheels, sidebar_w=300):
    """Draws car, tires, measurement lines, and displays cleanly spaced metrics in a sidebar."""
    if SHOW_BOUNDING_BOX:
        cv2.rectangle(image, (x, y), (x + w, y + h), COLOR_BBOX, 2)

    # Draw length line (horizontal at mid-height)
    y_mid = y + h // 2
    cv2.line(image, (x, y_mid), (x + w, y_mid), COLOR_LENGTH, 2)
    length_cm = pixel_to_meter(w) * 100

    # Draw width line (vertical at mid-width)
    x_mid = x + w // 2
    cv2.line(image, (x_mid, y), (x_mid, y + h), COLOR_WIDTH, 2)
    width_cm = pixel_to_meter(h) * 100

    # Get radii of tires and calculate average
    tire_radii = []
    for (cx, cy, r) in wheels:
        if SHOW_TIRE_CIRCLES:
            cv2.circle(image, (int(cx), int(cy)), int(r), COLOR_TIRE, 2)
        tire_radii.append(pixel_to_meter(r) * 100)
    avg_radius = sum(tire_radii) / len(tire_radii) if len(tire_radii) > 0 else 0.0

    # Create sidebar metrics with proper spacing
    if SHOW_SIDEBAR_METRICS:
        h_img, w_img, _ = image.shape
        sidebar = np.full((h_img, sidebar_w, 3), COLOR_BG, dtype=np.uint8)
        y_pos = 40
        # Draw heading
        cv2.putText(sidebar, "MEASUREMENTS (cm)", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLOR_TEXT, 2)
        y_pos += 60  # blank line
        cv2.putText(sidebar, f"Car Length: {length_cm:.1f}", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLOR_TEXT, 2)
        y_pos += 60  # blank line
        cv2.putText(sidebar, f"Car Width: {width_cm:.1f}", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLOR_TEXT, 2)
        y_pos += 60  # blank line
        cv2.putText(sidebar, f"Tire Radius: {avg_radius:.1f}", (20, y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLOR_TEXT, 2)
        image = np.hstack((image, sidebar))

    return image
