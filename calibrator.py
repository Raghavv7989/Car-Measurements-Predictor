from config import PIXELS_PER_METER

def pixel_to_meter(pixel_distance):
    return pixel_distance / PIXELS_PER_METER

def meter_to_pixel(meter_distance):
    return meter_distance * PIXELS_PER_METER
