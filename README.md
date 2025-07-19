# 🚗 Car Measurements Predictor 🧠

This project uses **Python + OpenCV** to detect and annotate a vehicle's **length**, **width**, and **average tire radius** from a side-view image.

---


The app will detect:
- 🧮 Car Length
- 📏 Car Width
- 🎯 Tire Radius (using circle detection and average computation)

✔️ All measurements are converted from pixels to **centimeters**, using a calibrated pixel-to-meter ratio.

---

## 🧠 Features

- ✅ Contour-based vehicle detection
- ✅ Hough Circle Transform to localize tires
- ✅ Draws length & width lines on car body
- ✅ Draws tire circles and shows **averaged tire radius only**
- ✅ Live sidebar with real-world measurements in cm
- ✅ Fully pure Python + OpenCV (no ML dependencies)

---

## 🧱 Structure

car_measurements/
├── main.py # Runs the full pipeline
├── config.py # General constants (PIXELS_PER_METER, colors)
├── detector.py # Car + tire detection logic
├── visualizer.py # Clean visualization with overlay + sidebar
├── calibrator.py # Converts pixels to meters/cm
├── helpers.py # Simple utility formatting
text

---

## 🚀 Usage

### 1. Install Requirements

pip install numpy opencv-python
text

> No extra ML dependencies required.

---

### 2. Set Your Calibration

Edit `config.py`:

PIXELS_PER_METER = 200.0 # 🔧 Change based on real-world scale
text

Use a known-distance reference (e.g., measure a car length in cm and get the pixel length from the image).

---

### 3. Run the App

python main.py your_car_image.jpg
text

> The app will open a window showing the annotated results with all measurements ⬅️ and a sidebar 🟫 on the right.


---

## 🧩 Customization

You can easily:
- 💡 Add wheelbase, door spacing, etc.
- 🌈 Change colors in `config.py`
- 🧪 Hook in YOLOv5 for smarter detection (optional)

---

## 📄 License

MIT License © Raghavv7989.

---

## ❤️ Acknowledgments

This project is part of my portfolio to showcase **practical computer vision applications for automotive scenes**.

🌟 If you liked it, **star the repo** and share your use case!
