import numpy as np

def format_measurement(meters):
    """Format a distance in meters as cm or m, for display."""
    cm = meters * 100
    return f"{cm:.1f} cm" if cm < 100 else f"{meters:.2f} m"
